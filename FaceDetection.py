import cv2
import sys
from PIL import Image as PImg
from wand.image import Image as WImg

def Swirl(img_path, swirl_intensity):
    ''' Load face detection '''
    faces = cv2.CascadeClassifier("resources/faceDetection.xml")
    ''' Load face image '''
    img = cv2.imread(img_path)
    ''' Fix format of image -> cv2 opens in BGR '''
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ''' Find faces '''
    detections = faces.detectMultiScale(img_gray,scaleFactor=1.2, minNeighbors=4)

    ''' Photoshop Roblox heads '''
    '''
    pil_image = Image.open(img_path)
    roblox = Image.open("resources/roblox.png")
    for (x, y, w, h) in detections:
        print(str(x) + "\t" + str(y) + "\t" + str(w) + "\t" + str(h))
        resized = roblox.resize((int(w * 1.4), int(h * 1.4)))
        pil_image.paste(resized, (x - int(w * 0.2), y - int(h * 0.2)), mask=resized)
        pil_image.save("output.png")
    '''

    pil_image = PImg.open(img_path)
    for (x, y, w, h) in detections:
        cut_image = pil_image.crop((x, y, x + w, y + h))
        cut_image.save("tmp.png")
        with WImg(filename='tmp.png') as i:
            i.swirl(degree=int(swirl_intensity))
            i.save(filename="tmp.png")
        swirled_img = PImg.open("tmp.png")
        pil_image.paste(swirled_img, (x, y))
    pil_image.save("output.png")

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("This script needs two args.\n#1 -> Path to image (string).\n#2 -> Swirl intensity (int 0 to 360).")
    else:
        try:
            Swirl(sys.argv[1], sys.argv[2])
        except Exception as e:
            print("ERROR -> this script needs two args.\n#1 -> Path to image (string).\n#2 -> Swirl intensity (int 0 to 360).")
            print(str(e))