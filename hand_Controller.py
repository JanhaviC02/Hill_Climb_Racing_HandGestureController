import cv2
import mediapipe as mp
import keyboard  
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
cap = cv2.VideoCapture(0)
def count_fingers(hand_landmarks):
    """Count extended fingers using landmark positions."""
    fingers = []

    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    finger_tips = [8, 12, 16, 20]
    finger_bottoms = [6, 10, 14, 18]

    for tip, bottom in zip(finger_tips, finger_bottoms):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[bottom].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)  

print("Starting webcam... Press 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            finger_count = count_fingers(hand_landmarks)

            if finger_count == 0:
                keyboard.release("right")  
                keyboard.press("left")
                cv2.putText(frame, "Brake", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)
                print("Brake Pressed")
            elif finger_count == 5:
                keyboard.release("left")   
                keyboard.press("right")    
                cv2.putText(frame, "Gas", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 4)
                print("Gas Pressed")
            else:
                keyboard.release("right")
                keyboard.release("left")
                cv2.putText(frame, f"Neutral ({finger_count} fingers)", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.imshow("Hand Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
hands.close()
keyboard.release("left")
keyboard.release("right")
print("Application closed.")