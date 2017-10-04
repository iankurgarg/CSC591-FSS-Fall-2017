[Back](../)
# HW 3

## Description

#### Unsupervised Discretization: 
Write code that takes a table column of N numbers, sorts in, and breaks into bins of size approximately sqrt(N). Note that these breaks have to satisfy the following sanity rules: <br />

- no range contains too few numbers (sqrt(N));
- each range is different to the next one by some epsilon value (0.2 * standard deviation of that column);
- the span of the range (hi - lo) is greater than that epsilon;
- the lo value of one range is greater than than the hi value of the previous range

#### Supervised Discretization: 
Write code that reflects over the ranges found by the unsupervised discretizer. Combine ranges where some dependent variable is not changed across that combination of ranges. Specifically, sort the ranges and do a recursive descent of the ranges. At each level of the recursion, break the ranges at the point that most minimizes the expected value of the standard deviation of the dependent variable.<br />

## Source Files
All source files are present in ./src/ directory <br />

Discretize.py - Main Class for testing <br />
Random.py - Class for Random number generator <br />
Range.py - Class used for Unsupervised discretization <br />
RangeManager.py - Class for Unsupervised discretization  <br />
Sample.py - Class to Sample of data for ranges <br />
SuperRange.py - Class for Supervised discretization  <br />

## Setup
Code has been tested on Python 2.7.12 <br />
It uses these libraries: (`os, sys, argparse, abc, numpy, math, random, copy`)

## Usage
To run the code,

`python src/Discretize.py`

It uses some source files from HW1 and HW2. Those paths have been included wherever required<br />
To ensure that it always runs, please run it from this (/HW3/) directory (using the same command above)<br />

## Input Data
It generates random data each time and then tries to discretize it. <br />
It generates 50 data points using the `Random` Class. <br />
Each of those numbers is mapped to a `y` value, which is calculated using `klass` function defined in `Discretize.py` It assigns one of three values (plus a random componenet) based on the `x` value.<br />

## Output
The first part of the output prints discretized ranges created using just the `x` values.<br />
The second part of the output prints supervised discretization ranges which are calcualted using the `y` values as well. <br />
It is observed that the number of supervised ranges are lesser as compared to number of unsupervised ranges.<br />


## References

More details about the instructions can be found at [Homeworks](https://txt.github.io/fss17/homeworks)
