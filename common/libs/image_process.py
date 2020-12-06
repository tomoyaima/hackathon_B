from common.anai_lib.resampling import resampling_sp
import cv2
import time
# import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.interpolate import interp1d
import math

import config.setting as setting

class SightDetector:

    def __init__(self):

        FACE_CASCADE_PATH = setting.FACE_CASCADE_PATH
        EYE_CASCADE_PATH = setting.EYE_CASCADE_PATH
        self.face_cascade_ = cv2.CascadeClassifier(FACE_CASCADE_PATH)
        self.eye_cascade_ = cv2.CascadeClassifier(EYE_CASCADE_PATH)
        self.flow_ = 0.75
        self.fupper_ = 3
        self.start_time_ = time.time()
        self.rec_time_ = 0
        self.noeye_count_ = 0
        self.eye_count_ = 0
        self.face_count_ = 0
        self.try_count_ = 0
        self.all_tracking_time_ = 0
        self.X1_ = []
        self.palse_ = []

        # デフォルト値
        self.frame_rate = 3
        self.nowathing_time = 3.0       # 何秒見ていないとサボり判定か
        self.watching_time = 3.0        # 何秒見ていると視聴判定か
        self.get_palse_interval = 5       # 集中力を測る感覚(秒)
        self.watching = True
        self.concentration = -1

    def filtering(self, sig, fold):
        # ones = np.ones(fold) / fold
        # moving_avg = np.convolve(sig, ones, 'valid')
        # return moving_avg
        wn = np.array([self.flow_, self.fupper_]) * 2 / self.frame_rate
        # define filter coefs
        (b, a) = signal.butter(fold, wn, btype='bandpass')
        # and make it attributes
        result = signal.filtfilt(b, a, sig, axis=0)
        return result

    def pulse_de(self, data):

        l = self.frame_rate + 1
        H = np.zeros(data.shape[0])
        for t in range(0, (data.shape[0] - l)):
            # Step 1: Spatial averaging
            C = data[t:t + l - 1, :].T
            # C = mean_rgb.T
            # Step 2 : Temporal normalization
            mean_color = np.mean(C, axis=1)
            # print("Mean color", mean_color)
            diag_mean_color = np.diag(mean_color)
            # print("Diagonal",diag_mean_color)
            diag_mean_color_inv = np.linalg.inv(diag_mean_color)
            # print("Inverse",diag_mean_color_inv)
            Cn = np.matmul(diag_mean_color_inv, C)
            # Cn = diag_mean_color_inv@C
            # print("Temporal normalization", Cn)
            # print("Cn shape", Cn.shape)
            # Step 3:
            projection_matrix = np.array([[0, 1, -1], [-2, 1, 1]])
            S = np.matmul(projection_matrix, Cn)
            # S = projection_matrix@Cn
            # Step 4:
            # 2D signal to 1D signal
            std = np.array([1, np.std(S[0, :]) / np.std(S[1, :])])
            P = np.matmul(std, S)
            # P = std@S
            # Step 5: Overlap-Adding
            H[t:t + l - 1] = H[t:t + l - 1] + (P - np.mean(P)) / np.std(P)
        # フィルターは削除
        # try:
        #     H = self.filtering(H, 3)
        # except:
        #     print('filter ERROR!')
        return H

    def detect(self, img):
        self.try_count_ += 1
        if self.try_count_ == 1:
            # 初起動なら
            self.start_time_ = time.time()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = []
        # 顔検出
        faces = self.face_cascade_.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        if len(faces) == 0:
            self.noeye_count_ += 1
            self.eye_count_ = 0
            print('視線未検出......')
        else:
            self.noeye_count_ = 0
            self.eye_count_ += 1
            print('視線検出!')
        
        for x, y, w, h in faces:
            self.face_count_ +=1 
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = img[y: y + h, x: x + w]
            face_gray = gray[y: y + h, x: x + w]
            eyes = self.eye_cascade_.detectMultiScale(face_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            roi = img[y: y+h, x:x+w]
            rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
            (r1, g1, b1) = cv2.split(rgb)
            mean_b1 = np.mean(b1)
            mean_g1 = np.mean(g1)
            mean_r1 = np.mean(r1)
            if self.face_count_ == 1:
                self.X1_ = np.array([mean_r1, mean_g1, mean_b1])
            else:
                self.X1_ = np.vstack((self.X1_, np.array([mean_r1, mean_g1, mean_b1])))

        self.rec_time_ = time.time() - self.start_time_
        self.all_tracking_time_ = (self.face_count_/self.try_count_)*self.rec_time_
        if (self.face_count_ ) % (int(self.get_palse_interval) * int(self.frame_rate)) == 0 and self.eye_count_ != 0:
            # get_palse_interval毎に集中度計算
            self.get_palse()

        if int(self.eye_count_ / self.frame_rate) > self.watching_time :
            self.watching = True
        elif int(self.noeye_count_ / self.frame_rate) > self.nowathing_time :
            self.watching = False
        return self.watching

    def resampling_sp(self, time, data, fs_re, s_time, e_time): # 引数：時間[s]、データ、リサンプリング周波数[Hz]、リサンプリング開始時間[s]、リサンプリング終了時間[s]
        """ データをリサンプリングする関数（3次スプライン補間を使用。時間の単位は「秒」にすること） """
        try:
            f_CS = interp1d(time, data, kind='cubic')               # 3次スプライン補間
            time_re = np.arange(s_time, e_time+1/fs_re, 1/fs_re)    # リサンプリング後の時間配列を作成（自由に決めてOK）
            data_re = f_CS(time_re)                                 # 3次スプライン補間を用いてリサンプリング    
            return time_re, data_re                                 # リサンプリング後の時間、リサンプリング後のデータ
        except:
            print('resampling ERROR!!')
            return

    def get_palse(self):
        try:
            self.pulse_ = self.pulse_de(self.X1_)
            #プロットするために時間（フレームレート）を作っている
            t = np.linspace(0, len(self.pulse_)-1, len(self.pulse_))
            t , self.pulse_ = self.resampling_sp(t, self.pulse_, fs_re=10 * self.frame_rate, s_time=math.ceil(t[0]), e_time=math.floor(t[-1])) 

            maxid = signal.argrelmax(self.pulse_, order=3)  #脈拍の最大点を取り出すためにidを受け取ってる

            max_pulse= t[maxid[0]]                          #脈拍の最大点の時間（フレーム数）を受け取っている
            rr = np.zeros(len(max_pulse))                 #rrインターバル（脈拍間隔）を受け取るために作る
            rr_s = np.zeros(len(max_pulse))

            fps = self.face_count_/round(self.rec_time_,1)  #カメラのフレームレート（1秒あたりの画像の枚数）を計算。        
            Concentration_count = 0
            correction = 0.5
            for i in range(0, len(max_pulse) - 1, 1):           #rrインターバルを計算する
                rr[i] = max_pulse[i+1] - max_pulse[i]
                rr_s[i] = rr[i]/fps+correction              #だいぶ怪しい手法ですが、精度が低いので無理やり上げています。
                if rr_s[i] > 1.5:
                    Concentration_count += 1

            self.concentration = Concentration_count/len(rr_s)

            print("集中率     :"+ str(round(self.concentration * 100 ,1)) + "％")
        except:
            print('palse ERROR!!')

    def reset(self):
        self.rec_time_ = 0
        self.noeye_count_ = 0
        self.face_count_ = 0
        self.try_count_ = 0
        self.all_tracking_time_ = 0
        self.X1_ = []
        self.watching = True

    def print_debug(self):
        """経過時間を出力"""
        print("起動時間　　:"+ str(round(self.rec_time_,1)) + "秒")
        print("視線検出時間:"+ str(round(self.all_tracking_time_,1)) + "秒")
        if self.watching:
            print('視聴判定中...')
        else :
            print('サボり判定中...')
        # print('count : ', self.count_, ', angry_count : ', self.angry_count_, ', face_count : ', self.face_count_, ', try_count : ', self.try_count_)
