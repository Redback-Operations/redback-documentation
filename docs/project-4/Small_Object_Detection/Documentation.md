
# Small Object Detection: Football Tracking Project

## Project Overview
This project focuses on detecting footballs in match videos using state-of-the-art object detection techniques tailored for small objects. Key achievements include dataset creation, model training and modification, and deployment for visual performance analysis.

---

## Completed Deliveries

### Custom Dataset Creation
- Manually annotated **more than 1000 images** of football matches.
- The dataset is exclusively focused on football detection to ensure a robust and targeted approach for small object detection.

### YOLOv8 Research and Implementation
- YOLOv8 was implemented and evaluated for small object detection.
- Key observations:
  - **High computational requirements** due to YOLOv8’s complexity, affecting real-time applications.
  - **Latency issues**, unsuitable for immediate feedback scenarios.
  - Challenges with **resource-constrained devices**, such as IoT systems.

[YOLOv8 Implementation Demonstration](https://youtu.be/c2xUFhsoxuU)

### SAHI Integration
- Integrated **SAHI (Slicing Aided Hyper Inference)** with a patch size of 960x540.
- Improved detection accuracy for small objects but introduced delays, limiting production feasibility.

### Custom Loss Function
- Developed a custom loss function to penalize misclassified bounding boxes.
- Reduced false positives (e.g., white jerseys misidentified as footballs).

```python
# Example of the deviation penalty in the custom loss function
deviation_penalty = 0.7
```

### YOLOv8 Architecture Modification
- Added an extra **convolutional head layer** (kernel size 3x3) to detect objects as small as 4x4 pixels.
- Enhanced detection accuracy for surface-level footballs.

### Video Frame Interpolation
- Applied interpolation techniques to address missing frames.
- Improved detection continuity and accuracy in video sequences.

### Deployment and Visualization
- Deployed an interactive application using **Streamlit** to visually showcase the model’s performance.
- Users can input real-time data and view detection results through a visual interface.

---

## Performance Analysis
- SAHI integration improves detection accuracy but introduces delays, raising concerns for real-time deployment.

---

## How to Use

### Requirements
- Python 3.8+
- Required libraries: `torch`, `opencv-python`, `streamlit`, `sahi`, `numpy`, `matplotlib`.

### Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/small-object-detection.git
   cd small-object-detection
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

4. **View Results**:
   - Upload a video or image of a football match to see the detection results.

---

## Open Issues
- SAHI integration causes processing delays.
- Further optimization is needed for real-time performance.

---

## Contributors
- **MD Tajish Farhan**

---

## Example Code

```python
import streamlit as st
import cv2
from sahi.predict import get_sliced_prediction
from sahi.model import Yolov5DetectionModel

# Streamlit App Configuration
st.title("Small Object Detection: Football Tracking")
st.write("Upload an image or video to detect footballs.")

# Upload File
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "mp4"])

# Load YOLOv8 Model
model_path = "path_to_yolov8_model.pt"
detection_model = Yolov5DetectionModel(
    model_path=model_path,
    confidence_threshold=0.4,
    device="cpu",  # Change to 'cuda' if GPU is available
)

if uploaded_file is not None:
    # Check file type
    if uploaded_file.name.endswith(("jpg", "jpeg", "png")):
        # Image Processing
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Object Detection
        result = get_sliced_prediction(
            image, detection_model, slice_height=540, slice_width=960
        )
        st.image(result.image, caption="Detection Result", use_column_width=True)

    elif uploaded_file.name.endswith("mp4"):
        # Video Processing (Example: Placeholder for actual implementation)
        st.video(uploaded_file)
        st.write("Video detection functionality coming soon!")

    else:
        st.error("Unsupported file format.")

st.write("Powered by YOLOv8 and SAHI.")
```
