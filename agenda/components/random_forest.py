from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from agenda.constructors.model import Model

from agenda.variables import *
from agenda.constructors import *

class Random_forest():
    def __init__(self, agenda):
        self.data = agenda.data
        self.target = agenda.target
        self.model, self.accuracy = self.model()

    def model(self):
        data = self.data
        target = self.target
        X = data.drop(target, axis=1)
        y = data[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        model = RandomForestClassifier(n_estimators=100)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return model, accuracy
    
    def execute(self):
        model_object = Model("Random Forest", self.model, self.accuracy)
        return None, self.report(), None, model_object, None

    def report(self):
        html = "<h2>Random Forest Model</h2>"
        html += "<p>Random forest model done with " + str(self.accuracy*100) + "% accuracy</p>"
        return html
   