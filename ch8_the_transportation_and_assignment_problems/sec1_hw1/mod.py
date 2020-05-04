"""
8.1-1. The Childfair Company has three plants producing child push chairs that are to be shipped to four
distribution centers. Plants 1, 2, and 3 produce 12, 17, and 11 shipments per month, respectively. Each
distribution center needs to receive 10 shipments per month. The distance from each plant to the respective
distributing centers is given as shown below (in miles)

            Dist1   Dist2   Dist3   Dist4
Plant 1     800     1300    400     700
Plant 2     1100    1400    600     1000
Plant 3     600     1200    800     900

The freight cost for each shipment is $100 plus 50 cents per mile. How much should be shipped from each plant to each
of the distribution centers to minimize the total shipping cost? (a) Formulate this problem as a transportation
problem by constructing the appropriate parameter table. (b) Draw the network representation of this problem. (c)
Obtain an optimal solution.

Copyright @author: S. Lei
"""

import pandas as pd
from docplex.mp.model import Model
from helper_functions.util import export_soln_to_csv

# Read in external data
df_arc = pd.read_csv('data_arc.csv')
df_plant = pd.read_csv('data_plant.csv')
df_distribution = pd.read_csv('data_distribution.csv')

# Indices/sets
arcs = list((t.plant, t.distribution) for t in df_arc.itertuples())
plants = df_plant['plant']
distributions = df_distribution['distribution']

# Parameters
distance = dict([((t.plant, t.distribution), t.distance) for t in df_arc.itertuples()])
capacity = df_plant['capacity']
demand = df_distribution['demand']

# Fixed parameters
shipment_cost = 100
per_mile_cost = .50
max_demand = 10

# Create model
m = Model('8.1-1')

# Create decision variables
x = m.integer_var_dict(arcs, name='x')

# Objective function
m.minimize(m.sum(distance[ij] * per_mile_cost * x[ij] for ij in arcs) + m.sum(shipment_cost * x[ij] for ij in arcs))

# capacity constraint
for i in plants:
    m.add_constraint(m.sum(x[(i, j)] for j in distributions) <= capacity[i - 1], ctname='capacity_constraint_%d' % i)

# demand constraint
for j in distributions:
    m.add_constraint(m.sum(x[i, j] for i in plants) >= demand[i - 1], ctname='demand_constraint_%d' % j)

# check
print(m.export_to_string())

# Set parameters for solving model
m.parameters.timelimit = 120
m.parameters.mip.strategy.branch = 1
m.parameters.mip.tolerances.mipgap = 0.15

# solve model
soln = m.solve(log_output=True)

# Display results
print(m.get_solve_status())
soln.display()

# Export results to csv
lst = []
for i in x:
    if soln.get_var_value(x[i]) > 0:
        solution = (i[0], i[1], soln.get_var_value(x[i]))
        lst.append(solution)
df = pd.DataFrame.from_records(lst, columns=['plant', 'distribution', 'quantity'])

export_soln_to_csv(m, df)
