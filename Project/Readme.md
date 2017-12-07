## Project

## Parameter Tuning for Comparison of Learners in Ordinal data Classification

### Original Reference Paper
DRONE: Predicting Priority of Reported Bugs by Multi-factor Analysis <br />
http://ieeexplore.ieee.org/document/6676891/

### Dataset
Eclipse Bugzilla Bug Reports between 2001-10-10 to 2007-12-14 <br />
~ 103k Bug Reports. <br />

Train - Test Split: 80:20 <br />

raw and processed datasets present in [data](./data) directory <br />

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

### Presentation
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRdtyMwFkwkVga6Zxa3KkuliTJdIu_qR9VK6P1sTyLTBS2ix6oZoc0f96Tw81uzFoplEenYqwe1GRZ0/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

### Comparison
Results found are as follows: <br />

## Report
1. Abstract & Introduction -- Clear problem definition in two sentences.
2. Related Work & Critique
  - Explain DRONE and the methodology briefly
  - clearly state the "problems" with the paper
4. Dataset & Evalution Criteria 
  - Eclipse
  - Feature engineering
  - Evaluation on average F1, Average Precision, Average Recall
5. Methodology
  - Diagram of training and testing with CV (from PPT)
  - Setting (we are compariing our results based on f1 score.. with drone)
  - Tuning Algorithm (About DE)
  - We tune for different objectives
  - Improvements to original Algorithm --- Not sure about this
6. Experiments & Results
  - Research Questions
  - Experimnent 1: 
    - The goal of this experiment is tuning based on Average F1 score.
    - Our results with graphs,
    - Stats, box plot
    - Model stability
    - Choosen one
    - Final comparison Table (Best, DRONE)
  - Experiment 2: Precision
  - Experiment 3: Recall
  - Misc.. (DRONE V2)
7. Conlusions (Analysis of results in terms of research questions)
8. Future Work (Prorpose some stuff)


## Tasks
1. Generate features and save a new CSV file
2. Run RandomForest, NaiveBayes, AdaBoost on the data with updated features
3. Write Differential Evolution code for Hyperparameter Tuning.
4. Do HPT for RF, AdaBoost etc and check how to run.
