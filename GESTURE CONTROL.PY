import cv2, nuppy as np ,mediapipe as mp, screenbrightness_control as sbc
from math import hypot

hands = mp.solution.hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
draw = mp.solution.drawing_utils

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Camera not found")
    exit()

while True:
    ok, img = cap.read()
    if not ok: break
    img = cv2.flip(img, 1)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for i, hand in enumerate(RESULT.MULTI_HAND_LANDMARKS):
            label = result.multi_handedness[i].classification[0].label
            draw.draw_landmarks(img, hand, mp.solution.hands.HAND_CONNECTIONS)

            thumb = hand.landmark[mp.solution.hands.HandLandmark.THUMB_TIP]
            index = hand.landmark[mp.solution.hands.HandLandmark.INDEX_FINGER_TIP]
            h, w, c = img.shape
            t_pos, i_pos = int(thumb.x * w), int(thumb.y * h), int(index.x * w),
            int(index.y * h)
            cv2.circle(img, t_pos, 10 (255, 0, 0), cv2.FILLED)
            cv2.circle(img, i_pos, 10 (255, 0, 0), cv2.FILLED)
            cv2.line(img, t_pos, i_pos,(0, 255, 0), 3)

            dist = hypot(i_pos[0]-t_pos[0], i_pos[1]-t_pos[1])
            if label == "left":
                brightness = np.interp(dist, [30, 200], [0, 100])
                sbc.set_brightness(brightness)
                cv2.rectangle(img , (100, 150), (135, 400), (255, 0 , 0).2)
                cv2.rectangle(img , (100, int(brightness * 2.5 + 150)), (135, 400), (0, 255 , 0). -1)
                cv2.puttext(img, f"Brightness: {int(brightness)} %", (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Gesture Control", img)
    if cv2.waitkey(0 & 0xFF == ord("q")):
        break

cap.release()
cv2.destroyAllWindows()