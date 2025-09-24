---
sidebar_position: 3
---

# Predictive Modelling of Diabetes 
Diabetes has become a leading cause for concern amongst Australia's population, with over 1.3 Million people confirmed cases and 500,000 more estimated undiagnosed type 2 cases.[^1]

The scale of this issue is compounded by the fact that on average each of these people typically have a family member or carer who's life is directly effected in a support capacity and that diabetes is the 7th leading cause of death of Australians.[^2] 

It is from this perspective that we aim to develop a predictive model for diabetes risk to improve the ability for medical professionals to make timely detections and interventions as well as to give users agency in preventing this disease. 

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
    - [KerasTuner](https://keras.io/keras_tuner/#quick-introduction)


### Dataset 1
https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset  
The original poster is coy[^3] about the source of the data but it is still one of the most popular datasets across Kaggle. 

This Dataset consists of 100001 records which after cleaning, and selction for those aged 55 and over, is reduced to 30995.

The columns are as follows

|Name|Description|Type|  
|-|-|-|
|gender|Gender of the patient|Nominal: [Male, Female, Other]|
|age|Age of the patient|Discrete: [Years, 55 ➡ 80]|
|hypertension|History of hypertension|Nominal: [0: false, 1: true]|
|heart_disease|Patient history of heart disease|Nominal: [0: false, 1: true]|
|smoking_history|Patients Smoking History|Nominal: ['never', 'current', 'No Info', 'former', 'not current', 'ever']|
|bmi|Body-Mass Index: calculated by body-mass / height^2|Continuous|
|HbA1c_level|Average Blood Glucose over the last 3 months|Continuous: [A1c%]|
|blood_glucose_level|Blood glucose at time of recording|Discrete: [mg/dL]|
|diabetes|Whether the patient has been diagnosed with diabetes|Nominal: [0: false, 1: true]|

### Dataset 2
https://archive.ics.uci.edu/dataset/529/early+stage+diabetes+risk+prediction+dataset

This dataset is provided in the UC Irvine ML repo and was collected using questionnaires from the patients of the Syhlet Diabetes Hospital in Bangladesh.[^4]

The Dataset contains 17 columns and 520 records 

|Name|Description|Type|
|-|-|-|
|Age|Age of the patient|Discrete: [Years]|
|Gender|Gender of the patient|Nominal: [Male, Female]|
|Polyuria|Excessive Urine|Nominal: [No, Yes]|
|Polydipsia|Excessive Thirst|Nominal: [No, Yes]|
|Sudden Weight Loss||Nominal: [No, Yes]|
|Weakness||Nominal: [No, Yes]|
|Polyphagia|Extreme Hunger|Nominal: [No, Yes]|
|Genital Thrush||Nominal: [No, Yes]|
|Visual Blurring| |Nominal: [No, Yes]|
|Itching||Nominal: [No, Yes]|
|Irritability||Nominal: [No, Yes]|
|Delayed Healing||Nominal: [No, Yes]|
|Partial Paresis|Muscular weakness / impairment|Nominal: [No, Yes]|
|Muscle Stiffness||Nominal: [No, Yes]|
|Alopecia|Hair Loss|Nominal: [No, Yes]|
|Obesity||Nominal: [No, Yes]|
|Class|Presense of Diabetes|Nominal: [Negative, Positive]|

## Approach
> Please discuss your analytics workflow / methodology here

:::info
**Document Creation:** 5 September 2024. **Last Edited:** 5 September 2024. **Authors:** Claire Van Gils, Lachlan Costigan
:::


[^1]: https://www.diabetesaustralia.com.au/about-diabetes/diabetes-in-australia/
[^2]: https://www.abs.gov.au/statistics/health/causes-death/provisional-mortality-statistics/jan-may-2024
[^3]: https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset/discussion/406676#2282358
[^4]: Islam, M. M. Faniqul et al. “Likelihood Prediction of Diabetes at Early Stage Using Data Mining Techniques.” Computer Vision and Machine Intelligence in Medical Image Analysis (2019): n. pag.

