class Analysis():
    def __init__(self, name, results):
        self.name = name
        self.results = results

    def __str__(self):
        return self.name + " with results: \n" + str(self.results)