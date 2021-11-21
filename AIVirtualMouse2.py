import cv2
import HandTrackingModule as htm

import win32api


def main():
    cap = cv2.VideoCapture(0)
    hands = htm.FindHands()
    cap.set(3, 1280)
    cap.set(4, 800)

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        listPos = hands.getPosition(frame, [8])
        
        index_fingerup = hands.index_finger_up(frame)
        middle_fingerup = hands.middle_finger_up(frame)

        msg = ""
        # if index_fingerup == True and middle_fingerup == True:
        #     msg = "index_fingerup + middle_fingerup"
        # elif index_fingerup == True:
        #     msg = "index_fingerup"
        # elif middle_fingerup == True:
        #     msg = "middle_fingerup"



        # "HandLandmark.INDEX_FINGER_TIP"

        # for pt in listPos:
        #     cv2.circle(frame, pt, 5, (0,255,0), cv2.FILLED)
        
        if len(listPos) > 0 and index_fingerup == True and middle_fingerup == True:
            win32api.SetCursorPos((listPos[0][0]*1, listPos[0][1]*1))
            # msg = str(listPos[0][0]) +"," + str(listPos[0][1]) + " " + str(pg.position()[0]) + "," + str(pg.position()[1]) 
        # cv2.putText(frame, str(msg), (20,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

        cv2.imshow("AI Virtual Mouse Testing", frame)
        if cv2.waitKey(10) == ord("q"):
            break

if __name__ == "__main__":
    main()

