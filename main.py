import cv2
import numpy as np
import os
import uuid
import mediapipe as mp

# Initialize MediaPipe Hands and drawing utilities
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def is_dragging_object(index_x, index_y, object_center, object_radius):
    """
    Check if the index finger is close enough to drag an object.
    """
    distance = ((index_x - object_center[0]) ** 2 + (index_y - object_center[1]) ** 2) ** 0.5
    return distance < object_radius

# Open the default camera
cap = cv2.VideoCapture(0)

# Initialize object positions
circle_center = (300, 300)
circle_radius = 50
triangle_points = [(400, 200), (450, 300), (350, 300)]
rectangle_top_left = (500, 200)
rectangle_width = 100
rectangle_height = 50

# Start MediaPipe Hands
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Preprocess the frame
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # BGR 2 RGB
        image = cv2.flip(image, 1)  # Mirror the frame
        image.flags.writeable = False
        results = hands.process(image)  # Detect hands
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Initialize finger count
        total_fingers_up = 0

        # Process detected hands
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=2, circle_radius=2),
                    mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2)
                )

                # Count raised fingers
                fingers_up = 0
                finger_tips = [8, 12, 16, 20]
                finger_joints = [6, 10, 14, 18]
                for tip, joint in zip(finger_tips, finger_joints):
                    if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[joint].y:
                        fingers_up += 1

                # Detect thumb based on hand orientation
                thumb_tip_x = hand_landmarks.landmark[4].x
                thumb_joint_x = hand_landmarks.landmark[2].x
                wrist_x = hand_landmarks.landmark[0].x
                if (thumb_tip_x < wrist_x and thumb_tip_x < thumb_joint_x) or \
                   (thumb_tip_x > wrist_x and thumb_tip_x > thumb_joint_x):
                    fingers_up += 1

                total_fingers_up += fingers_up

                # Get index finger position
                index_x = int(hand_landmarks.landmark[8].x * image.shape[1])
                index_y = int(hand_landmarks.landmark[8].y * image.shape[0])

                # Drag circle
                if is_dragging_object(index_x, index_y, circle_center, circle_radius):
                    circle_center = (index_x, index_y)

                # Drag triangle
                triangle_center_x = sum([p[0] for p in triangle_points]) // 3
                triangle_center_y = sum([p[1] for p in triangle_points]) // 3
                if is_dragging_object(index_x, index_y, (triangle_center_x, triangle_center_y), 50):
                    dx = index_x - triangle_center_x
                    dy = index_y - triangle_center_y
                    triangle_points = [(x + dx, y + dy) for x, y in triangle_points]

                # Drag rectangle
                rect_center_x = rectangle_top_left[0] + rectangle_width // 2
                rect_center_y = rectangle_top_left[1] + rectangle_height // 2
                if is_dragging_object(index_x, index_y, (rect_center_x, rect_center_y), 50):
                    rectangle_top_left = (index_x - rectangle_width // 2, index_y - rectangle_height // 2)

        # Draw objects
        cv2.circle(image, circle_center, circle_radius, (0, 255, 0), -1)  # Green circle
        cv2.polylines(image, [np.array(triangle_points, np.int32)], isClosed=True, color=(128, 0, 128), thickness=2)  # Purple triangle
        cv2.fillPoly(image, [np.array(triangle_points, np.int32)], color=(128, 0, 128))
        cv2.rectangle(image, rectangle_top_left,
                      (rectangle_top_left[0] + rectangle_width, rectangle_top_left[1] + rectangle_height),
                      (139, 0, 0), -1)  # Dark blue rectangle

        # Display the frame
        cv2.imshow('Hands Tracking', image)

        # Exit on 'q' key
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()

