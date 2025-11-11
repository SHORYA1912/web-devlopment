import cv2, numpy as np, mediapipe as mp, time

# Initialize MediaPipe
hands = mp.solutions.hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
draw = mp.solutions.drawing_utils

filters = ['NONE', 'GRAY', 'SEPIA', 'NEG', 'BLUR']
current_filter, last_action, debounce = 0, 0, 1
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Camera not found")
    exit()

def apply_filter(img, filter_type):
    if filter_type == 'GRAY':
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if filter_type == 'SEPIA':
        m = np.array([[0.272, 0.534, 0.131],
                      [0.349, 0.686, 0.168],
                      [0.393, 0.769, 0.189]])
        return cv2.transform(img, m)
    if filter_type == 'NEG':
        return cv2.bitwise_not(img)
    if filter_type == 'BLUR':
        return cv2.GaussianBlur(img, (15, 15), 0)
    return img

t = (0, 0)  # Track previous position of index tip

while True:
    ok, img = cap.read()
    if not ok:
        break

    img = cv2.flip(img, 1)
    RES = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if RES.multi_hand_landmarks:
        for im, hand in enumerate(RES.multi_hand_landmarks):
            label = RES.multi_handedness[im].classification[0].label
            draw.draw_landmarks(img, hand, mp.solutions.hands.HAND_CONNECTIONS)

            index_tip = hand.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
            h, w, _ = img.shape
            i_pos = int(index_tip.x * w), int(index_tip.y * h)
            cv2.circle(img, i_pos, 10, (255, 0, 0), cv2.FILLED)

            # Gesture logic
            if label == "Right":
                if i_pos[1] < h // 3 and debounce:
                    current_filter = (current_filter + 1) % len(filters)
                    last_action = time.time()
                    debounce = 0
                elif time.time() - last_action > 1:
                    debounce = 1

            if abs(t[0] - i_pos[0]) < 20 and abs(t[1] - i_pos[1]) < 20:
                if label == "Left":
                    current_filter = 0
            elif abs(t[0] - i_pos[0]) > 40 or abs(t[1] - i_pos[1]) > 40:
                t = i_pos

    img = apply_filter(img, filters[current_filter])
    cv2.putText(img, f"Filter: {filters[current_filter]}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("Gesture Control Screenshot", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

