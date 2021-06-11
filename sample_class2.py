class Example():
    def __init__(self, a,b,c):
        self.num1 = a
        self.num2 = b
        self.num3 = c


    def print_tot(self):
        tot = self.num1+self.num2+self.num3
        print(tot)

    def print_tot2(self):
        tot2 = self.num1*self.num2*self.num3
        print(tot2)


myinstance = Example(1,2,3)
myinstance.print_tot()
myinstance.print_tot2()
myinstance2 = Example(4,5,6)
myinstance2.print_tot()
myinstance2.print_tot2()
