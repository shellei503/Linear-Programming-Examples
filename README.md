# Introduction To Operations Research 7th ed
  Provides sample Python code to solve homework problems from the textbook Introduction to Operations Research, 7th edition by 
  Hillier and Lieberman
  
  Textbook pdf: https://notendur.hi.is/kth93/3.20.pdf
  

## Directory Structure

The general folder structure of this repository is as follows:
```
root/section/problem
```
#### Additional notes
* The  `helper_functions` folder is a python package with functions used across multiple problems
* An `output` folder is created when a model script is run. It stores exported csv solution  
* Each problem folder contains at least one mod.py file. This is the file

## Naming convention

#### Folders
* lowercase with underscore
* section - chapter.section + (Section Title) --> `8.1 (The Transportation Problem)`
* problem - prob_{number} --> `prob_1`
 
#### Files
* lowecase with underscore
* model - mod_v{version number}.py --> `mod_v1.py`
* data - data_{descriptive_name}.csv --> `data_arc.csv`
* output - soln_{model_name}.csv --> `soln_8.1-1.csv`

### Jupyter Notebooks
* notebook - {chapter}.{section}-{problem} --> `8.1-1.ipynb`
* embedded image - {img}_{notebook}_{description}.png --> `img_8.1-1_table.png`
 
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
1. Select a `section` folder -> i.e. `8.1 (The Transportation Problem)`
2. Select a`problem` folder -> i.e. `i.e. 8.1 (The Transportation Problem)/prob_1/`
3. Select a `model` file -> i.e. `8.1 (The Transportation Problem)/prob_1/mod_v1.py`
3. Run `model` file using default configuration (on Mac: ctrl+shift+R)
4. Running the `model` file will create a new `output` folder (within the `section` directory). Solutions results 
will be exported this this folder in a csv format.


## Contact

Please feel free to contact us with any questions, suggestions or comments:
* S. Lei
* slei232@gmail.com

