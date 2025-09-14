import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

detector = HandDetector(detectionCon=0.5, maxHands=1)

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

while True:
    success, img = cam.read()
    hands, img = detector.findHands(img)

    if hands and hands[0]['type'] == "Right":
        fingers = detector.fingersUp(hands[0])
        totalFingers = fingers.count(1)

        cv2.putText(img, f'Fingers: {totalFingers}', (50, 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        # Reset all keys first
        pyautogui.keyUp('left')
        pyautogui.keyUp('right')
        pyautogui.keyUp('space')

        # Apply action based on finger count
        if totalFingers == 5:
            pyautogui.keyDown('right')
        elif totalFingers == 3:
            pyautogui.keyDown('space')
        elif totalFingers == 2:
            pyautogui.keyDown('left')

    cv2.imshow('Livefeed', img)
    cv2.waitKey(1)
