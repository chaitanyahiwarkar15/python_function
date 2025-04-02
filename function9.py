# Employee Management System

def employee_details(**kewargs):
    print("n/r Employee Details")
    for key, value in kewargs.items():
        print(f"{key.capitalize()}: {value}")

employee_details(Name = "virat kohli", age = 30, salary = 500000, Department = "IT")
employee_details(name="Amit Sharma", age=30, department="IT", salary=75000)
employee_details(name="Priya Verma", age=28, department="HR", experience="5 years", location="Mumbai")
employee_details(name="Rahul Mehta", age=35, department="Finance", position="Manager", salary=95000, location="Bangalore")