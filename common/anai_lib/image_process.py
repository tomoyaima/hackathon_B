import cv2
# from pygame import mixer
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

flow = 0.75
fupper = 3
frame_rate = 30

def filtering(sig, fold):
    # ones = np.ones(fold) / fold
    # moving_avg = np.convolve(sig, ones, 'valid')
    # return moving_avg
    wn = np.array([flow, fupper]) * 2 / frame_rate
    # define filter coefs
    (b, a) = signal.butter(fold, wn, btype='bandpass')
    # and make it attributes
    result = signal.filtfilt(b, a, sig, axis=0)

    return result

def pulse_de(data):

    l = int(frame_rate * 1.6)

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

    H = filtering(H, 3)

    return H

face_cascade_path = '/mnt/d/chiat/python_ws/hackathon_B/haarcascade_frontalface_default.xml'
eye_cascade_path = '/mnt/d/chiat/python_ws/hackathon_B/haarcascade_eye.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

cap = cv2.VideoCapture(0)
start_time = time.time() 
count = 0
face_count = 0
try_count = 0
all_tracking_time = 0
angry_count = 0
while True:
    try_count += 1 
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = []
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    if len(faces) == 0:
        count += 1
    if count == 100 :
        angry_count +=1
        if angry_count >= 4:
            # mixer.init()        #初期化
            # mixer.music.load("C:/Users/ME_PC_2020/Desktop/Hackathon/_game_swordman-death1.mp3")
            # mixer.music.play(1) 
            angry_count = 0
            count = 0
        elif angry_count < 4:
            # mixer.init()        #初期化
            # mixer.music.load("C:/Users/ME_PC_2020/Desktop/Hackathon/line-girl1-kaatsu1.mp3")
            # mixer.music.play(1)
            count = 0
    
    for x, y, w, h in faces:
        face_count +=1 
#         print(tracking_start_time) 
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = img[y: y + h, x: x + w]
        face_gray = gray[y: y + h, x: x + w]
        
        
        eyes = eye_cascade.detectMultiScale(face_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    
#     if try_count == 900:
#         pulse = pulse_de(X1)
#         plt.plot(pulse)
#         plt.show()
    
    roi = img[y: y+h, x:x+w]
    rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    (r1, g1, b1) = cv2.split(rgb)
    mean_b1 = np.mean(b1)
    mean_g1 = np.mean(g1)
    mean_r1 = np.mean(r1)
    if try_count == 1:
        X1 = np.array([mean_r1, mean_g1, mean_b1])
    else:
        X1 = np.vstack((X1, np.array([mean_r1, mean_g1, mean_b1])))
        
    cv2.imshow('video image', img)
    key = cv2.waitKey(10)
    
    if key == 27:  # ESCキーで終了
        pulse = pulse_de(X1)
        plt.plot(pulse)
        plt.show()
        
        end_time = time.time()
        rec_time = end_time - start_time
        all_tracking_time = (face_count/try_count)*rec_time
        if all_tracking_time < 10:
            print(a)
            # mixer.init()        #初期化
            # mixer.music.load("C:/Users/ME_PC_2020/Desktop/Hackathon/line-girl1-sonotyoushisonotyousi1.mp3")
            # mixer.music.play(1)
        elif all_tracking_time < 20:
            print(b)
            # mixer.init()        #初期化
            # mixer.music.load("C:/Users/ME_PC_2020/Desktop/Hackathon/people-stadium-cheer1.mp3")
            # mixer.music.play(1)
        elif all_tracking_time > 20:
            print(c)
            # mixer.init()        #初期化
            # mixer.music.load("C:/Users/ME_PC_2020/Desktop/Hackathon/people-studio-kyaa1.mp3")
            # mixer.music.play(1)
        break

# 経過時間を表示
print("起動時間　　:"+ str(round(rec_time,1)) + "秒")
print("視線検出時間:"+ str(round(all_tracking_time,1)) + "秒") 
cap.release()
cv2.destroyAllWindows()
