import cv2 ,time ,pyautogui
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

SCROLL_SPEED = 300
SCROLL_DELAY = 1
Cam_width, Cam_height= 640, 480

def detect_gesture():
    finger = []

    tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP,]

    for tip in tips:
        if landmarks[tip].y < landmarks[tip - 2].y:
            finger.append(1)

            Thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
            Thumb_ip = landmarks[mp_hands.HandLandmark.THUMB_IP]

            if(handedness = "Right"):
                if Thumb_tip.x < Thumb_ip.x:
                    finger.append(1)

    return "scroll_up" if sum(finger)_ == [5] else "scroll_down" if finger == [] else "none"
cap = cv2.VideoCapture(0)
cap.set(3, Cam_width)
cap.set(4, Cam_height)
last_scroll_time = p_time = 0
while cap isopened():
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
