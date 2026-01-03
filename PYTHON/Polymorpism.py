# class Employee:
#     def get_designation(self):
#         print("Employee")

class Teacher:
    def get_designation(self):
        print("Employee + Teacher")

class Accountant:
    def get_designation(self):
        print("Accountant + Employee")

t1 = Teacher()
t1.get_designation()

acc1 = Accountant()
acc1.get_designation()