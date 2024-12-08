    if result.pose_landmarks:
        mp_drawing.draw_landmarks(
            frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS
        )
        
        landmarks = result.pose_landmarks.landmark
        action = classify_pose(landmarks)