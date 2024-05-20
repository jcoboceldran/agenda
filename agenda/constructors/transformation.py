class Transformation():
    def __init__(self, name, old_data, new_data):
        self.name = name
        self.old_data = old_data
        self.new_data = new_data

    def __str__(self):
        return self.name + " transformation done"