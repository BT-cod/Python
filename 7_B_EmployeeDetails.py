# Write a python program by creating a class called Employee to store the details of Name,
# Employee_ID, Department and Salary, and implement a method to update salary of
# employees belonging to a given department.

#SuperClass Section--Employee Details
class Employee:
    def __init__(self):
        self.name = ""
        self.empId = ""
        self.dept = ""
        self.salary = ""
#SubFunction Section--Taking Input--Employee Details
    def getEmpDetails(self):
        self.name = input("Enter Employee Name: ")
        self.empId = input("Enter Employee Id: ")
        self.dept = input("Enter Employee Department: ")
        self.salary = int(input("Enter Employee Salary: "))
#SubFunction Section--Printing Output--Employee Details
    def showEmpDetails(self):
        print("---------------------------Employee Details--------------------------")
        print("Name:", self.name)
        print("Employee Id:", self.empId)
        print("Department:", self.dept)
        print("Salary:", self.salary)
        print("-----------------------------------------------------")
#SubFunction Section--Updating--Employee Details--salary
    def updtSalary(self):
        self.salary = int(input("Enter the updated salary: "))
#Calling all the functions one-by-one
e1 = Employee()
e1.getEmpDetails()
e1.showEmpDetails()
e1.updtSalary()
e1.showEmpDetails()
