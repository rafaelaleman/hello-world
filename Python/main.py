# comment
class Person:
    def __init__(self, name, dateOfBirth):
        self.name = name
        self.dateOfBirth = dateOfBirth


    def SetName(self, name):
        self.name = name

    def GetName(self):
        return self.name

x  =5
print(x);
print('hello, Rafael')
print('im happy today')
print('planning to go out to the outlet')
iteration = 1

while iteration <= 5:
    print(iteration)
    iteration += 1

print('end')

input("Press Enter to continue...")

myArray = ['rafael','maria','miguel','gabriel']
print(myArray[0])

# using classes
print("\n using classes")
p1 = Person("Rafael", "06/19/1976")
print(p1.GetName())

# using lists
a = []

a.append("rafael")
a.append("maria")
a.append("miguel")
a.append("gabriel")

print(a)

# using dictionaries

print("\n using dictionaries:")
myDictionary = {"rafael": 1976, "maria": 1971, "miguel": 2006, "gabriel": 2006 }
print(myDictionary)
myDictionary["rafael"] = 1985
print(myDictionary)

for element in myDictionary:
    print(element,   myDictionary[element])
