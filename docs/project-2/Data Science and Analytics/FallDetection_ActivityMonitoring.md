---
sidebar_position: 4
---

**Last updated by:** Lachlan, **Last updated on:** 17/12/2024


**Last updated by:** Lachlan, **Last updated on:** 17/12/2024


# Fall detection feature for Elderly Care Wearable

The aim of this feature is to implement functionality to detect and promptly alert care providers to falls. This feature also seeks to detect abnormal locomotion (i.e limping) to provide early warning to care providers for potential intervention.

## Implementation
At present, we are able to detect a fall using the devices, accelerometer and gyroscoper.  
We're presently working towards Activity Monitoring and Automated alerts to relevant parties


### Assumptions
1. The fall detection model can be generalised for the elderly.
2. The model can generalize to detect falls in elderly individuals outside specified height ranges.
3. Readings taken with the sensor positioned around the wrist are assumed to be comparable to those taken around the chest.

### Future Considerations
- Explore advanced AI algorithms to enhance fall detection accuracy.
- Implement proactive health monitoring features to detect early signs of potential health issues beyond falls.
- Incorporate intuitive user interfaces based on ongoing user feedback to optimize usability.
- Acquire a larger dataset, retrain the model, and conducting hyperparameter tuning to attain optimal performance in fall detection.
- Collaborate with the Software and App Development and Backend Development teams to incorporate the feature to the wearable device.

### How to run the project on Local Machine
To run the project on a local machine, follow these steps:

1. Clone the repository from GitHub
2. Navigate to the ```Fall detection``` directory
3. Install the required dependencies using ```pip install -r docs/requirements.txt```
4. To run the project, run the ```fall_detection.ipynb``` file
5. To retrain the model with a different dataset, add the dataset into the ```/data``` directory. The trained models are stored in the ```/models``` directory

### Implementation details

This feature makes use of the following Python Libraries:
- Data Analytics / Transformation:
    - [Pandas](https://pandas.pydata.org/docs/reference/index.html)
    - [Numpy](https://numpy.org/doc/stable/reference/index.html#reference)
- Visualization:
    - [MatPlotLib](https://matplotlib.org/stable/api/index.html)
- Machine Learning:
    - [Scikit-Learn](https://scikit-learn.org/stable/api/index.html)
    - [Tensorflow](https://www.tensorflow.org/api_docs/python/tf) / [Keras](https://keras.io/api/)

Models were trained using captured sensor data from the 1st wearable prototype

>Please fill in with technical details of implementation 

:::info
**Document Creation:** 5 September 2024. **Last Edited:** 5 September 2024. **Authors:** Lachlan Costigan
:::
