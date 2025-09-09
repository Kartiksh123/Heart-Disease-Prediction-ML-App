# # # # with open('example.txt','r') as f:
# # # #     content = f.read()
# # # # with open('source.txt','w') as f:
# # # #     f.write(content)

# # # # Program to merge two text files into one.
# # # # with open('example.txt') as f:
# # # #     content = f.read()
# # # # with open('source.txt', 'r') as f:
# # # #     content += f.read()

# # # # with open('merged.txt', 'w') as f:
# # # #     f.write(content)

# # # #Program that handles ZeroDivisionError and ValueError.
# # # # try:
# # # #     num1 = int(input("enter a number"))
# # # #     num2 = int(input("enter another number"))
# # # #     result = num1 / num2
# # # #     print(f"The result is {result}")
# # # # except ZeroDivisionError:
# # # #     print("Error: Division by zero is not allowed.")
# # # # except ValueError:
# # # #     print("Error: Invalid input. Please enter a valid integer.")
# # # # finally:
# # # #     print("Execution completed.")
# # # # Program using assert to validate input is less than 100.
# # # # try:
# # # #     num =int(input("enter a number less than 100:"))
# # # #     assert num<100
# # # #     print("Valid input:", num)
# # # # except AssertionError:
# # # #     print("Error: Input must be less than 100.")
# # # # except ValueError:
# # # #     print("Error: Invalid input. Please enter a valid integer.")

# # # #Create a binary file to store employee records (name, ID, salary).

# # # # import tkinter as tk
# # # # def information():
# # # #     name = name_entry.get()
# # # #     age = age_entry.get()
# # # #     Result_label.config(text=f"Name: {name}, Age: {age}")

# # # # window = tk.Tk()
# # # # window.title("Information")
# # # # window.geometry("300x200")

# # # # Result_label = tk.Label(window, text="")
# # # # Result_label.pack()

# # # # name_label = tk.Label(window, text="name: ")
# # # # name_label.pack()
# # # # name_entry = tk.Entry(window)
# # # # name_entry.pack()

# # # # age_label = tk.Label(window, text="age: ")
# # # # age_label.pack()
# # # # age_entry = tk.Entry(window)
# # # # age_entry.pack()

# # # # def greet():
# # # #     name = input("Enter your name: ")
# # # #     print(f"Hello, {name}! Welcome to the program.")
# # # #     # return f"greet sent to {name}"
# # # # greet()
# # # # num  = {1,2,3,2,3}
# # #   # This will raise an AttributeError since sets do not have an append method.
# # # # To add an element to a set, use the add method.
# # # # num.add(4)
# # # # print(set(num))

# # # # l = [1, 0, 0, 2, 3, 0, 4, 5, 0, 6, 7, 8, 9, 0]
# # # # l = list(set(l))
# # # # print(l)
# # # # Function to compute LCM
# # # # def find_lcm(x, y):
# # # #     if x > y:
# # # #         greater = x
# # # #     else:
# # # #         greater = y

# # # #     while True:
# # # #         if (greater % x == 0) and (greater % y == 0):
# # # #             lcm = greater
# # # #             break
# # # #         greater += 1

# # # #     return lcm

# # # # # Input from user
# # # # num1 = int(input("Enter first number: "))
# # # # num2 = int(input("Enter second number: "))

# # # # # Output
# # # # print("LCM of", num1, "and", num2, "is", find_lcm(num1, num2))
# # # #find common letters in two strings
# # # # name_1 = "hari"
# # # # name_2 = "hale"
# # # # common_letters = set(name_1)&set(name_2)
# # # # print("Common letters:", common_letters)
# # # #find the sum of all the items in a disctionary

# # # # dict_1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# # # # sum_of_values = sum(dict_1.values())    
# # # # print("Sum of all items in the dictionary:", sum_of_values)

# # # # print("calculator")
# # # # print("1. Addition")
# # # # print("2. Subtraction")
# # # # print("3. Multiplication")
# # # # print("4. Division")
# # # # num = int(input("Enter a number: "))

