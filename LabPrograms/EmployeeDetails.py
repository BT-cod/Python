                               
class Employee:
    def __init__(self):
        self.name = ""
        self.empId = ""
        self.dept = ""
        self.salary = 0
#SubClass Section--Taking Input--Employee Details
    def getEmpDetails(self):
        self.name = input("Enter Employee name: ")
        self.empId = input("Enter Employee ID: ")
        self.dept = input("Enter Employee Dept: ")
        self.salary = int(input("Enter Employee Salary: "))
#SubClass Section--Printing Output--Employee Details
    def showEmpDetails(self):
        print("---------------Employee Details-------------------")
        print("Name:", self.name)
        print("ID:", self.empId)
        print("Dept:", self.dept)
        print("Salary:", self.salary)
        print("---------------------------------------------------")
#SubClass Section--Updating--Employee Details--salary
    def updtSalary(self):
        self.salary = int(input("Enter new Salary: "))
        print("Updated Salary:", self.salary)
#Calling all the functions one-by-one
e1 = Employee()
e1.getEmpDetails()
e1.showEmpDetails()
e1.updtSalary()
e1.showEmpDetails()
