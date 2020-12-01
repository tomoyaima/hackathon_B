from time import time, sleep
import cv2

# VideoCameraを追加
class VideoCamera():
    def __init__(self):
        self.frames = []
        self.files = []
        self.MAX_FRAME_NUM = 10 # 撮影枚数を指定
        self.RECORD_INTERVAL = 1 # 撮影のインターバルを指定

        self.record()
        

    def get_frame(self):
        # 撮影された画像を順に返す
        for file in self.files:
            self.frames.append(open(file, 'rb').read())
        return self.frames[int(time()) % len(self.frames)]

    def record(self):
        print("aa")
        self.cap = cv2.VideoCapture(0)

        cnt = 0
        while True:
            # 撮影したファイルの保存先を指定
           
            path = './'+str(cnt) + '.jpg'
            ret, frame = self.cap.read()
            self.files.append(path)

            cv2.imwrite(path, frame)

            # ESCキーで停止する
            k = cv2.waitKey(1)
            if k == 27:
                print("aa")
                break

            # 指定した枚数を撮影したら停止する
            cnt += 1
            if cnt == self.MAX_FRAME_NUM:
                break

            # 撮影のインターバルを取る
            sleep(self.RECORD_INTERVAL)

        self.cap.release()
        cv2.destroyAllWindows()