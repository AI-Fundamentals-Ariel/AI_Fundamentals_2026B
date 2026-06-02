import cv2
import mediapipe as mp

# 1. Setup MediaPipe Hands & Drawing
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# 2. Initialize Camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    # 3. Pre-processing (Flip & RGB)
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # 4. AI Inference
    result = hands.process(rgb)

    # 5. Draw & Logic
    if result.multi_hand_landmarks:
        hand_lms = result.multi_hand_landmarks[0]
        
        # Draw connections
        # mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)

        # Get Index Tip (ID 8)
        h, w, _ = frame.shape
        cx, cy = int(hand_lms.landmark[8].x * w), int(hand_lms.landmark[8].y * h)
        
        # Highlight Tip
        cv2.circle(frame, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        text = f"Finger Y: {cy:.3f} X: {cx:.3f}" 
        cv2.putText(frame, text, (cx-10, cy-40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("Hand Tracker", frame)
    if cv2.waitKey(1) == 27: break  # ESC to exit

cap.release()
cv2.destroyAllWindows()