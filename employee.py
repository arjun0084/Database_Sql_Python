class Employee:
    empcount=0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1

    def displaycount (self):
        print("Total Employee ",Employee.empcount)

    def displayEmployee(self):
        print("Name: ",self.name,",Salary: ",self.salary)

emp1=Employee("arjun",5800000)
emp2=Employee("reddy",0)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee", Employee.empcount)