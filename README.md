# Introduction To Operations Research 7th ed
  Provides sample Python code to solve homework problems from the textbook Introduction to Operations Research, 7th edition by 
  Hillier and Lieberman
  
  Textbook pdf: https://notendur.hi.is/kth93/3.20.pdf
  

## Directory Structure

The folder structure of this repository is as follows:
```
root/chapter/problem
```
#### Naming convention
* chapter - ch{chapter number}_{chapter_title} --> **ch8_the_transportation_and_assignment_problems**
* problem - sec{section number}_hw{problem number} --> **sec1_hw1** 
* model - mod_v{version number}.py --> **mod_v1.py**
* data - data_{descriptive_name}.csv --> **data_arc.csv** 

#### Models and data files
* each problem folder contains at least one mod.py file. This is the file 

## Environment/Packages/Libraries
* Conda
* Python             (3.7)
* cplex              (12.10.0.1)
* docplex            (2.13.184)
* xlrd               (1.2.0)

## Installation
All models require CPLEX to solve. Install `cplex` with `pip`
```
python -m pip install cplex

```
Some models are written using docplex module. Install `docplex` with `pip`
```
python -m pip install docplex
```
Some models/notebooks use xlrd library to read in .csv and/or .xlsx files. Install `xlrd` with `pip`
```
python -m pip install xlrd
```

## Running Models
1. Open up the `probelm` folder (i.e. ch8_the_transportation_and_assignment_problems/sec1_hw1)
2. Open `mod.py` file
3. Run `mod.py` using default configuration (on Mac: ctrl+shift+R)
4. `mod.py` will create a new `output` folder and export solution results to a csv file to this folder


## Contact

Please feel free to contact us with any questions, suggestions or comments:

* Xueli Lei
* slei232@gmail.com

