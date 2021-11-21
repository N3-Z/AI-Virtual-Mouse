import cv2
import mediapipe as mp
# from math import sqrt
# import time
# import pyautogui
import HandTrackingModule
import win32api
# pypiwin32
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
click = 0


ptime = 0
# wcam, hcam = 1280, 720


video = cv2.VideoCapture(0)

# video.set(cv2.CAP_PROP_FRAME_WIDTH, wcam)
# video.set(cv2.CAP_PROP_FRAME_HEIGHT, hcam)


with mp_hands.Hands(min_detection_confidence=0.3, min_tracking_confidence=0.3) as hands:
    while video.isOpened():
        _, frame = video.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        fh,fw, _ = frame.shape
        results= hands.process(frame)
        
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)


        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(250,44,250), thickness=2, circle_radius=1),)
            
            
        if results.multi_hand_landmarks != None:
            for handLandmarks in results.multi_hand_landmarks:
                for point in mp_hands.HandLandmark:

                    normalizedLandmark = handLandmarks.landmark[point]
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, fw, fh)
                    point = str(point)
                    
                    if point == 'HandLandmark.INDEX_FINGER_TIP':
                        try:
                            indexfingertip_x = pixelCoordinatesLandmark[0]
                            indexfingertip_y = pixelCoordinatesLandmark[1]
                            win32api.SetCursorPos((indexfingertip_x*2, indexfingertip_y*3))
                        except:
                            pass
                    # elif point == 'HandLandmark.THUMB_TIP':
                    #     try:
                    #         thumbfingertip_x = pixelCoordinatesLandmark[0]
                    #         thumbfingertip_y = pixelCoordinatesLandmark[1]
                    #     except:
                    #         pass
                    # try:
                    #     # pyautogui.moveTo(indexfingertip_x, indexfingertip_y)
                    #     distance_x= sqrt((indexfingertip_x-thumbfingertip_x)**2 + (indexfingertip_x-thumbfingertip_x)**2)
                    #     distance_y= sqrt((indexfingertip_y-thumbfingertip_y)**2 + (indexfingertip_y-thumbfingertip_y)**2)

                    #     if distance_x < 5 or distance_y < -5:
                    #         click += 1

                    #         if click%5 == 0:
                    #             # print("single click")
                    #             pyautogui.click()
                                
                    # except:
                    #     pass
        # ctime = time.time()
        # fps = 1 / (ctime - ptime)
        # ptime = ctime
        # cv2.putText(frame, str(int(fps)), (20,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

        cv2.imshow('Virtual Mouse', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    
video.release()
cv2.clea

