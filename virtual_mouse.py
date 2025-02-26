import cv2 #To capture videos 
import mediapipe as mp
import util

mpHands=mp.solutions.hands
hands=mpHands.Hands( static_image_mode=False,#To capture vid
                    model_complexity=1,
                    min_detection_confidence=0.7, # minimum confidence score (70%) for the detection
                    min_tracking_confidence=0.7, #for tracking
                    max_num_hands=1
                    )


def main():
    cap=cv2.VideoCapture(0) #0-primary camera-capture
    draw=mp.solutions.drawing_utils
    
    try:
        while cap.isOpened():
            ret, frame=cap.read() #ret-bool val if frame is read True

            if not ret:
                break
            frame=cv2.flip(frame,1) #for mirroring the image in vertical axis
            frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)#mediapipe gives in bgr format
            processed = hands.process(frameRGB)#contains landmark of hands

            landmarks_list=[]

            if processed.multi_hand_landmarks: #to seggrgate one landmark from many
                hand_landmarks = processed.multi_hand_landmarks[0]
                draw.draw_landmarks(frame,hand_landmarks,mpHands.HAND_CONNECTIONS)

                for lm in hand_landmarks.landmark:
                    landmarks_list.append((lm.x,lm.y))

               # print(landmarks_list)

#func to detect gesture
            detect_gestures=(frame,landmarks_list,processed)




            cv2.imshow('Frame',frame)
            if cv2.waitKey(2) & 0xFF==27: #waiting for 2ms 27-esc key ascii. if clicked exit
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ =='__main__':
    main()

#Mediapipe to detect hand points
#cv from opencv to access camera
