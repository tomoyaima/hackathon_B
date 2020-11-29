import cv2
import os

SAVE_DIR = "/images"
# if not os.path.isdir(SAVE_DIR):
#     os.mkdir(SAVE_DIR)

def canny(image):
    save_path = os.path.join(SAVE_DIR, "test.png")
    # image = cv2.Canny(image, 100, 200)
    cv2.imwrite("test.png", image)
    print("saved image!")
    return
