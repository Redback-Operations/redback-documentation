---
sidebar_position: 5
---
# Heart Attack Prediction

This feature has been built with the intention of providing an early warning for Heart disease based on indicators collected by the wearable's sensor array. This feature seeks to provide users and their support network an alert to worrying decreases in cardiovascular health.

## Data Analytics

To analyse this data, as well as to train machine learning classification models, a number of python libraries have been incorporated into the project:

- Data Analytics / Transformation:
    - [Pandas](https://pandas.pydata.org/docs/reference/index.html)
    - [Numpy](https://numpy.org/doc/stable/reference/index.html#reference)
- Visualization:
    - [MatPlotLib](https://matplotlib.org/stable/api/index.html)
    - [Seaborn](https://seaborn.pydata.org/api.html)
- Machine Learning:
    - [Scikit-Learn](https://scikit-learn.org/stable/api/index.html)
    - [Tensorflow](https://www.tensorflow.org/api_docs/python/tf) / [Keras](https://keras.io/api/)
    - [LightGBM](https://lightgbm.readthedocs.io/en/stable/)
    - [XGBoost](https://xgboost.readthedocs.io/en/stable/)
    - [imblearn](https://imbalanced-learn.org/stable/references/index.html#api)


### Dataset 1
The dataset used in heart_attack_prediction.ipynb is the Heart Attack Risk Prediction Dataset synthesized by Sourav Banerjee with the assistance of ChatGPT[^1]


|Name|Description|Type|  
|-|-|-|
|Patient ID||Nominal|
|Age||Discrete: [years]|
|Sex||Nominal: [Male, Female]|
|Cholestrol| Total Cholestrol measured| Discrete: [mg/dL]|
|Blood Pressure| 2 Values showing the pressure over the heart beating and the heart relaxing| Discrete: [Systotic/Diastolic (mm Hg)]|
|Heart Rate| | Discrete: [beats per minute]
|Diabetes| Presence of diabetes in the patient| Nominal: [1: Yes, 0: No]|
|Family History||Nominal: [1: Yes, 0: No]|
|Smoking||Nominal: [1: Yes, 0: No]|
|Obesity||Nominal: [1: Yes, 0: No]|
|Alcohol Consumption||Nominal: [1: Yes, 0: No]|
|Hours of Exercise per Week||Continuous|
|Diet||Ordinal: [ Healthy, Average, Unhealth]|
|Previous Heart Problems||Nominal: [1: Yes, 0: No]|
|Medication Use||Nominal: [1: Yes, 0: No]|
|Stress Level|Self-reported level of stress|Ordinal: [1 ➡ 10]
|Sedentry Hours|Per Day|Continuous|
|Income| Annual income| Continuous|
|BMI|Body-Mass Index: calculated by body-mass / height^2|Continuous|
|Triglycerides|| Continuous: [mg/dL]|
|Physical Activity Days Per Week||Continous|
|Sleep Hours Per Day||Continous|
|Heart Attack Risk||Continuous: [0➡1]




### Dataset 2
>Please cite the sources of this dataset. I tried my damndest but couldnt find it  

The dataset used in the Heart_Disease_Prediction.ipynb notebook:

[^1]:https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset/data 
