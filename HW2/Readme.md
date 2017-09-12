## Code for HW 2

## Description

Read lines from CSV files one a time incrementally updating column headers for each line. <br />
Headers are either Nums or Syms as determined by the magic characters in row1. <br />
Num and Syms incremental maintain knowledge about mean, standard deviation, and symbol counts in a column. <br/ >
So when the table reads row1, it builds the headers of Nums and Syms. And when the other rows are read, the headers get updated.<br /> <br />
Code up the domination counter (the dom function in Tbl which also uses dominate and dominate1 in Row<br />
<br />
Test: Find and print the top and bottom ten rows of auto.csv, as sorted by their dom score. with the top 5 and the bottom 5 domination scores. That print out will look something like this (you dont’ need to emulate this, just get the same info):


## Source Files
All source files are present in ./src/ directory <br />

Col.py - Abstract Class for Column Type <br />
Num.py - Class for numerical Columns (inherits Col) <br />
Sym.py - Class for Symbolic Columns (inherits Col) <br />
ID.py - Generates new ID each time <br />
Row.py - Class to represent each Row. (needs Class Table) <br />
Table.py - Class to represnt table. (uses CSV Reader from HW1 to read input file) <br />

./data/ contains sample data files

## Setup
Code requires Python 2.7.12 or above. <br />
It uses these packages: (`os, sys, argparse, abc`)

## Usage
To run the code,

`python src/Table.py <file_path>`

The file path can be changed as required.
The source File Table.py requires code from HW1. It has been added in the path (using sys.path).
To ensure that it always runs, please run it from this (/HW2/) directory (using the same command above)


More details about the instructions can be found at [Homeworks](https://txt.github.io/fss17/homeworks)
