class A:
    def __init__(self,num):
        self.num=num
    def changenum(self):
        self.num=0

a=A(2)
a.changenum()
print(a.num)
a=[1,2,3,4,5,6,7,8,9]
for i in a:
    if i==2:
        i=3
print(a)