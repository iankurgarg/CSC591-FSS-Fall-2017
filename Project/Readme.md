## Project

## Parameter Tuning for Comparison of Learners in Ordinal Data Classification

### Original Reference Paper
DRONE: Predicting Priority of Reported Bugs by Multi-factor Analysis <br />
http://ieeexplore.ieee.org/document/6676891/

### Dataset
Eclipse Bugzilla Bug Reports between 2001-10-10 to 2007-12-14 <br />
~ 103k Bug Reports. <br />

Train - Test Split: 80:20 <br />

raw and processed datasets present in [Data](./Data) directory <br />

### Feature Extraction
Temporal Features, Author Features and Product Features generated as per description in Paper. <br />
Each set of features available individually [here](./Data/individual_features) <br />

Code to generate all these features present in (features)[./features] folder. <br />
Nomenclature of features same as paper. <br />
Temporal Features - (TMP1 to TMP9) <br />
Author Features - (AUT 1 to AUT3) <br />
Product Features - (PRO1 to PRO11) & Component Features - (PRO12 to PRO22) <br />

#### Text Features
Features from text field `Summary` were generated based on paper. Using Tokenizer and countvectorizer.
Code for the same is available [here](./Code/data_preprocessing)

### Original Algorithm
Implementation of DRONE is available [here](./Code/DRONE.ipynb) <br />

### Presentation
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRdtyMwFkwkVga6Zxa3KkuliTJdIu_qR9VK6P1sTyLTBS2ix6oZoc0f96Tw81uzFoplEenYqwe1GRZ0/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Steps to Reproduce
We provide the raw dataset as well as the processed dataset [here](./Data). <br/>
<u>Disclaimer</u>: Datasets have been sourced from [Eclipse Bugzilla](https://bugs.eclipse.org/bugs). It is available under Terms and conditions specified on the Eclipse Bugzilla Webpage. Refer [this](http://www.eclipse.org/legal/termsofuse.php) for any queries related to license for use or distribution of the dataset. <br /> <br /> 
In case you would like to process the features again, the Code with instructions for the same is present [here](./Code/FeatureGeneration). <br /><br /> 
Once the these features are generated, we need to generate count vector for `summary` column. For this we have [DataPreprocessing.py](./Code/DataPreprocessing.py) which can be imported and used to preprocess training and testing Data (using fit() and transform() methods). <br /><br /> 
Finally, Code for running Differential Evolution is present [here](./Code/ParameterTuningDE.ipynb). <br /><br /> 

Implementation of the original DRONE algorithm is also available [here](./Code/DRONE.ipynb). <br />

## Report
Detailed report with results can be found [here](./Report/Report_Group_I.pdf)


