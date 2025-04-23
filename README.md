# Hand Gesture Control for Hill Climb Racing

This project enables hand gesture controls for the **Hill Climb Racing** game using a webcam. It utilizes **OpenCV** and **MediaPipe** to detect hand gestures and simulates key presses using the **keyboard** library. The game is controlled via hand gestures that trigger the "left" (brake) and "right" (gas) buttons, simulating driving actions in the game.

---

## Features

- **Brake**: When no fingers are extended (0 fingers), the "left" key is pressed.
- **Gas**: When all fingers are extended (5 fingers), the "right" key is pressed.
- **Neutral**: Any other number of fingers triggers no key presses, simulating a neutral position.

---

## Installation Guide

Follow these steps to set up and run the project:

### Prerequisites

You need Python 3.x installed along with the following libraries:

- OpenCV
- MediaPipe
- Keyboard

### Setup Steps

1. **Clone the repository**:
   ```bash
   https://github.com/your-username/Hill_Climb_Racing_HandGestureController.git
   ```

2. **Navigate to the project folder**:
   ```bash
   cd Hill_Climb_Racing_HandGestureController
   ```

3. **Install the required dependencies**:
   Run the following command to install all necessary libraries:
   ```bash
   pip install opencv-python mediapipe keyboard
   ```

4. **Run the script**:
   To start the hand gesture control, simply run the Python script:
   ```bash
   python hand_control.py
   ```

   The webcam will open, and hand gestures will be detected. Press 'q' to quit the application.

---

## How It Works

1. The program uses the webcam to capture hand movements in real-time.
2. **Hand gesture detection** is powered by **MediaPipe**, which recognizes the positions of key hand landmarks.
3. Based on the number of fingers extended:
   - **0 fingers** = "Brake" (Simulates the "left" key press)
   - **5 fingers** = "Gas" (Simulates the "right" key press)
   - Any other number = "Neutral" (No key press)

---

## Key Press Simulation

- **Left Arrow Key**: Simulates the brake action (presses "left").
- **Right Arrow Key**: Simulates the gas action (presses "right").

---

## Troubleshooting

- **Webcam not detected**: Ensure your webcam is connected and properly configured.
- **Gesture detection is slow or inaccurate**: Try adjusting the lighting or distance between your hand and the webcam.
- **Application crashes**: Make sure all dependencies are installed correctly.

---

## Notes

- This project was initially created for use with the **Hill Climb Racing** game but can be adapted to control other games or applications that accept keyboard inputs.
- The detection confidence threshold is set to 0.7 for both detection and tracking. You can adjust these values for better accuracy depending on your setup.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to contribute or fork the repository. Pull requests are welcome for bug fixes or improvements.
