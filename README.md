# Introduction To Operations Research
  Created for students just learning about Operations Research. Goes over key problem structures you are likely to encounter in industry and shows how to solve using Python.

  Recommended reading: Introduction to Operations Research, 7th edition by Hillier and Lieberman <br>
  Textbook pdf: https://notendur.hi.is/kth93/3.20.pdf
  

## Directory Structure

The general folder structure of this repository is as follows:
```
root/section/problem/model
root/section/problem/data
root/section/problem/notebook
root/section/problem/image
```
#### Additional notes
* The  `helper_functions` folder is a python package with functions used across multiple problems
* An `output` folder is created when a model script is run. It stores exported csv solutions  

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

#### Jupyter Notebooks
* notebook - {chapter}.{section}-{problem} --> `8.1-1.ipynb`
* image - {img}_{notebook}_{description}.png --> `img_8.1-1_table.png`
 
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

## Stand alone models ready to run
* 8.1 (The Transportation Problem)/prob_1/mod_v1.py
* 9.3 (The Shortest Path Problem)/prob_1/mod_v1.py

## Running Models
1. Select a `model` file -> i.e. `8.1 (The Transportation Problem)/prob_1/mod_v1.py`
2. Execute the `model` file using default configuration (on Mac: `ctrl+shift+R`)
3. Review model results in the newly created `output` folder -> `8.1 (The Transportation Problem)/prob_1/output`

## Contact
Please feel free to contact us with any questions, suggestions or comments:
* S. Lei
* slei232@gmail.com

