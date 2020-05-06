"""
9.4-2. The Wirehouse Lumber Company will soon begin logging eight groves of trees in the same general area. Therefore,
it must develop a system of dirt roads that makes each grove accessible from every other grove. The distance (in
miles) between every pair of groves is as follows:

                grove_1   grove_2     grove_3     grove_4     grove_5     grove_6     grove_7     grove_8
    grove_1     --        1.3         2.1         0.9         0.7         1.8         2.0         1.5
    grove_2     1.3       --          0.9         1.8         1.2         2.6         2.3         1.1
    grove_3     2.1       0.9         --          2.6         1.7         2.5         1.9         1.0
    grove_4     0.9       1.8         2.6         --          0.7         1.6         1.5         0.9
    grove_5     0.7       1.2         1.7         0.7         --          0.9         1.1         0.8
    grove_6     1.8       2.6         2.5         1.6         0.9         --          0.6         1.0
    grove_7     2.0       2.3         1.9         1.5         1.1         0.6         --          0.5
    grove_8     1.5       1.1         1.0         0.9         0.8         1.0         0.5         --

Management now wishes to determine between which pairs of groves the roads should be constructed to connect all
groves with a minimum total length of road.<br>

(a) Describe how this problem fits the network description of the minimum spanning tree problem.
(b) Use the algorithm described in Sec. 9.4 to solve the problem.

Copyright @author: S. Lei
"""

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from helper_functions.util import export_soln_to_csv
from networkx.algorithms import tree


# model name
m = '9.4-2_v2'

# read in data
df = pd.read_csv('data_arc.csv')
df = df[df['distance'] != 0]

# create a Graph object
arcs = list((t[1], t[2]) for t in df.itertuples())
distance_dict = dict([((t[1], t[2]), t.distance) for t in df.itertuples()])

G = nx.Graph()

for x in arcs:
    i = x[0]
    j = x[1]
    weight = distance_dict[i,j]
    G.add_edge(i,j,weight = weight)

# solve for MSP
mst = tree.minimum_spanning_edges(G, algorithm='prim', data=False)
edges = list(mst)
edges

# print results
distance_lst = []
for x in edges:
    i = x[0]
    j = x[1]
    weight = distance_dict[i,j]
    distance_lst.append(weight)
total_distance = sum(distance_lst)
print(total_distance)
print(edges)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=400)
nx.draw_networkx_edges(G, pos, edgelist=edges, width=1)
nx.draw_networkx_labels(G, pos, font_size=15, font_family='sans-serif')

plt.axis('off')
plt.show()

# export solution to csv
node_1 = [i[0] for i in edges]
node_2 = [i[1] for i in edges]

output_df = pd.DataFrame(
    {'node_1': node_1,
     'node_2': node_2,
     'distance': distance_lst
     })

export_soln_to_csv(output_df, m)
