# Greyhound Detection and Tracking Project
![readme style: standard](https://img.shields.io/badge/readme%20style-standard-brightgreen)
![Roboflow](https://img.shields.io/badge/Roboflow-Model%20Status-blue)
![Python](https://img.shields.io/badge/Python-3.12-blue)

## Overview
This project focuses on detecting and tracking greyhounds in races. Using YOLOv8 for object detection and tracking, the system highlights all the dogs in each video frame by putting a bounding box around them or identifying their number. Additionally, it calculates their relative speeds.

### Watch the Project in Action
- [Watch the video demonstration of greyhound detection](https://deakin365-my.sharepoint.com/:v:/g/personal/s222182857_deakin_edu_au/Ec6OtwCsxdtInGLccCf3-BMBsgsL47J3IEAnwrbzqUd-jw?e=Avsg1g&nav=eyJwbGF5YmFja09wdGlvbnMiOnt9LCJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJUZWFtcyIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJwb3N0cm9sbC1jb3B5bGluayIsInJlZmVycmFsUGxheWJhY2tTZXNzaW9uSWQiOiIwNzFhZTJhZi0xMWFmLTQzMjEtODY5Ny0yY2E4MDAzYzZlZjkifX0%3D)
- [View our project on Roboflow](https://universe.roboflow.com/greyhound-tracking-ioamr/australian-greyhound-racing)
- [Relative speed of greyhounds](https://github.com/rissicay/redback-orion/blob/main/greyhound_tracking/notebooks/speed_test.ipynb)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
- [Dataset](#dataset)
- [Challenges Faced](#challenges-faced)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [Contributors](#contributors)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features
- **Greyhound Detection:** Accurately detects and identifies all greyhounds in each video frame.
- **Tracking and Sorting:** Tracks the positions of the greyhounds throughout the race.
- **Bounding Boxes:** Draws consistent bounding boxes around detected greyhounds.
- **Speed Calculation:** Calculates the relative speed of each greyhound in the race, though further refinement is needed.
- **Custom Dataset:** Created and labeled a large custom dataset using Roboflow, with tasks distributed among team members for efficient data labeling.

## Installation

### Prerequisites
- NumPy
- Matplotlib
- Ultralytics
- OpenCV
- Keras
- Graphviz
- Pydot

### Steps
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/rissicay/redback-orion
    ```
2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Download the Dataset:**
    - Use the [Roboflow dataset link](https://app.roboflow.com/ds/TYmihJNfyP?key=D4ylby1lBR) to download the training data.
4. **Setup YOLOv8:**
    - Follow the [YOLOv8 installation guide](https://docs.ultralytics.com/models/yolov8/) to set up the detection model.

## Dataset
The dataset used for training the model includes a large collection of images of greyhounds, labeled and annotated using Roboflow. The dataset was created by the team, with tasks distributed among members to efficiently label each image, ensuring a high-quality dataset to improve the model's performance.

## Challenges Faced
- **Close Proximity Detection:** Initial challenges included difficulties in detecting greyhounds when they were close together. This was mitigated by expanding the dataset and refining the model.
- **Obstruction Issues:** Detecting greyhounds behind railings or other obstacles required additional training data and fine-tuning of the model.
- **Speed Calculation:** The speed feature was added to the system, but it requires further refinement to ensure accurate measurements.
- **Dataset Management:** Creating and labeling a large dataset involved coordination among team members to ensure consistency and accuracy.

## Future Work
- **Further Model Refinement:** Continue refining the model to enhance accuracy and robustness.
- **Speed Feature Improvement:** Improve the speed calculation feature for more accurate real-time tracking.
- **Automated Testing Pipeline:** Implement an automated testing pipeline to validate the model against new datasets.
- **Extended Features:** Explore adding features such as live commentaries.

## Contributing
Contributions are welcome! Please follow the standard contribution guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Contributors :sparkles:
- [*Harsh Bhanot*](https://github.com/HarshBhanot7)
- [*Mohitpreet Sing*](https://github.com/plasma141)
- [*Chris Abbey*](https://github.com/rissicay)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
We would like to extend our gratitude to the following:

- **YOLOv8 and Ultralytics Communities:** Thank you for your contributions to the field of object detection and tracking. Your work has been instrumental in the development of our project.
- **Roboflow:** Special thanks for providing platform and annotation tools that have significantly contributed to the accuracy and efficiency of our model.
