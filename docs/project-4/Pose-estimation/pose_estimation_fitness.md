---
sidebar_position: 3
---

:::info
Document Creation: [09/05/2025]. Last Edited: [09/05/2025]. Authors: [Luk Gvozdenac].

Document Code: [PE-1]. Effective Date: [09/05/2025]. Expiry Date: [09/05/2026].
:::

## Code Location : Redback-Operations/redback-orion/tree/main/Player_Tracking/Pose_Matching_project/Pose_Estimation/pose-estimation-fitness

# Pose Estimation Fitness Project

This project focuses on pose estimation and strain analysis for fitness applications using a pre-trained Keypoint R-CNN model. The primary goal is to detect keypoints, evaluate exercise form, and visualize strain metrics.

## Summary

### Libraries Used
- `os`
- `cv2` (OpenCV)
- `matplotlib.pyplot`
- `numpy`
- `torch`
- `csv`

### Key Components
1. **Pose Estimation Model**: Uses a pre-trained Keypoint R-CNN model from `torchvision`.
2. **Strain Analysis**: Calculates strain metrics for specific exercises (e.g., deadlift, bench press, squat).
3. **Visualization**: Draws poses and highlights areas of high strain.
4. **CSV Handling**: Saves and loads strain results to/from CSV files.
5. **Best/Worst Form Analysis**: Identifies and displays the best and worst exercise forms based on strain metrics.
6. **Graphical Output**: Generates strain metric graphs for visualization.

## Documentation

### Functions

#### `load_pose_model(device='cpu')`
Loads the pre-trained Keypoint R-CNN model.

#### `pose_estimation(image, model, device='cpu')`
Performs pose estimation on an image.

#### `draw_pose(image, keypoints, strain_results=None, threshold=0.5)`
Draws poses on an image and highlights areas of high strain.

#### `calculate_strain(keypoints, exercise_type)`
Calculates strain metrics based on keypoints and exercise type.

#### `save_strain_results_to_csv(strain_results, csv_path)`
Saves strain results to a CSV file.

#### `load_strain_results_from_csv(csv_path)`
Loads strain results from a CSV file.

#### `evaluate_images(data_dir, model, device, exercise_type)`
Evaluates all images in a directory and identifies the best form.

#### `display_best_and_worst_images_with_strain(data_dir, model, device, exercise_type)`
Displays the best and worst exercise forms with corresponding strain graphs.

## Usage

1. **Setup**: Install dependencies and prepare the `dataDeadlift` directory with exercise images.
2. **Run**: Execute the main script to analyze exercise form.
3. **Visualization**: View poses, strain metrics, and graphs for each image.
4. **Analysis**: Identify the best and worst exercise forms based on strain metrics.

## Conclusion
This project provides a comprehensive solution for pose estimation and strain analysis in fitness applications. It can be applied to sports analytics, personal training, and rehabilitation.

