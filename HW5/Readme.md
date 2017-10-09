[Back](../)
# HW 5 - Not Completed

## Description

Our contrast learner will examine each pair of nodes in the decision tree and report the delta and effect between each node in a pair <br />
<br />
The delta is the difference in the branch path between each node<br />
The effect is the mean difference in the performance score those nodes<br />
Note that if the delta is:<br />
<br />
positive then the contrast is a plan (something to do).<br />
negative then the contrast is a monitor (something to watch for).<br />
Note also that is statistically there is no difference between the population of instances in each node, then there is no point printing that contrast. For code to conduct those statistical tests, see same in num.<br />
<br />
Test: Using auto.csv, print the plans and monitors separately. Note that for the leaves with best scores, there should be no plans generated. Similarly, for the leaves with worst scores, there should be monitors generated.<br />

## Source Files
All source files are present in ./src/ directory <br />

Contrasts.py<br />

## Setup
Code has been tested on Python 2.7.12 <br />
If uses files from previous homeworks (1, 2, 3, 4)

## Usage
To run the code,

`python src/Contrasts.py data/auto.csv`

Replace the path of the test file as requried <br />
It uses some source files from HW1, HW2, HW3 and HW4. Those paths have been included wherever required<br />
To ensure that it always runs, please run it from this (/HW5/) directory (using the same command above)<br />

## References

More details about the instructions can be found at [Homeworks](https://txt.github.io/fss17/homeworks)
