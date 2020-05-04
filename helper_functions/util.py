# Create directory to save output to
import os


def export_soln_to_csv(model, df):
    """ model refers to model object from docplex.mp.model"""

    base_dir = os.getcwd()
    try:
        os.mkdir(os.path.join(base_dir, 'output'))
    except:
        pass

    filename = 'output/' + 'soln_' + model.get_name() + '.csv'
    solution_output = os.path.join(os.getcwd(), filename)
    df.to_csv(solution_output, index=False)


# ****************************************
# check
# ****************************************
from docplex.mp.model import Model
import pandas as pd

# sample df
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

# sample model
m = Model('prob1')

if __name__ == '__main__':
    export_soln_to_csv(m, df)
