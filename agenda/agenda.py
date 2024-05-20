import time
import os

from agenda.variables import *

class Agenda():
    def __init__(self, flow, data, target):
        self.flow = flow
        self.data = data
        self.target = target
        self.reports = []
        self.transformations = []
        self.models = []
        self.analysis = [] 
        self.execute()
        self.report()

    def execute(self):
        for component in self.flow:
            component_instance = component(self)
            print("Executing " + component_instance.__class__.__name__ + "...")
            start_time = time.time()
            data, report, transformation, model, analysis = component_instance.execute()
            end_time = time.time()
            print("Done in " + str(end_time - start_time) + " seconds")
            print("\n")
            if data is not None:
                self.data = data
            attributes = {
                report: self.reports,
                transformation: self.transformations,
                model: self.models,
                analysis: self.analysis
            }
            for item, attr_list in attributes.items():
                if item:
                    attr_list.append(item)

    def report(self):
        try:
            os.mkdir(OUTPUT_PATH)
        except:
            pass
        with open(OUTPUT_PATH + 'style.css', 'w') as f:
            f.write(CSS)
        html = HTML_HEADER
        for h in self.reports:
            html += h
        html += HTML_CLOSER
        with open(OUTPUT_PATH + 'report.html', 'w') as f:
            f.write(html)
        
        print("Report generated at " + OUTPUT_PATH + 'report.html')
        