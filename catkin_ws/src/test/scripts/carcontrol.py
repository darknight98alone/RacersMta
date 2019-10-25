import cv2

def detectline(image):
    (h,w) = image.shape[:2]
    image = image[h//2:h,:w]
    return image

def showImage(image):
    cv2.imshow("ok",image)
    
# if __name__ == '__main__':
#     image = cv2.imread("./saved/1.jpg")
#     image = detectline(image)
#     print(image.shape[:2])