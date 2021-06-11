class MyClass():
    def __init__(self, message):
        self.value = message


myinstance = MyClass("Hello!")
print(myinstance.value)

myinstance2 = MyClass("bay!")
print(myinstance2.value)