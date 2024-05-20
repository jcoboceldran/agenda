import pandas as pd
from sklearn.datasets import load_iris

from agenda import Agenda
from agenda.components import Standard_scaler, Correlation_analysis, Random_forest


flow = [Standard_scaler, Correlation_analysis, Random_forest]

data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target


agenda = Agenda(flow, df, 'target')

