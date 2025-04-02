# stored students records 

def student_record(**kewargs):
    print("/n Students Records")
    for key , value in kewargs.items():
        print(f"{key.capitalize()}: {value}")

student_record(name="Ravi Kumar", age=21, course="B.Tech", university="IIT Delhi")
student_record(name="Sneha Sharma", age=22, course="MBA", university="IIM Bangalore", specialization="Finance")       
    