class Model():
    def __init__(self, name, model, accuracy):
        self.name = name
        self.model = model
        self.accuracy = accuracy
    
    def __str__(self):
        return self.name + " with accuracy " + str(self.accuracy*100) + "%"