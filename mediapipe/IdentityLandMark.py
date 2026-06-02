import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # מראה
        h, w, c = frame.shape

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb = np.ascontiguousarray(rgb)

        result = hands.process(rgb)

        if result.multi_hand_landmarks:

            hand = result.multi_hand_landmarks[0]

            # Landmark 8 = קצה האצבע המורה
            x = int(hand.landmark[8].x * w)
            y = int(hand.landmark[8].y * h)

            # ציור נקודה במקום שבו מצביעים
            cv2.circle(frame, (x, y), 10, (0, 0, 255), -1)

            # הצגת הקורדינטות על המסך
            text = f"X: {x}, Y: {y}"
            cv2.putText(frame, text, (x + 15, y - 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (255, 255, 255), 2)

        cv2.imshow("Pointer Tracking", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

cap.release()
cv2.destroyAllWindows()
