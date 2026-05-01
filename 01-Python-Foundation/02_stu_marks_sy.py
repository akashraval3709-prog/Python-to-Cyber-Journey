class Student:
    def __init__(self,name):
        self.name=name
        self.__marks1=0
        self.__marks2=0
        self.__marks3=0
    @property
    def marks(self):
        return f'Student Marks : {self.__marks1}, {self.__marks2}, {self.__marks3}'
    
    @marks.setter
    def marks(self,value):
        if len(value) == 3:
         m1, m2, m3 = value
        if m1 >= 0 and m2 >= 0 and m3 >= 0:
            self.__marks1=m1
            self.__marks2=m2
            self.__marks3=m3
       
    
    def result(self):
        total = self.__marks1 + self.__marks2 + self.__marks3
        per = total / 3
        return f'Total Marks :{total}\nPer :{per:.2f}'
    def show(self):
        
        return f'\n\nName : {self.name}'
        


stu1=Student('Akash')
stu1.marks=(89,90,91)
print(stu1.show())
print(stu1.marks)
print(stu1.result())
