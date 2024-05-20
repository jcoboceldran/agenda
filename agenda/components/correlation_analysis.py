import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from agenda.variables import *
from agenda.constructors import *

class Correlation_analysis():
    def __init__(self, agenda):
        self.data = agenda.data
        self.corr = self.analyze()

    def analyze(self):
        return self.data.corr()
    
    def execute(self):
        analysis_object = Analysis("Correlation Analysis", self.corr)
        return None, self.report(), None, None, analysis_object

    def report(self):
        sns.heatmap(self.corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0, square=True, linewidths=.5)
        plt.title("Correlation Analysis")
        plt.savefig(IMG_PATH + "correlation_analysis.svg", bbox_inches='tight')

        html =  "<h2>Correlation Analysis</h2>"
        html += "<p>Correlation analysis done.</p>"  
        html += "<img src='img/correlation_analysis.svg'>"
        html += "<p>Correlation values:</p>"
        html += self.corr.to_html()
        return html
    