# Hand Detection and Object Manipulation Project

A real-time computer vision application that uses hand tracking to detect finger gestures and manipulate virtual objects through index finger positioning. The project combines MediaPipe's hand detection capabilities with OpenCV for real-time video processing and interactive object manipulation.

## 🎯 Project Overview

This application captures video from your webcam and uses advanced hand tracking algorithms to:
- Detect and track hand landmarks in real-time
- Count the number of raised fingers
- Enable dragging and manipulation of virtual objects (circle, triangle, rectangle) using index finger positioning
- Provide visual feedback with hand landmark visualization

## 🚀 Features

- **Real-time Hand Detection**: Accurate hand landmark detection using MediaPipe
- **Finger Counting**: Automatic detection of raised fingers including thumb orientation handling
- **Interactive Object Manipulation**: Drag virtual objects using your index finger
- **Multiple Shape Support**: Interact with circles, triangles, and rectangles
- **Visual Feedback**: Hand landmarks and connections are drawn on the video feed
- **Mirror Mode**: Flipped video for natural interaction

## 📚 Libraries and Dependencies

### Core Libraries

1. **OpenCV (cv2)**
   - **Purpose**: Computer vision operations, video capture, image processing, and drawing
   - **Usage**: Webcam access, frame processing, shape drawing, and display
   - **Key Functions**: `VideoCapture()`, `imshow()`, drawing functions

2. **MediaPipe**
   - **Purpose**: Machine learning framework for hand tracking and pose estimation
   - **Usage**: Hand landmark detection and tracking
   - **Components Used**: 
     - `mp.solutions.hands` - Hand detection model
     - `mp.solutions.drawing_utils` - Visualization utilities

3. **NumPy**
   - **Purpose**: Numerical computing and array operations
   - **Usage**: Array manipulations for coordinate calculations and shape definitions
   - **Key Operations**: Array creation, mathematical operations

4. **Standard Libraries**
   - **os**: Operating system interface (imported but not actively used in current version)
   - **uuid**: Unique identifier generation (imported but not actively used in current version)

## 🛠️ Prerequisites

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python Version**: Python 3.7 to 3.10 because Mediapipe does not support newer version of python
- **Webcam**: Built-in or external USB camera
- **RAM**: Minimum 4GB (8GB recommended for smooth performance)
- **Processor**: Multi-core processor recommended for real-time processing

### Hardware Considerations
- **Good Lighting**: Ensure adequate lighting for optimal hand detection
- **Camera Quality**: Higher resolution cameras provide better tracking accuracy
- **Stable Positioning**: Mount or position camera to minimize shake

## 📦 Installation

### Step 1: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv hand_detection_env

# Activate virtual environment
# On Windows:
hand_detection_env\Scripts\activate
# On macOS/Linux:
source hand_detection_env/bin/activate
```

### Step 2: Install Required Packages
```bash
pip install opencv-python==4.8.1.78
pip install mediapipe==0.10.7
pip install numpy==1.24.3
```

### Alternative Installation (using requirements.txt)
Create a `requirements.txt` file with:
```
opencv-python==4.8.1.78
mediapipe==0.10.7
numpy==1.24.3
```

Then install:
```bash
pip install -r requirements.txt
```

## 🎮 Usage

### Running the Application
```bash
python hand_detection.py
```

### Controls and Interactions
- **Exit**: Press 'q' key to quit the application
- **Object Manipulation**: 
  - Position your index finger close to any object to drag it
  - Objects include: green circle, purple triangle, and dark blue rectangle
  - Each object has a detection radius for interaction

### Hand Gestures
- The application automatically counts raised fingers
- Thumb detection adapts to hand orientation (left/right hand)
- All finger positions are tracked and visualized

## ⚙️ Configuration Options

### Adjustable Parameters

#### MediaPipe Settings
```python
# Confidence thresholds (in code)
min_detection_confidence=0.7  # Range: 0.0-1.0
min_tracking_confidence=0.5   # Range: 0.0-1.0
```

#### Object Properties
```python
# Circle
circle_radius = 50            # Adjustable radius
circle_center = (300, 300)    # Initial position

# Triangle
triangle_points = [(400, 200), (450, 300), (350, 300)]  # Vertex coordinates

# Rectangle
rectangle_width = 100         # Width in pixels
rectangle_height = 50         # Height in pixels
```

#### Detection Sensitivity
```python
# Drag detection radius (in is_dragging_object function)
object_radius                 # Proximity threshold for interaction
```

## 🔧 Troubleshooting

### Common Issues and Solutions

1. **Camera Not Detected**
   ```python
   # Try different camera indices
   cap = cv2.VideoCapture(1)  # Instead of 0
   ```

2. **Poor Hand Detection**
   - Ensure good lighting conditions
   - Avoid cluttered backgrounds
   - Keep hands within camera frame
   - Adjust confidence thresholds

3. **Performance Issues**
   - Close other applications using the camera
   - Reduce frame resolution if needed
   - Ensure adequate system resources

4. **Import Errors**
   ```bash
   # Reinstall packages
   pip uninstall opencv-python mediapipe numpy
   pip install opencv-python mediapipe numpy
   ```

## 🎯 Customization Ideas

### Extending the Project
- Add more interactive objects
- Implement gesture-based commands
- Add sound effects for interactions
- Create different interaction modes
- Implement object physics (collision, gravity)
- Add gesture recording and playback
- Integrate with external applications

### Advanced Features
- Multi-hand support
- Gesture recognition for specific commands
- Object creation/deletion through gestures
- Save/load object configurations
- Network multiplayer interactions

## 📝 Technical Considerations

### Performance Optimization
- The application processes frames in real-time, requiring sufficient computational resources
- MediaPipe models are optimized for mobile and desktop deployment
- Frame rate may vary based on hardware capabilities

### Accuracy Considerations
- Hand detection accuracy depends on lighting conditions and background complexity
- Distance from camera affects tracking precision
- Hand orientation and occlusion can impact detection quality

### Privacy and Security
- All processing is done locally on your device
- No data is transmitted or stored externally
- Camera access is only used during application runtime

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new features
- Improving performance
- Fixing bugs
- Enhancing documentation
- Creating tutorials

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter issues or have questions:
1. Check the troubleshooting section
2. Verify all dependencies are correctly installed
3. Ensure your camera is working properly
4. Check MediaPipe and OpenCV documentation for additional guidance

---

**Note**: This project is designed for educational and demonstration purposes. Performance may vary based on hardware specifications and environmental conditions.