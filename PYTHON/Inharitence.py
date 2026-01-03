class Employee:
    start_time = "10AM"
    end_time = "6PM"

    def change_time(self , new_endTime):
        self.end_time = new_endTime

class Teacher(Employee):
    def __init__(self,subject):
        self.subject = subject


class Admin(Employee):
    def __init__(self,role):
        self.role = role
        

# t1 = Teacher("Math")
# t1.change_time("9PM")

# print(t1.start_time,t1.end_time,t1.subject)
        
A1 = Admin("Manager")
print(A1.role , A1.start_time , A1.end_time)
