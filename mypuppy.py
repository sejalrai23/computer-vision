import cv2
img =cv2.imread('DATA/car_plate.jpg')

while True:
    cv2.imshow("puppy",img)
    
    #if we've waited at least 1 ms and we've pressed the esc key 27 meanse esc key
    
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyAllWindows()