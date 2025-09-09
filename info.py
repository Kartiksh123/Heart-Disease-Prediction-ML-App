# # # cities =["delhi","mumbai","gurgaon","noida"]
# # # heroes = ["superman","batman","ironman",]

# # # def print_len(list):
# # #     print(len(list))

# # # print_len(cities)
# # # print_len(heroes)
# # # def print_list(list):
# # #     for item in list:
# # #         print(item, end=" ")

# # # print_list(cities)


# # # def fact(n):
# # #     fact = 1
# # #     for i in range(1,n+1):
# # #         fact*=i
# # #     print(fact)
# # #     return 0
        
# # # fact(5)




# # # # def converter(usd):
# # # #     inr=usd*83.5
# # # #     print(usd , "usd=" ,inr , "inr=")

# # # # converter(100)


# # # #write a program to print odd if the number is odd and even if the number is even
# # # def odd_even(n):
# # #     if n%2==0:
# # #         print("even")
# # #     else:
# # #         print("odd")
# # # # # # # # # # odd_even(10)

# # # # def show(n):
# # # #     if n==18:
# # # #         return 0
# # # #     print(n)
# # # #     show(n+1)

# # # # show(0)


# # # def fact(n):
# # #     if (n==0 or n==1):
# # #         return 1 
# # #     else:
# # #         return n*fact(n-1)
# # # print(fact(8))

# # # def sum(n):
# # #     if n==0:
# # #         return 0
# # #     print(n)
# # #     return sum(n-1) + n
# # # calc = sum(6)
# # # print(calc)

# # # f = open("demo.txt", "r")
# # # data = f.read()
# # # print(data)
# # # print(type(data))
# # # # # # # # f.close()

# # # # # # # class Student:
# # # # # # #     name = "kartik"

# # # # # # # s1 = Student()
# # # # # print(s1.name)
    
# # # # # class Student:
	
# # # # # # 	def __init__ (self, name, section, year):
# # # # # # 		self.name = name
# # # # # # 		self.section = section
# # # # # # 		self.year = year

# # # # # # # f = open("demo.txt", "r+")
# # # # # # # f.write("hello")
# # # # # # # # f.close()

# # # # # # #     name = "kartik"

# # # # # # # s1 = Student()
# # # # # # # print(s1.name)
    
# # # # # class Student:
# # # # #     college_name = "RKGIT"
# # # # #     def __init__ (self, name, section, year):
# # # # #         self.name = name
# # # # #         self.section = section
# # # # #         self.year = year

# # # # # s1 = Student("Kartik", "AIML A", 2023)
# # # # # print(s1.name, s1.section, s1.year, sep="\n")
# # # # # print(s1.college_name)

# # # # # s1 = Student("Kartik" "AIML A", 2023)
# # # # # print(s1.name , s1.section , s1.year, sep="\n")

# # # # # s1 = Student("Kartik", "AIML A", 2023)
# # # # # print(s1.name, s1.section, s1.year, sep="\n")
# # # # # print(s1.college_name)

# # # # class details:
# # # #     def __init__(self, name, marks):
# # # #         self.name = name
# # # #         self.marks = marks   
        
# # # #     def average(self):
# # # #         return sum(self.marks) / len(self.marks)
# # # #     @staticmethod
# # # #     def hello():
# # # #         print("hello")    
# # # # s1 = details("kartik", [90, 80, 70])
# # # # print("name=", s1.name, "marks=", s1.marks)
# # # # print("average=", s1.average())
# # # # print(s1.hello())

# # class Account:
# #     def __init__(self, bal,acc):
# #         self.balance = bal
# #         self.account_no = acc
        
# #     #debit method
# #     def debit(self,amount):
# #         self.balance -= amount
# #         print("Rs.", amount, "debited from your account")
# #         print("total amount", self.get_balance())
        
# #     #credit method
# #     def credit(self, amount):
# #         self.balance += amount
# #         print("Rs.", amount, "credited to your account")
# #         print("total amount", self.get_balance())
    
# #     def get_balance(self):
# #         return self.balance  
		  
# # acc1= Account(100000,543534253)
# # acc1.debit(5000)
# # acc1.credit(100000000)

# import random

# number_to_guess = random.randint(1, 100)
# guess = None
# attempts = 0

# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")

# while guess != number_to_guess:
#     try:
#         guess = int(input("Enter your guess: "))
#         attempts += 1

#         if guess < number_to_guess:
#             print("Too low! Try again.")
#         elif guess > number_to_guess:
#             print("Too high! Try again.")
#         else:
#             print(f"Congratulations! You guessed the number in {attempts} attempts.")
#     except ValueError:
#         print("Please enter a valid number.")

# Program to find the ASCII value of a character

# Take input from the user
char = input("Enter a character: ")

# Print ASCII value using ord() function
print("The ASCII value of", char, "is", ord(char))