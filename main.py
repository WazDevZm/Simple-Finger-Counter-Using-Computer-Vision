import cv2
import mediapipe as mp
import pyttsx3
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

myEngine = pyttsx3.init()
myEngine.setProperty('rate', 150)
myEngine.setProperty('volume', 1)

WidthCam = 720
HeightCam = 720
cap = cv2.VideoCapture(0)
cap.set(3, WidthCam)
cap.set(4, HeightCam)
cap.set(cv2.CAP_PROP_FPS, 60)

lastFingerCount = -1
lastTime = time.time()

myFingerTips = [
    mp_hands.HandLandmark.THUMB_TIP,
    mp_hands.HandLandmark.INDEX_FINGER_TIP,
    mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
    mp_hands.HandLandmark.RING_FINGER_TIP,
    mp_hands.HandLandmark.PINKY_TIP  
]

def count_raised_fingers(hand_landmarks):
    finger_count = 0
    if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x > hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x:
        finger_count += 1
    for tip in myFingerTips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 1].y:
            finger_count += 1
    return finger_count

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    finger_count = 0
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        finger_count = count_raised_fingers(hand_landmarks)
    
    cv2.putText(img, f'Fingers: {finger_count}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    current_time = time.time()
    
    if finger_count != lastFingerCount and current_time - lastTime >= 1:
        myEngine.say(f"{finger_count} fingers raised")
        myEngine.runAndWait()
        lastFingerCount = finger_count
        lastTime = current_time
    
    cv2.imshow("Finger Counter by Wazingwa. Computer Engineering@CBU", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
