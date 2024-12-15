
# Small Object Detection: Football Tracking Project

## Project Overview
Small object detection, particularly for footballs, was a significant challenge in the tracking system due to their small size, rapid movement, and visual similarity to other objects like jerseys or field markings. To address this, the YOLOv8 architecture was enhanced with an additional convolutional head layer to detect objects as small as 4x4 pixels, improving ground-level football detection accuracy. A custom loss function was implemented to penalize misclassified bounding boxes, reducing false positives. SAHI (Slicing Aided Hyper Inference) further enhanced small object detection by focusing on localized regions but introduced latency, limiting real-time applicability. Frame interpolation techniques were also employed to improve detection continuity during rapid movements. These solutions provided robust football detection across diverse scenarios and video qualities.

## Objectives

### Improve Our Models
- Enhance the pose estimation model for sports-specific movements.
- Create a reliable player-tracking model using face detection.
- Optimize small object detection, particularly for tracking footballs in matches.

### Research and Learning
- Study the latest techniques in YOLOv8 and small object tracking.
- Test and train models on new datasets, focusing on improving accuracy in critical areas.

### Efficient Data Storage and Access
- Design a data storage system that is efficient and easy to search.
- Develop a user-friendly interface for quick access to specific information.

### Custom Dataset Creation
- Manually annotated **more than 1000 images** of football matches.
- The dataset is exclusively focused on football detection to ensure a robust and targeted approach for small object detection.

### YOLOv8 Research and Implementation
- YOLOv8 was implemented and evaluated for small object detection.
- Key observations:
  - **High computational requirements** due to YOLOv8’s complexity, affecting real-time applications.
  - **Latency issues**, unsuitable for immediate feedback scenarios.
  - Challenges with **resource-constrained devices**, such as IoT systems.

<div align="center">
<a href="https://youtu.be/c2xUFhsoxuU">YOLOv8 Implementation Demonstration</a>
</div>

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



## Performance Analysis
The performance analysis revealed key insights into the challenges of deploying advanced detection models like YOLOv8 and SAHI in real-world scenarios:

1. **Accuracy vs. Latency Tradeoff**:
   - SAHI significantly improves detection accuracy for small objects like footballs by slicing images into smaller patches. 
   - However, this improvement comes at a steep cost in terms of computational overhead and processing time.

2. **Execution Time Comparison**:
   - YOLOv8 alone processed the dataset in **123.77 seconds**, demonstrating its efficiency for general object detection.
   - When combined with SAHI, the execution time skyrocketed to **613.16 seconds**, representing a fivefold increase.
   - This drastic increase highlights the inefficiency of SAHI for real-time or resource-constrained environments.

3. **Resource Utilization**:
   - The additional computations required for slicing and processing with SAHI heavily taxed available resources.
   - This resulted in higher memory usage, slower response times, and potential bottlenecks on devices with limited hardware capabilities.

4. **Production Feasibility**:
   - Given the significant processing delays, SAHI is not a viable option for production environments, especially for real-time sports analysis or IoT applications where quick feedback is critical.

Future work will focus on optimizing the pipeline to balance accuracy and execution time, possibly exploring alternative methods or hybrid approaches.


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



## Open Issues
- While SAHI improves small object detection accuracy, it significantly increases execution time. 
  - Execution time with YOLOv8 alone: **123.77 seconds**.
  - Execution time with YOLOv8 + SAHI: **613.16 seconds**.
- This fivefold increase in processing time makes SAHI unsuitable for production environments, particularly for real-time applications or scenarios with limited computational resources.
- Further research and optimization are needed to balance accuracy and efficiency.


## Contributors
- **MD Tajish Farhan**
- **Sahil Guglani**



## Example Code

```python
import streamlit as st
import cv2
from sahi.predict import get_sliced_prediction
from sahi.model import Yolov8DetectionModel

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