# # # # if num == 1:
# # # #     a = float(input("Enter first number: "))
# # # #     b = float(input("Enter second number: "))
# # # #     print("Result:", a + b)
# # # # elif num == 2:
# # # #     a = float(input("Enter first number: "))
# # # #     b = float(input("Enter second number: "))
# # # #     print("Result:", a - b)
# # # # elif num == 3:
# # # #     a = float(input("Enter first number: "))
# # # #     b = float(input("Enter second number: "))
# # # #     print("Result:", a * b)
# # # # elif num == 4:
# # # #     a = float(input("Enter first number: "))
# # # #     b = float(input("Enter second number: "))
# # # #     if b != 0:
# # # #         print("Result:", a / b)
# # # #     else:
# # # #         print("Error: Division by zero is not allowed.")
# # # # else:
# # # #     print("Invalid option.")

# # # # input_string = "hello world"
# # # # count =0
# # # # for char in input_string:
# # # #     if char.isalpha():  # Check if the character is an alphabet
# # # #         count += 1
# # # #         print(f"{count}: {char}")

# # # # import matplotlib.pyplot as plt
# # # # X_axis = (30,25,20,15,10)
# # # # Y_axis = ('python', 'java', 'c++', 'c#', 'javascript')
# # # # plt.pie(X_axis, labels=Y_axis)
# # # # plt.title("Programming Languages Popularity")
# # # # plt.legend(title="Languages")
# # # # plt.axis('equal')
# # # # plt.tight_layout()


# # # # plt.show()
# # # # longest_word= ('apple', 'banana', 'cherry', 'date')
# # # # print(max(longest_word, key=len))

# # # # Input from user
# # # # string = input("Enter a string: ")

# # # # # Create an empty dictionary to store character counts
# # # # char_count = {}

# # # # # Loop through each character in the string
# # # # for char in string:
# # # #     if char in char_count:
# # # #         char_count[char] += 1  # If character already exists, increment count
# # # #     else:
# # # #         char_count[char] = 1   # If character not present, add it with count 1

# # # # Display the result
# # # # print("Character frequencies:")
# # # # for char in char_count:
# # # #     print(f"'{char}': {char_count[char]}")

# # # # list_1 = [1,3,4,5,6,7]
# # # # sum = 0
# # # # for num in list_1:
# # # #     sum +=num
# # # # print("Sum of the list:", sum)
# # # # for i in range(0,50,2):
# # # #     print(i)

# # # # list_1 = [1, 2, 3, 4, 5,6,7]
# # # # for num in list_1:
# # # #     if num==7:
# # # #       print('found')
# # # #     else:
# # # #         print('not found')
# # # # class Person:
# # # #     def __init__(self, name, age):  # Constructor method
# # # #         self.name = name  # These lines are part of the class block
# # # #         self.age = age

# # # #     def greet(self):
# # # #         print(f"Hi, I am {self.name} and I am {self.age} years old.")

# # # # # Creating an instance of the class
# # # # p1 = Person("Alice", 30)
# # # # p1.greet()
# # # # file = open("example.txt", 'a')
# # # # file.write("wkwnlkwnklwndw")
# # # # print(file)
# # # # file.close()

# # # # with open('example.txt', 'r') as file:
# # # #     lines = file.readlines()
# # # #     longest_length = 0
# # # #     longest_line = ""
# # # #     for line in lines:
# # # #         line_length = len(line.strip())
# # # #         if line_length > longest_length:
# # # #             longest_length = line_length
# # # #             longest_line = line.strip()
# # # #     print(f"The longest line is: '{longest_line}'")
# # # #     print(f"Its length is: {longest_length} characters")
# # # # with open('example.txt', 'r') as file:
# # # #     searched_string = input("Enter the string: ")
# # # #     content = file.read()
# # # #     if searched_string in content:
# # # #         print('found')
# # # #     else:
# # # #         print('not found')

# # # # with open('example.txt','r') as exm:
# # # #     content = exm.read()
# # # #     char_count = 0
# # # #     for char in content:
# # # #         char_count+=1
# # # #     print(f"Total character are : {char_count}")
# # # #     exm.seek(0)
# # # #     content = exm.read() 
# # # #     word_count = 0
# # # #     for words in content:
# # # #        words = content.split()
# # # #        word_count =len(words) 
# # # #     print(f"Total words are : {word_count}")
# # # #     exm.seek(0)
# # # #     content = exm.readlines() 
# # # #     line_count= 0
# # # #     for lines in content:
# # # #       line = len(lines)
# # # #       line_count+=1
# # # #     print(f"Total lines are : {line_count}")
        
# # # # with open('example.txt','r') as file:
# # # #     lines = file.readlines()
# # # #     line_count = len(lines)
# # # #     word_count = 0
# # # #     character_count = 0
# # # #     for line in lines:
# # # #         words = line.split()
# # # #         word_count +=len(words)
# # # #         character_count += len(line)
# # # #     print(f"total lines{line_count}")
# # # #     print(f"total word{word_count}")
# # # #     print(f"total character{character_count}")

# # # # with open('example.txt','r') as inp , open('source.txt','w') as out:
# # # #     lines = inp.readlines()
# # # #     for line in lines:
# # # #       capitalized_line = line.title()
# # # #       out.write(capitalized_line)
# # # #     print(out)

# # # # with open('p.txt', 'w') as file:
# # # #     file.write("My name")
# # # #     file.write("Father name")
# # # # with open('p.txt', 'r') as file:
# # # #     content = file.read()
# # # #     print(content)

        

# # # # Name = "mynk"
# # # # Age = 20
# # # # print("Name:", Name)
# # # # print("Age:", Age)

# # # # import pandas as pd     
# # # # data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 
# # # #         'Age': [25, 30, 35, 40], 
# # # #         'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']} 
# # # # df = pd.DataFrame(data) 
# # # # df['gender'] = ['m','f','m','f']
 
# # # # # Display the DataFrame 
# # # # print("DataFrame:") 
# # # # print(df)
# # # #   # Displaying first two rows and first two columns
# # # # import pandas as pd 
# # # # # Reading data from a CSV file 
# # # # df = pd.read_csv('data.csv') 
# # # # # Display the DataFrame 
# # # # print("DataFrame read from CSV:") 
# # # # print(df) 
# # # # # Writing data to a CSV file 
# # # # df.to_csv('output.csv', index=True) 
# # # # print("DataFrame written to CSV.") 

# # # # import numpy as np 
# # # # import matplotlib.pyplot as plt 
# # # # xpoints = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125]) 
# # # # ypoints = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330]) 
# # # # plt.plot(xpoints, ypoints) 
# # # # plt.title("Sports Watch Data") 
# # # # plt.xlabel("Average Pulse") 
# # # # plt.ylabel("Calorie Burnage") 
# # # # plt.show() 
# # # # import matplotlib.pyplot as plt 
# # # # import numpy as np 
# # # # # xpoints = np.array([1, 2, 6, 8]) 
# # # # # ypoints = np.array([3, 8, 1, 10]) 
# # # # # plt.plot(xpoints)
# # # # # plt.plot(ypoints) 
# # # # # plt.show() import numpy as np 
# # # # # Generate random data for the histogram 
# # # # data = np.random.randn(10) 
# # # # # Plotting a basic histogram 
# # # # plt.hist(data,edgecolor='black') 
# # # # # Adding labels and title 
# # # # plt.xlabel('Values') 
# # # # plt.ylabel('Frequency') 
# # # # plt.title('Basic Histogram') 
# # # # # Display the plot 
# # # # plt.show() 

# # # import matplotlib.pyplot as plt

# # # # Define the coordinates
# # # x = [0,0]
# # # y = [6,250]

# # # # Plot the lines connecting the points
# # # plt.plot(x, y, marker='o', linestyle='-', color='blue')

# # # # Annotate each point
# # # # for i in range(len(x)):
# # # #     plt.text(x[i], y[i], f'({x[i]}, {y[i]})', fontsize=9, ha='right')

# # # # Label axes and show grid
# # # plt.xlabel("X-axis")
# # # plt.ylabel("Y-axis")
# # # plt.title("Line Connecting Points") 
# # # plt.grid(True)
# # # plt.axhline(0, color='black', linewidth=0.5)  # X-axis line
# # # plt.axvline(0, color='black', linewidth=0.5)  # Y-axis line

# # # # Show the plot
# # # plt.show()
# # # import matplotlib.pyplot as plt

# # # # Coordinates of the points
# # # x = [0, 6]
# # # y = [0, 250]

# # # # Plotting the line
# # # plt.plot(x, y, marker='o', linestyle='-', color='green')

# # # # Annotate the points
# # # plt.text(0, 0, '(0, 0)', fontsize=9, ha='right')
# # # plt.text(6, 250, '(6, 250)', fontsize=9, ha='left')

# # # # Set up labels and title
# # # plt.xlabel("X-axis")
# # # plt.ylabel("Y-axis")
# # # plt.title("Line from (0, 0) to (6, 250)")
# # # plt.grid(True)

# # # # Draw axes lines
# # # plt.axhline(0, color='black', linewidth=0.5)
# # # plt.axvline(0, color='black', linewidth=0.5)

# # # # Show plot
# # # plt.show()
# # # import numpy as np
# # # arr = np.random.randint(10, 50,size=(5))
# # # print("Random array:", arr)
# # # global_variable = "I am global" 
# # # def outer_function(): 
# # #     # Enclosing scope 
# # #     enclosing_variable = "I am in the enclosing scope" 
# # #     def inner_function(): 
# # #         # Local scope 
# # #         local_variable = "I am in the local scope" 
# # #         print(local_variable) 
# # #         print(enclosing_variable) 
# # #         print(global_variable) 
# # #         print(len(global_variable))  # Using a built-in function 
# # #     inner_function() 
# # # outer_function()

# # def add(x, y): 
# #     return x + y  
# # def sub(x, y): 
# #      return x - y  
# # def mult(x, y): 
# #      return x * y  
# # def div(x, y): 
# #     if y != 0: 
# #         return x % y 
# #     else: 
# #         return "Error! Division by zero." 
# #     print("Select operation:") 
# # print("1. Add") 
# # print("2. Subtract") 
# # print("3. Multiply") 
# # print("4. Divide") 
# # choice = input("Enter choice (1/2/3/4): ") 
# # num1 = float(input("Enter first number: ")) 
# # num2 = float(input("Enter second number: ")) 
# # if choice == '1': 
# #     print(num1, "+", num2, "=", add(num1, num2)) 
# # elif choice == '2': 
# #     print(num1, "-", num2, "=", sub(num1, num2)) 
# # elif choice == '3': 
# #     print(num1, "*", num2, "=", mult(num1, num2)) 
# # elif choice == '4': 
# #     print(num1, "%", num2, "=", div(num1, num2)) 
# # else: 
# #     print("Invalid input. Please enter a valid choice.") 
# # def HCF(num1, num2): 
# #     while num2: 
# #         num1, num2 = num2, num1 % num2 
# #     return abs(num1) 
# # # Example usage: 
# # number1 = 24 
# # number2 = 36 
# # result =  HCF (number1, number2) 
# # print(f"The HCF of {number1} and {number2} is {result}") 
# # Function to compute LCM
# def find_lcm(x, y):
#     if x > y:
#         greater = x
#     else:
#         greater = y

#     while True:
#         if (greater % x == 0) and (greater % y == 0):
#             return greater
#         greater += 1

# # Input from user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# # Call the function and print result
# lcm = find_lcm(num1, num2)
# print("LCM of", num1, "and", num2, "is:", lcm)
with open('p.txt', 'w') as file:
    file.write("My name")
    file.write("Father name")
with open('p.txt', 'r') as file:
    content = file.read()
    print(content)