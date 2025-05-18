---
sidebar_position: 1
---

**Last updated by:** lukgvo, **Last updated on:** 10/12/2024


**Last updated by:** lukgvo, **Last updated on:** 10/12/2024


:::info
Document Creation: [5/12/2024]. Last Edited: [10/12/2024]. Authors: [Luk Gvozdenac].


Document Code: [PE-1]. Effective Date: [10/12/2024]. Expiry Date: [10/12/2025].
:::

# Pose Estimation and Matching Project

This project focuses on pose estimation and matching using OpenCV’s DNN (Deep Neural Network) module with a pre-trained TensorFlow model. The primary goal is to detect and classify human poses in images and videos, and to compare the similarity between different poses.

## Summary

### Libraries Used
- `os`
- `cv2` (OpenCV)
- `matplotlib.pyplot`
- `numpy`
- `pandas`
- `time`
- `torch`

### Key Components
1. **YOLO Model Loading**: The YOLO model is loaded using `torch.hub.load`.
2. **Pose Estimation Parameters**: Parameters such as input width, height, and threshold are defined.
3. **Body Parts and Pose Pairs**: Dictionaries and lists defining body parts and their connections.
4. **Image Processing**: Images are read, processed, and displayed using OpenCV and Matplotlib.
5. **Data Collection**: Data such as frame number, processing time, detected keypoints, and confidence scores are collected and saved to a CSV file.
6. **Pose Classification**: Functions to classify poses based on detected keypoints.
7. **Video Processing**: Real-time pose estimation on video feeds using OpenCV.
8. **Pose Matching**: Functions to calculate the similarity between poses in two images.

## Documentation

### Functions

#### `classify_pose(points)`
Classifies the pose based on keypoints.

#### `yolo_pose_estimation(image)`
Performs pose estimation using the YOLO model.

#### `pose_estimation(frame, frame_id)`
Estimates the pose in a given frame and returns the processed frame and pose label.

#### `pose_estimation(frame)`
Estimates the pose in a given frame using OpenCV’s DNN module.

#### `euclidean_distance(point1, point2)`
Calculates the Euclidean distance between two points.

#### `calculate_similarity_percentage(keypoints1, keypoints2, max_distance=200)`
Calculates the similarity percentage between two sets of keypoints.

#### `resize_to_same_height(img1, img2)`
Resizes two images to have the same height.

### Data Collection
Data is collected for each frame and saved to a CSV file for further analysis.

### Real-Time Processing
Real-time pose estimation is performed on video feeds, with the results displayed in real-time.

### Pose Matching
The similarity between poses in two images is calculated and displayed.

## Usage

1. **Image Processing**: Load and process images to estimate poses and classify them.
2. **Video Processing**: Perform real-time pose estimation on video feeds.
3. **Pose Matching**: Compare the similarity between poses in two images.

## Conclusion
This project provides a comprehensive solution for pose estimation and matching using deep learning techniques. It can be applied to various domains such as sports analytics, fitness applications, and human-computer interaction.
