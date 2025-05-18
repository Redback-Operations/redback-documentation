---
sidebar_position: 7
---

**Last updated by:** Lachlan, **Last updated on:** 17/12/2024


**Last updated by:** Lachlan, **Last updated on:** 17/12/2024

# Sleep Disorder Prediction

This feature aims to quantify both sleep quality and quantity by measuring motion from sleeping wearers of the IoT device. Sleep quality and monitoring has proven to be significant in recent time for many preventative health care outcomes. For this reason Smartwatches boasting this capability have flooded the market. To capitalize on these capabilities and hopefully provide these benefits to our users, Redback has undertaken predictive modelling of sleep disorders. 

## Data Analytics

> Please fill this out with a walkthrough of your analytics and ML model training workflow

At present the sleep predictor has an accuracy of 73.5% on unseen test data

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




### Dataset
>Talk about Data Preprocessing  

The dataset used for initial training of the model is ICHI14-BORAZIO[^1][^2], collected from 42 subjects aged 28 - 86, wearing high frequency 3d inertial data loggers over 409 hours. 

>I dont have time to make a dataset summary table for this. 

:::info
**Document Creation:** 5 September 2024. **Last Edited:** 5 September 2024. **Authors:** Lachlan Costigan
:::


[^1]:Borazio, Marko & Berlin, Eugen & Kücükyildiz, Nagihan & Scholl, Philipp & Van Laerhoven, Kristof. (2014). Towards Benchmarked Sleep Detection with Inertial Wrist-worn Sensing Units. Proceedings - 2014 IEEE International Conference on Healthcare Informatics, ICHI 2014. 10.1109/ICHI.2014.24.   
[^2]: [Source for the dataset itself](https://www.researchgate.net/publication/305212784_ICHI14-Borazio) 

