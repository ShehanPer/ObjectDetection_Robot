import cv2 as cv
import numpy as np
import Bluetooth as bl

url = 'http://192.168.8.101:8080/video'
prevCircles = None
dist = lambda x1, y1, x2, y2: np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

video = cv.VideoCapture(url)
connects = bl.connect()
while True:
    
    ret, frame = video.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    frame = cv.resize(frame, (640, 480))
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurFrame = cv.GaussianBlur(grayFrame, (19, 19), 0)

    circles = cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT, 1.2, 100, param1=50, param2=60, minRadius=75, maxRadius=400)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None:
                chosen = i
            if prevCircles is not None:
                print('Ball is ditected')
                connects.send_data('1')
                if dist(chosen[0], chosen[1], prevCircles[0], prevCircles[1]) <= dist(i[0], i[1], prevCircles[0], prevCircles[1]):
                    chosen = i
                

        # Calculate bounding box coordinates
        top_left = (chosen[0] - chosen[2], chosen[1] - chosen[2])
        bottom_right = (chosen[0] + chosen[2], chosen[1] + chosen[2])

        # Draw the bounding box
        cv.rectangle(frame, top_left, bottom_right, (0, 255, 0), 5)

        # Display the text "Circle" above the bounding box
        font = cv.FONT_HERSHEY_SIMPLEX
        text_position = (top_left[0], top_left[1] - 10)  # Position the text above the top-left corner of the box
        cv.putText(frame, 'Ball', text_position, font, 0.5, (0, 255, 0), 2)
        prevCircles = chosen

   
    cv.imshow('Circles', frame,)
    if cv.waitKey(1) == ord('q'):
        break   
if connects:
    connects.close()
video.release()
cv.destroyAllWindows()