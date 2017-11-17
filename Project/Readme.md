## Project

## Parameter Tuning for Comparison of Learners in Ordinal data Classification

### Dataset
Eclipse Bugzilla Bug Reports between 2001-10-10 to 2007-12-14
~ 103k Bug Reports.

Train - Test Split: 80:20

raw and processed datasets present in [data](./data) directory

### Feature Extraction
Temporal Features, Author Features and Product Features generated as per description in Paper. <br />
Each set of features available individually [here](./data/individual_features) <br />

Code to generate all these features present in (features)[./features] folder. <br />
Nomenclature of features same as paper. <br />
Temporal Features - (TMP1 to TMP9) <br />
Author Features - (AUT 1 to AUT3) <br />
Product Features - (PRO1 to PRO11) & Component Features - (PRO12 to PRO22) <br />

#### Text Features
Features from text field `Summary` were generated based on paper. Using Tokenizer and countvectorizer.
Code for the same is available [here](./code/data_preprocessing)

### Original Algorithm
Implementation of DRONE is available [here](./code/DRONE.ipynb) <br />

### Comparison
Results found are as follows: <br />

## Tasks
1. Generate features and save a new CSV file
2. Run RandomForest, NaiveBayes, AdaBoost on the data with updated features
3. Write Differential Evolution code for Hyperparameter Tuning.
4. Do HPT for RF, AdaBoost etc and check how to run.
