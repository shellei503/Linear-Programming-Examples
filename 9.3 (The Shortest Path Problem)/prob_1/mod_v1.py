"""
9.3-1. You need to take a trip by car to another town that you have never visited before. Therefore,
you are studying a map to determine the shortest route to your destination. Depending on which route you choose,
there are five other towns (call them A, B, C, D, E) that you might pass through on the way. The map shows the
mileage along each road that directly connects two towns without any intervening towns. These numbers are sum-
marized in the following table, where a dash indicates that there is no road directly connecting these two towns
without going through any other towns.

        Town    A   B   C   D   E   Dest
        Origin  40  60  50  --  --  --
        A           10  --  70  --  --
        B               20  55  40  --
        C                   --  50  --
        D                       10  60
        E                           80

(a) Formulate this problem as a shortest-path problem by drawing a network where nodes represent towns,
links represent roads, and numbers indicate the length of each link in miles. (b) Use the algorithm described in Sec.
9.3 to solve this shortest- path problem. C (c) Formulate and solve a spreadsheet model for this problem. (d) If each
number in the table represented your cost (in dollars) for driving your car from one town to the next, would the an-
swer in part (b) or (c) now give your minimum cost route? (e) If each number in the table represented your time (in
minutes) for driving your car from one town to the next, would the an- swer in part (b) or (c) now give your minimum
time route?

Copyright @author: S. Lei
"""

import pandas as pd
from docplex.mp.model import Model
from helper_functions.util import export_soln_to_csv

# Read in external data
df = pd.read_csv('data_arc.csv')

# Initializing external data
distance = dict([((t.origin, t.destination), t.distance) for t in df.itertuples()])

# Indices for edges
edges = list((t.origin, t.destination) for t in df.itertuples())

# Indices used in constraint 1
final_destination = 'T'
cities = set(df['destination'])
cities.remove(final_destination)

# Creating list for final leg (used in constraint 2)
last_arc_df = df[df['destination'] == 'T']
last_arc = list((t.origin, t.destination) for t in last_arc_df.itertuples())

# Create the model
m = Model('9.3-1')

# Create decision variables
x = m.binary_var_dict(edges, name='x')

# Objective Function
m.minimize(m.sum(distance[uv] * x[uv] for uv in edges))

# Constraint 1
for c in cities:
    m.add_constraint((m.sum(x[(u, v)] for u, v in edges if v == c)) ==
                     (m.sum(x[(v, w)] for v, w in edges if v == c)), ctname='city_' + c)

# Constraint 2
m.add_constraint(m.sum(x[(i, j)] for i, j in last_arc if j == 'T') == 1, ctname='last_arc')

# Check
print(m.export_to_string())

# Model Solve parameters
m.parameters.timelimit = 120
m.parameters.mip.strategy.branch = 1
m.parameters.mip.tolerances.mipgap = 0.15

# Solve model
soln = m.solve(log_output=True)

# Display results
print(m.get_solve_status())
soln.display()

path = []
for i in x:
    if soln.get_var_value(x[i]) > 0:
        path.append(i[1])
print(path)

# Export results to csv
lst = []
for u,v in edges:
    if soln.get_var_value(x[u, v]) > 0:
        arc = u + '->' + v
        solution = (u, v, arc, distance[u, v])
        lst.append(solution)
df = pd.DataFrame.from_records(lst, columns=['origin', 'destination', 'arc_name', 'distance'])

export_soln_to_csv(df, m.get_name())
