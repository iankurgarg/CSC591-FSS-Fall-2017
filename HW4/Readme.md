[Back](../)
# HW 4

## Description

To build a regression tree learner: <br />
<br />
- Apply supervised Discretization
- At each level of the tree, break the data on the ranges and find the column whose breaks most reduces the variability of the target variable (we will use dom).
- For each break, apply the regression tree learner recursively.
- Recursion stops when the breaks do not improve the supervised target score, when there are tooFew examples to break, or when the tree depth is too much.
- Write a list printer that recurses down the tree and prints details about each node, indented by its level in tree.
<br />
Test: run your decision tree learner on auto.csv. Using dom and tooFew is 10, the auto.csv divides into something like this:

## Source Files
All source files are present in ./src/ directory <br />

Sdtree.py - Class for Regression Tree Learner<br />

## Setup
Code has been tested on Python 2.7.12 <br />
If uses files from previous homeworks (1, 2 3)

## Usage
To run the code,

`python src/Sdtree.py data/auto.csv`

Replace the path of the test file as requried <br />
It uses some source files from HW1 and HW2. Those paths have been included wherever required<br />
To ensure that it always runs, please run it from this (/HW4/) directory (using the same command above)<br />

## References

More details about the instructions can be found at [Homeworks](https://txt.github.io/fss17/homeworks)
