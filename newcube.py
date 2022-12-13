import numpy as np
import cv2
import time
from twophase import solve
bounds = {
	"red" : (np.array([160, 50, 50]), np.array([180, 255, 255])),
	"blue" : (np.array([110, 75, 75]), np.array([130, 255, 255])),
	"green" : (np.array([35, 0, 0]), np.array([85, 255, 255])),
	"yellow" : (np.array([20, 75, 75]), np.array([40, 255, 255])),
	"white" : (np.array([0, 0, 20]), np.array([180, 30, 255])),
	"orange" : (np.array([10, 100, 100]), np.array([20, 255, 255]))
}

def density(img, color):
	lower = bounds[color][0]
	upper = bounds[color][1]
	mask = cv2.inRange(img, lower, upper)
	return np.sum(mask)/255

def cubestr(data):
	ret = ""
	for i in "URFDLB":
		ret += "".join(data[i])
	for i in "URFDLB":
		ret = ret.replace(data[i][4], i)
	return ret

def screen_record():
    last_time = time.time()
    cv2.startWindowThread()
    # cv2.namedWindow("preview")
    cap = cv2.VideoCapture(1)
    faces = "FUDLRB"
    idx = 0

    data = {
        "F" : ["", "", "", "", "", "", "", "", ""],
        "U" : ["", "", "", "", "", "", "", "", ""],
        "D" : ["", "", "", "", "", "", "", "", ""],
        "L" : ["", "", "", "", "", "", "", "", ""],
        "R" : ["", "", "", "", "", "", "", "", ""],
        "B" : ["", "", "", "", "", "", "", "", ""]
    }

    while(True):
        _, img = cap.read()
        last_time = time.time()
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        colors = {
        	"red" : (0, 0, 255),
        	"blue" : (255, 0, 0),
        	"green" : (0, 255, 0),
        	"yellow" : (0, 255, 255),
        	"white" : (255, 255, 255),
        	"orange" : (0, 165, 255)
        }

        offset = 75
        z = 0
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                px = 358 + j * offset
                py = 280 + i * offset


                maxDens = [0, "white"]
                crop = img_hsv[(py-35):(py+35), (px-35):(px+35)]
                for k in ("red", "blue", "green", "yellow", "white", "orange"):
                    d = density(crop, k)
                    if d > maxDens[0]:
                        maxDens[0] = d
                        maxDens[1] = k

                cv2.circle(img,(px, py), 5, colors[maxDens[1]], -1)
                data[faces[idx]][z] = maxDens[1][0]
                z += 1


        lower = np.array([110, 100, 100])
        upper = np.array([130, 255, 255])
        
        mask = cv2.inRange(img_hsv, lower, upper)
        output = cv2.bitwise_and(img, img, mask = mask)

        cv2.imshow(faces[idx] + ' Face', img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cap.release()
            break

        if cv2.waitKey(25) & 0xFF == ord('h'):
            idx += 1
            if idx == len(faces):
                print(solve(cubestr(data)))
                cv2.destroyAllWindows()
                cap.release()
                break
screen_record()