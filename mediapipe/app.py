import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

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

        # הפיכת תמונה - חשוב!
        frame = cv2.flip(frame, 1)

        # המרה ל-RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # התיקון הקריטי! -> תמונה רציפה בזיכרון
        rgb = np.ascontiguousarray(rgb)

        # שליחת התמונה למדיה-פייפ
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Hand Tracking", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

cap.release()
cv2.destroyAllWindows()
