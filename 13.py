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
