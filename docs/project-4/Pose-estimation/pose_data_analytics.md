---
sidebar_position: 2
---

:::info
Document Creation: [5/12/2024]. Last Edited: [10/12/2024]. Authors: [Luk Gvozdenac].


Document Code: [PE-2]. Effective Date: [10/12/2024]. Expiry Date: [10/12/2025].
:::

# Pose Estimation and Matching Project

This project focuses on pose estimation Data Analytics and its usecase and application in improving accuracy and keyframe detection. This file is used to visualise data from the pose_estimation_matching.ipynb model and detect weakpoints in the algorithm.

## Summary

### Libraries Used
- `pandas`
- `matplotlib.pyplot`
- `seaborn`

### Key Components
1. **Data Loading**: Loading pose data from CSV files.
2. **Data Visualization**: Plotting processing time, detected keypoints, and confidence scores.
3. **Pairwise Plot**: Visualizing relationships between key metrics.

## Documentation

### Functions

#### `import pandas as pd`
Imports the pandas library for data manipulation and analysis.

#### `import matplotlib.pyplot as plt`
Imports the matplotlib library for creating visualizations.

#### `import seaborn as sns`
Imports the seaborn library for statistical data visualization.

#### `pd.read_csv("pose_data.csv")`
Loads pose data from a CSV file into a DataFrame.

#### `pd.read_csv("video_pose_data.csv")`
Loads video pose data from a CSV file into a DataFrame.

#### `plt.plot(data_df['frame'], data_df['processing_time_ms'])`
Plots the processing time per frame.

#### `plt.plot(data_df['frame'], data_df['detected_keypoints'])`
Plots the number of detected keypoints per frame.

#### `plt.hist(all_confidences, bins=20)`
Creates a histogram for confidence scores distribution.

#### `sns.pairplot(data_df[['frame', 'processing_time_ms', 'detected_keypoints']])`
Creates a pairwise plot of key metrics.

### Data Collection
Data is collected for each frame and saved to a CSV file for further analysis.

### Real-Time Processing
Real-time pose estimation is performed on video feeds, with the results displayed in real-time.

### Pose Matching
The similarity between poses in two images is calculated and displayed.

## Usage

1. **Data Loading**: Load pose data from CSV files.
2. **Data Visualization**: Visualize processing time, detected keypoints, and confidence scores.
3. **Pairwise Plot**: Visualize relationships between key metrics.

## Conclusion
This project focuses on pose estimation Data Analytics and its usecase and application in improving accuracy and keyframe detection. This file is used to visualise data from the pose_estimation_matching.ipynb model and detect weakpoints in the algorithm.

