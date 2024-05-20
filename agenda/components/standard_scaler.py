import pandas as pd
from sklearn.preprocessing import StandardScaler

from agenda.variables import *
from agenda.constructors import *

class Standard_scaler():
    def __init__(self, agenda):
        self.data = agenda.data
        self.target = agenda.target
        self.new_data = self.transform()

    def transform(self):
        scaler = StandardScaler()
        data_no_target = self.data.drop(self.target, axis=1)
        scaled_data = scaler.fit_transform(data_no_target)
        scaled_data = pd.DataFrame(scaled_data, columns=data_no_target.columns)
        scaled_data = pd.concat([scaled_data, self.data[self.target]], axis=1)
        return scaled_data

    def execute(self):
        transformation_object = Transformation("Standard Scaler", self.data, self.new_data)
        return self.new_data, self.report(), transformation_object, None, None
    
    def report(self):
        html = "<h2>Standard Scaler</h2>"
        html += "<p>Standard scaler done.</p>"
        return html
    