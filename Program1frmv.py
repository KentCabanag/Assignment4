def getNameAgeAdd():
    _name = input("Enter your name: ")
    _age = int(input("Enter your age: "))
    _add = input("Enter you address: ")
    return _name, _age, _add

def _format(_Name, _Age, _Address):
    print(f"Hi, my name is {_Name}. I am {_Age} years old and I live in {_Address}.")

name, age, add = getNameAgeAdd()

_format(name, age, add)