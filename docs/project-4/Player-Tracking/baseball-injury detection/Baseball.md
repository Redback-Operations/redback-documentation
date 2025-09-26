# Baseball Injury Risk Analysis — Project Documentation

## Table of Contents
- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Project Objectives](#project-objectives)
- [Technology Stack and Rationale](#technology-stack-and-rationale)
- [System Architecture](#system-architecture)
- [Dataset Development](#dataset-development)
- [Model Training](#model-training)
- [Challenges and Limitations](#challenges-and-limitations)
- [Key Features](#key-features)
- [Future Work](#future-work)
- [Conclusion](#conclusion)

---

## Introduction

The **Baseball Injury Risk Assessment** project provides an intelligent system to analyze baseball player movements from video footage and assess injury risk. Using computer vision and machine learning, it detects risk-prone joint movements and outputs visual feedback with pose overlays and injury predictions.

## Problem Statement

Athletes in baseball face frequent injury risks due to repetitive motions. Traditional analysis methods are manual, subjective, and slow. This project introduces an automated, objective tool to classify movement risk levels from video data.

## Project Objectives

- Extract pose landmarks using MediaPipe.
- Compute key joint angles (shoulder, elbow, knee).
- Train a model to classify movement risk.
- Overlay risk labels and visual feedback on video.
- Build a Streamlit-based web interface for users.

## Technology Stack and Rationale

- **Pose Estimation**: MediaPipe — fast, efficient, and real-time.
- **Model Training**: TensorFlow (Keras) — flexible and browser-friendly.
- **Frontend**: Streamlit — lightweight, Python-native UI framework.
- **Backend**: OpenCV — handles video processing and frame annotations.

## System Architecture

### Main Scripts
- `main.py`: End-to-end processing (video → prediction → overlay).
- `streamlit_app.py`: Web interface, handles upload and display.

### Utility Scripts
- `utils/angles.py`: Calculates joint angles via cosine rule.
- `utils/draw_overlay.py`: Draws skeletons, angles, and risk labels.
- `model/predictor.py`: Loads the trained model and makes predictions.
- `model/trainer.py`: Trains a classifier using joint angle data.
- `config.py`: Central settings for paths, constants, and configs.
- `dataset/label_mapper.py`: Converts string labels to numeric and vice versa.

## Dataset Development

The dataset consists of joint angle data extracted from 4 baseball videos:

- **High-risk pitchers**: Drew Storen, Max Scherzer (shoulder/elbow risk).
- **Low-risk batters**: George Springer, Luis Arraez (safe movement).

Landmarks → Joint angles → CSV format:  
`[left_elbow, right_elbow, left_shoulder, right_shoulder, left_knee, right_knee, label]`

## Model Training

- **Model type**: Feedforward Neural Network
- **Input**: 6 joint angles
- **Output**: Risk class (`safe`, `shoulder risk`, `elbow risk`)
- **Architecture**:
  - Input layer: 6 units
  - Hidden layer: 64 units, ReLU
  - Output layer: softmax over 3 classes

Trained using Adam optimizer and categorical crossentropy. Saved as `.h5` for runtime prediction.

## Challenges and Limitations

- **Pose Estimation Errors**: MediaPipe struggles with blur/occlusion.
- **Small Dataset**: Only 4 videos — potential overfitting.
- **Deployment Constraints**: Memory and time limits in hosting platforms.
- **Label Noise**: Labels applied at video level, not frame-specific.

## Key Features

- **Video-Based Risk Assessment**: Annotated pose + risk feedback
- **Web Interface**:
  - Upload videos
  - View progress with spinner
  - Download risk-annotated output

- **Modular Design**:
  - Replaceable pose or classification modules
  - Easily extendable to other sports

## Future Work

- Real-time webcam-based risk detection.
- Larger, diverse datasets for robust training.
- Frame-level joint-specific risk localization.
- Expand to other sports like cricket, tennis, football.

## Conclusion

This capstone delivers a complete ML pipeline for video-based injury risk assessment in baseball. It demonstrates practical integration of computer vision, web development, and machine learning to solve real-world biomechanical problems in sports.

