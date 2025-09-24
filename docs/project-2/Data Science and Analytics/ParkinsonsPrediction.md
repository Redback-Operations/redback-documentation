---
sidebar_position: 6
---
# Parkinson's Disease Prediction Model

This feature has been undertaken to predict the presence of Parkinson's Disease based on the features expressed by patients that can be extracted from the patient's vocal patterns. Parkinson's Disease is a neurodegenerative disorder that has the common symptoms of[^1]:
- Tremors, 
- Bradykinesia (Slowed movemend)
- Stiff or rigid muscles
- Impaired posture, balance
- Impaired automatic movements
- Speech changes
- Dexterity degeneration, particularly noticeable in hand writing 

At present, the cause of Parkinson's is utterly unknown but more data collected about patients as well as early intervention and care may aid to slow the onset. 

## Data Analysis

To analyse this data, as well as to train machine learning classification models, a number of python libraries have been incorporated into the project:
- Data Analytics / Transformation:
    - [Pandas](https://pandas.pydata.org/docs/reference/index.html)
    - [Numpy](https://numpy.org/doc/stable/reference/index.html#reference)
- Visualization:
    - [MatPlotLib](https://matplotlib.org/stable/api/index.html)
    - [Seaborn](https://seaborn.pydata.org/api.html)
- Machine Learning:
    - [Scikit-Learn](https://scikit-learn.org/stable/api/index.html)


### Dataset
The dataset used at this stage is the Oxford Parkinson's Disease Detection Dataset[^2]. This dataset consists of 195 voice recordings of 31 people, 23 of which have been diagnosed with Parkinson's Diseas

The data has the following features:

|Name|Description|type|
|-|-|-|
|Name|An ID denoting a patient|nominal|
|MDVP:Fo| Average Vocal fundamental frequency|Continuous: [Hz]|
|MDVP:Fhi|Max. Vocal fundamental frequency|Continuous: [Hz]|
|MDVP:Flo|Min Vocal fundamental frequency|Continuous:[Hz]|
|MDVP:Jitter|measure of variation in fundamental frequency|Continuous:[%]|
|MDVP:Jitter|measure of variation in fundamental frequency|Continuous:[Absolute Value]|
|MDVP:RAP|measure of variation in fundamental frequency|Continuous|
|MDVP:PPQ|measure of variation in fundamental frequency|Continuous|
|Jitter:DDP|measure of variation in fundamental frequency|Continuous|
|MDVP:Shimmer|measure of variation in amplitude|Continuous|
|MDVP:Shimmer|measure of variation in amplitude|Continuous: [dB]|
|Shimmer:APQ3|measure of variation in amplitude|Continuous|
|Shimmer:APQ5|measure of variation in amplitude|Continuous|
|MDVP:APQ|measure of variation in amplitude|Continuous|
|Shimmer:DDA|measure of variation in amplitude|Continuous|
|NHR|measure of ratio of noise to tonal components in the voice|Continous|
|HNR|measure of ratio of noise to tonal components in the voice|Continuous|
|status|Health status of the subject|Nominal: [1: Parkinson's. 0: No Parkinson's]|
|RPDE|Nonlinear Dynamical Complexity Measure|Continuous|
|DFA|Signal fractal scaling exponent|Continuous|
|spread1|Nonlinear measure of fundamental frequency variation|Continuous|
|spread2|Nonlinear measure of fundamental frequency variation|Continous|
|D2|Nonlinear measure of fundamental frequency variation|Continuous|
|PPE||Continuous|

:::info
**Document Creation:** 5 September 2024. **Last Edited:** 5 September 2024. **Authors:** Lachlan Costigan
:::


[^1]:https://www.mayoclinic.org/diseases-conditions/parkinsons-disease/symptoms-causes/syc-20376055

[^2]:Little, M. (2007). Parkinsons [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C59C74. Accessible from http://archive.ics.uci.edu/dataset/174/parkinsons



