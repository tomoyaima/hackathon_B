import cv2
import time
# import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

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
        self.angry_count_ = 0
        self.X1_ = []

        self.frame_rate = 1
        self.angry_time = 5.0   # 何秒見ていないとキレるか
        self.mad_count = 4      # 何回キレるとブチ切れるか
        self.nowathing_time = 3.0       # 何秒見ていないとサボり判定か
        self.watching_time = 3.0        # 何秒見ていると視聴判定か
        self.watching = True


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

        l = int(self.frame_rate * 1.6)
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
        H = self.filtering(H, 3)
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
            self.angry_count_ = 0
            print('視線検出!')

        # if self.noeye_count_ % int(self.angry_time / self.frame_rate) == 0:
        #     self.angry_count_ +=1
        #     if self.angry_count_ >= self.mad_count:
        #         print("Death!!!")
        #         self.angry_count_ = 0
        #     elif self.angry_count_ < self.mad_count:
        #         print('コラ')
        
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
            # cv2.imshow('video image', img)

        self.rec_time_ = time.time() - self.start_time_
        self.all_tracking_time_ = (self.face_count_/self.try_count_)*self.rec_time_

        if int(self.eye_count_ / self.frame_rate) > self.watching_time :
            self.watching = True
        elif int(self.noeye_count_ / self.frame_rate) > self.nowathing_time :
            self.watching = False
        return self.watching


    def get_palse(self):
        pulse = self.pulse_de(self.X1_)
        # plt.plot(pulse)
        # plt.show()

    def reset(self):
        self.rec_time_ = 0
        self.noeye_count_ = 0
        self.face_count_ = 0
        self.try_count_ = 0
        self.all_tracking_time_ = 0
        self.angry_count_ = 0
        self.X1_ = []

    def print_debug(self):
        """経過時間を出力"""
        print("起動時間　　:"+ str(round(self.rec_time_,1)) + "秒")
        print("視線検出時間:"+ str(round(self.all_tracking_time_,1)) + "秒")
        if self.watching:
            print('視聴判定中...')
        else :
            print('サボり判定中...')
        # print('count : ', self.count_, ', angry_count : ', self.angry_count_, ', face_count : ', self.face_count_, ', try_count : ', self.try_count_)
