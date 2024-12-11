import cv2
import mediapipe as mp
import numpy as np


mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils


def classify_pose(landmarks):
    """
    landmarks: Mediapipe Pose landmarks
    동작 인식을 위한 간단한 분류 함수
    """
    if landmarks:
       
        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
        left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
        left_knee = landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]

       
        if left_hip.y > left_shoulder.y and left_hip.y < left_knee.y:
            return "Squat"
        else:
            return "Standing"
    return "Unknown"


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

   
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(frame_rgb)

   
    if result.pose_landmarks:
        mp_drawing.draw_landmarks(
            frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS
        )

       
        landmarks = result.pose_landmarks.landmark
        action = classify_pose(landmarks)

       
        cv2.putText(
            frame,
            f"Action: {action}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )

  
    cv2.imshow("Pose Detection", frame)

  
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
