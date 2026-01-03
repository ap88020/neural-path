# # # class Student:
# # #     def __init__(self,name):
# # #         # print("constructor was called....")
# # #         self.name = name

# # #     # subject = "Python"
# # #     # college = "ABC"
# # #     # year = "4th year"

# # # stu1 = Student("ashu")
# # # stu2 = Student("bashu")

# # # # print(stu1.college , stu1.subject, stu1.year)
# # # # print(stu2.college , stu2.subject, stu2.year)

# # # print(stu1.name)
# # # print(stu2.name)


# # class Student:
# #     def __init__(self,name,cgpa):
# #         self.name = name
# #         self.cgpa = cgpa
    
# #     def get_cgpa(self):
# #         return self.cgpa


# # stu1 = Student("guru-randhawa" , 9.0)

# # print(f"{stu1.name} has good cgpa which is {stu1.get_cgpa()}")

# class Student:
#     college_name = "Abc college" #class-attribute

#     def __init__(self,name,cgpa):
#         self.name = name
#         self.cgpa = cgpa
#         self.PI = 3.14
    
# stu1 = Student("Romio",9.0)


# print(stu1.cgpa)

class Laptop:
    storage_type = "ssd"
    def __init__(self,ssd,ram):
        self.ssd = ssd
        self.ram = ram
    @classmethod
    def get_ssd(cls):
        print(f"the storage type : {cls.storage_type}")

    def get_info(self):
        print(f"this laptop has {self.ssd} SSD or {self.ram} RAM")

    @staticmethod
    def calc_method(price,disc):
        final_price = price - (disc*price/100)
        print(f"discounted price : {final_price}")


lap = Laptop("1tb","8gb")
Laptop.get_ssd()
lap.calc_method(400,20)