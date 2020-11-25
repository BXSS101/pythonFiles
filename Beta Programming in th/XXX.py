class Employee :
    'Common Base Class on employee'
    empCount = 0
    def __init__(self, name, salary):​
        self.name = name​
        self.salary = salary​
        Employee.empCount += 1​
    def displayCount(self):​
        print ("Total Employee %d" % Employee.empCount)​
    def displayEmployee(self):​
        print ("Name : ", self.name, ", Salary: ", self.salary)​

emp = Employee('Jame',2500)​
print ("Employee.__doc__:", Employee.__doc__)​
print ("Employee.__name__:", Employee.__name__)​
print ("Employee.__module__:", Employee.__module__)​
print ("Employee.__bases__:", Employee.__bases__)​
print ("Employee.__dict__:", Employee.__dict__)​
print ("emp1.__dict__",emp1.__dict__)​
Employee.__doc__: Common base class for all employees​
Employee.__name__: Employee​
Employee.__module__: __main__​
Employee.__bases__: (<class 'object'>,)​
Employee.__dict__: ​
{'__module__': '__main__’, ​
'__doc__': 'Common base class for all employees’, ​
'empCount': 1, ​
'__init__': <function Employee.__init__ at 0x7ff603587bf8>, 'displayCount': <function Employee.displayCount at 0x7ff6035877b8>, ​
'displayEmployee': <function Employee.displayEmployee at 0x7ff6035879d8>, ​
'__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>}​
emp1.__dict__ {'name': 'Jame', 'salary': 2500}​