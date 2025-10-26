class EmpRequir:
    def __init__(self, employee_Number):
        self.employee_Number = employee_Number        

    def dataEmployee(self, emp_name, emp_salary, emp_position):
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_position = emp_position

    def display_info(self):
        print("Name:: ",self.emp_name, "Actual Position: ",self.emp_position,"Salary",self.emp_salary)
        return "\n"

    def give_raise(self):
        self.emp_salary = self.emp_salary * 1.1
        print("You got a 10%/ raise. Your new salary is ", self.emp_salary)

def HR_OO():
    
    emp1 = EmpRequir(10)
    emp2 = EmpRequir(20)

    emp1.dataEmployee("Salim", 1000, "Manager")
    emp2.dataEmployee("Henri", 2000, "Engineer")
    
    print(emp1.display_info())
    print(emp2.display_info())

    emp1.emp_salary = emp1.emp_salary * 1.1
    print("Employee number", emp1.employee_Number, " named ", emp1.emp_name, "had an increase of " \
    "10% on his salary. New salary is", emp1.emp_salary)

if __name__ == "__main__":
    HR_OO()