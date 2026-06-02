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
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb = np.ascontiguousarray(rgb)

        result = hands.process(rgb)

        y_val = None

        if result.multi_hand_landmarks:
            lm = result.multi_hand_landmarks[0].landmark
            y_val = lm[8].y   # ערך בין 0–1

            # נקודה
            h, w, _ = frame.shape
            x = int(lm[8].x * w)
            y = int(lm[8].y * h)
            cv2.circle(frame, (x, y), 10, (0, 0, 255), -1)

        text = f"Finger Y: {y_val:.3f}" if y_val else "No hand detected"
        cv2.putText(frame, text, (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

        cv2.imshow("DEBUG FINGER Y", frame)
        if cv2.waitKey(1) == 27:
            break

cap.release()
cv2.destroyAllWindows()
