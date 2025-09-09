# # # # f = open("demo.txt", "r+")
# # # # f.write("hello")
# # # # # f.close()

# # # #     name = "kartik"

# # # # s1 = Student()
# # # # print(s1.name)
    
# # # class Student:
# # #     college_name = "RKGIT"
# # #     def __init__ (self, name, section, year):
# # #         self.name = name
# # #         self.section = section
# # #         self.year = year

# # # s1 = Student("Kartik", "AIML A", 2023)
# # # print(s1.name, s1.section, s1.year, sep="\n")
# # # print(s1.college_name)

# # class details:
# #     def __init__(self, name ,marks):
# #         self.name=name
# #         self.marks=marks   
# #     def average(self):
# #             return sum(self.marks)/len(self.marks)
        
# # s1=details("kartik", 90, 80, 70)
# # print("name=" ,s1.name, "marks=", s1.marks)
# # print("average=",s1.average())

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
        
    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "debited from your account")
        print("total amount", self.get_balance())
        
    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "credited to your account")
        print("total amount", self.get_balance())
        
    def get_balance(self):
        return self.balance  
          
acc1 = Account(100000, 543534253)
acc1.debit(10000)
print("Final balance:", acc1.get_balance())