import cv2
import numpy as np


def enhance_frame(frame, alpha, beta):
    # Enhance the frame by adjusting brightness and contrast
    enhanced_frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
    return enhanced_frame


def main():
    # Open the default camera (usually the laptop's built-in camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    alpha = 2  # Contrast control (1.0-3.0)
    beta = 10  # Brightness control (0-100)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Get the enhanced frame
        enhanced_frame = enhance_frame(frame, alpha, beta)

        # Display the original frame
        cv2.imshow('Original Video', frame)

        # Display the enhanced frame
        cv2.imshow('Enhanced Video', enhanced_frame)

        # Exit condition: press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
