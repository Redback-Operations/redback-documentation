---
sidebar_position: 2
---
# Predictive modelling of Alzheimer's Disease

Alzheimer's is brutal brain disorder that is one of the leading causes of dementia across our aged community.  
It is incurable and effects quality of life for the patient and their loved ones. Coupled with a demagraphically aging population, this becomes a broader societal concern.  

The aim of this project is to research and develop an advanced predictive model leveraging both existing datasets as well as data captured by the IoT Smartwatch. 

## Data Analytics

We make use of Jupyter Notebooks to conduct and display our work with assisstance from following Python libraries:
- Data Analytics:
    - [Pandas](https://pandas.pydata.org/docs/user_guide/index.html#user-guide), 
    - [Numpy](https://numpy.org/doc/stable/user/index.html#user)
- Data Visualization:
    - [MatplotLib](https://matplotlib.org/stable/users/index.html)
    - [Seaborn](https://seaborn.pydata.org/api.html) 
- Machine learning:
    - [scikit-Learn](https://scikit-learn.org/stable/user_guide.html)

The dataset in use for classification training at this stage is the [Open Access Series of Imaging Studies (OASIS)](https://sites.wustl.edu/oasisbrains/) released on [Kaggle](https://www.kaggle.com/datasets/jboysen/mri-and-alzheimers/data) by the Washington University Alzheimer's Disease Research center, the Neuroinformatics Research group at Washington University School of medicine, the Biomedical Informatics Research Network and Dr Randy Buckner of the Howard Hughes Medical Institute.[^1]

The Dataset (n=373) consists of the following columns:  


|Column Name| Description| Type|
|-|-|-|
|Subject ID | Unique identifier for each subject of the study.|Nominal|
|MRI IR| Unique identifier for each MRI scan.|Nominal|
|Group| Classification of the subject|Nominal: [Nondemented , Demented , Converted]|
|Visit| n-th visit of the patient|Discrete|
|MR Delay|Time between the occurence of this scan and the last| Discrete|
|M/F|Gender of the subject|Nominal: [M: Male , F: Female]|
|Hand|Dominant hand of the subject |Nominal: [R: Right Handed, L: Left Handed]|
|Age|Age of the subject at time of visit| Discrete: [years: 60 - 96]|
|EDUC|Years of formal schooling|Discrete: [years]|
|SES|An index of socioeconomic status[^2] expanded to 5 factors| Ordinal:  [1: Highest ➡ 5: Lowest] |
|MMSE|Mini Mental State Examination Score[^3]|Ordinal: [30: Best ➡ 0: Worst]|
|CDR|Clinical Dementia Rating[^4]|Ordinal: [0: None, 0.5: Very Mild, 1: Mild, 2:Moderate]|
|eTIV|Estimated total intracranial volume[^5]|Continuous: [cm^3]|
|ASF|Atlas Scaling Factor - Automated Normalisation of head size / brain analysis[^5]|Continuous [unitless]|
|nWBV|Normalized Whole Brain Volume (percent of voxels in masked image labeled as grey / white matter)[^6].|Discrete: [0%-100%]|

## Approach

>Please discuss the logic behind your workflow here


:::info
**Document Creation:** 5 September 2024. **Last Edited:** 5 September 2024. **Authors:** Lachlan Costigan
:::


[^1]: Open Access Series of Imaging Studies (OASIS): Longitudinal MRI Data in Nondemented and Demented Older Adults. Marcus, DS, Fotenos, AF, Csernansky, JG, Morris, JC, Buckner, RL, 2010. Journal of Cognitive Neuroscience, 22, 2677-2684. doi: 10.1162/jocn.2009.21407

[^2]: Hollingshead, A. (1957). Two factor index of social position. New Haven, CT: Yale University Press.

[^3]: Folstein MF, Folstein SE, McHugh PR. "Mini-mental state". A practical method for grading the cognitive state of patients for the clinician. J Psychiatr Res. 1975 Nov;12(3):189-98. doi: 10.1016/0022-3956(75)90026-6. PMID: 1202204.

[^4]: Morris JC. The Clinical Dementia Rating (CDR): current version and scoring rules. Neurology. 1993 Nov;43(11):2412-4. doi: 10.1212/wnl.43.11.2412-a. PMID: 8232972.

[^5]: Buckner RL, Head D, Parker J, Fotenos AF, Marcus D, Morris JC, Snyder AZ. A unified approach for morphometric and functional data analysis in young, old, and demented adults using automated atlas-based head size normalization: reliability and validation against manual measurement of total intracranial volume. Neuroimage. 2004 Oct;23(2):724-38. doi: 10.1016/j.neuroimage.2004.06.018. PMID: 15488422.

[^6]: Fotenos AF, Snyder AZ, Girton LE, Morris JC, Buckner RL. Normative estimates of cross-sectional and longitudinal brain volume decline in aging and AD. Neurology. 2005 Mar 22;64(6):1032-9. doi: 10.1212/01.WNL.0000154530.72969.11. PMID: 15781822.
