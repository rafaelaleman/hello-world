class Person:
    def __init__(self, name, dateOfBirth):
        self.name = name
        self.dateOfBirth = dateOfBirth


    def SetName(self, name):
        self.name = name

    def GetName(self):
        return self.name
