# Add to number
a,b=10,5
sum=a+b
print(sum)
#maximum of two numbers
a,b=10,15
if a>b:
    print("a is greater than b ")
else:
    print("b is greater than a")
#factorial of a number
n=5
for i in range(1, 6):
    if i==1:
        fact=1
    else:
        fact=fact*i
        print(fact)
#simple interest
p,r,t=10000,10,5
si=(p*r*t)/100
print("Simple Interest is:", si)
#Armstrong number
num=1634
sum=0
temp=num
order = len(str(num))
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
if sum==num:    
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
#Fibonacci series
n = 10  
a, b = 0, 1
print("Fibonacci series:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b

#ASCII Value of a character
char = 'A'
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is {ascii_value}")
#Reverse a string
string = "Hello, World!"
reversed_string = string[::-1]
print(f"The reversed string is: {reversed_string}") 
#something
for _ in range(3):
    print("Hello!")
#odd or even
num=15
even =(num%2==0)
print(f"the number is :{even}")
#largest of three number
a,b,c=10,14,1
if(a>b)&(a>c):
    print("a is the greatest")
elif(a<b)&(b>c):
    print("b is the greatest")
else:
    print("c is the gretest")
#multiplication table
num = 10
for i in range (11):
    Mul=num*i
    print(Mul)
#sum of all number in a list using loop
list=[10,20,30,40]
sum=0 
for num in list:
    sum+=num
print("the total is :", sum)   
#print 1 to 10 using while loop
i=10
while i<=10:
    print(i)
    i+=1
    #check vowels in a string
string = "Hello World"
vowels = "aeiouAEIOU"
count = 0 
for char in string:
    if char in vowels:
        count += 1
print(f"Number of vowels in the string: {count}")

#
country_capitals = { 
  "United States": "Washington D.C.",  
  "Italy": "Naples"  
} 
 
# print dictionary keys one by one 
for country in country_capitals: 
    print(country) 
print("----------") 
 
# print dictionary values one by one 
for country in country_capitals: 
    capital = country_capitals[country] 
    print(capital)
#function
    def greet():
        print("Hello, World!")
    greet()
#add to number
    def add_numbers(x,y):
        sum = x + y
        print(sum)
    add_numbers(10, 5)
#square of a number
    def square_number(num):
        result =num*num
        return result
    Square = square_number(5)
    print(Square) 
    #factorial of a number
    def factorial(n):
        if n==0 or n==1:
            return 1
        else:
            return n *factorial(n-1)
    num=5
    result = factorial(num)
    print(f"The factorial of {num} is {result}")

#questions 
'''Demonstrate five different built in functions used in the string. Write 
a program to check whether a string is a palindrome or not.'''
string = "hello world"
string_upper  = string.upper()
string_lower = string.lower()
string_capitalize = string.capitalize()
string_length = string.__len__()
print(string_upper)
print(string_lower)
print(string_capitalize)
print(string_length)
string_replace = string.replace("world", "Python")
print(string_replace)
# '''Write a program that accepts sequence of lines as input and prints the 
# lines after making all characters in the sentence capitalized. e.g. If 
# Input: Hello world Practice makes perfect Then, Output: HELLO 
# WORLD PRACTICE MAKES PERFECT'''
# String = input("enter a line : ")
# capitalized_string = String.upper()
# print(capitalized_string)    
# '''Write a python program to count the vowels present in a given input 
# string. Explain the output of the program through examples. '''
# input_string = input("Enter a string: ")
# vowels  = "aeiouAEIOU"
# count = 0
# for char in input_string:
#     if char in vowels :
#         count+=1
# print("Number of vowels in the string:", count)

# '''Write a Python program to change a given string to a new string where 
# the first and last chars have been exchanged. '''
# original_string = input("Enter a string: ")
# if len(original_string)>2:
#     new_string = original_string[-1] + original_string[1:-1]+original_string[0]
#     print("original string: ",original_string)
#     print("new string: ",new_string)
# else:
#     print("string is too short to exchange first and last characters.")
#methods of list
List_1 = [1,2,3,4,5,5,6]
List_2 = [7,8,9,10]
#concatination of two lists
list_concat= list_concat = List_1+List_2
print("Concatenated List:", list_concat)
#append an element to the list
List_1.append(6)
print("List after appending 6:", List_1)
#insert an element at a specific position
List_1.insert(2, 10)
print("List after inserting 10 at index 2:", List_1)
#remove an element from the list
List_1.remove(5)
print("List after removing 5:", List_1)
#pop an element from the list
popped_element = List_1.pop()
print("Popped element:", popped_element)
print("List after popping an element:", List_1)
#sort the list
List_1.sort()
print("Sorted List:", List_1)   
#reverse the list
List_1.reverse()
print("Reversed List:", List_1)
#count the occurrence of an element
count_of_5 = List_1.count(5)
print("Count of 5 in List_1:", count_of_5)  
#find the index of an element
index_of_3 = List_1.index(3)
print("Index of 3 in List_1:", index_of_3)
#copy the list
List_copy = List_1.copy()
print("Copied List:", List_copy)
#clear the list
List_1.clear()
print("List after clearing:", List_1)

#List Slicing 
lsit= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#slicing the list from index 2 to 5
sliced_list = lsit[2:6]
print("Sliced List from index 2 to 5:", sliced_list)
#slicing the list from index 0 to 4
sliced_list_2 = lsit[:5]

'''longest word in a list'''
words = ['apple','banana','mango']
longest_words = max(words,key= len)
print(longest_words)

#creating three dictiionaies and merging them
dict_1 = {'Person': "john",'Age':23}
dict_2 = {'City':'New York','Country': 'USA'}
dict_3 = {'Occupation': 'Engineer', 'Salary': 70000}
dict_4 ={**dict_1, **dict_2, **dict_3}
# print("Merged Dictionary:", dict_4)
# #files
# f = open("C:\Users\DELL\OneDrive\Desktop\kartik\example.txt", "r") 
# print(f.read()) 
#	Write a Python program that counts the frequency of each character in a string.
input_string = "hello world"
count =0
for char in input_string:
    if char.isalpha():  # Check if the character is an alphabet
        count += 1
        print(f"{count}: {char}")

#Create a Python program that removes duplicate elements from a list.
input_string = [1,1,1,1,2,33,2,5,55,5,6] 
mofdified_string =set(input_string)   # Convert the string to a set to remove duplicates
print(mofdified_string)

#sort a dictionary by its values? 
input_dict  = {'apple':3, 'banana':2, 'cherry':5}
sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[0]))
print(sorted_dict)
#Write a Python function that returns the longest word from a given list of words.
list = ['apple', 'banana', 'cherry', 'watermelon']
longest_words= max(list, key=len)
print(f"The longest word in the list is: {longest_words}")
#How can you check if a given key exists in a dictionary?
input_dict  = {'apple':3, 'banana':2, 'cherry':5}
key = 'MANGO'
if key in input_dict:
    print(f"The key '{key}' exists in the dictionary.")
else:
    print(f"The key '{key}' does not exist in the dictionary.")

#add, update, and delete key-value pairs in a dictionary?
input_dict = {'apple': 3, 'banana': 2, 'cherry': 5}
input_dict['orange']= 4
print("Dictionary after adding 'orange':", input_dict)
input_dict['banana'] = 6
print("Dictionary after updating 'banana':", input_dict)
input_dict.pop('cherry', None)
print("Dictionary after deleting 'cherry':", input_dict)
#Use a lambda function in Python to sort a list of tuples based on the second element of each tuple.
list_of_tuples = [(1, 3), (2, 1), (3, 2)]
sorted_list = sorted(list_of_tuples, key = lambda x:x[1])
print(sorted_list)
'''Write a Python program, which returns a list with 2-tuples.
Each tuple consists of the order number and the product of the price per item and the quantity.
The product should be increased by 10$ if the value of the order is smaller than 100$'''
list_of_orders =[(1234,99,1),(9876,100,2),(1235,5,3)]
for order in list_of_orders:
    order_number,price,quantity= order
    total = price*quantity
    if total <100:
        total += 10
    print(f"Order Number: {order_number}, Total: ${total}")

#Implement a Python function that takes a list of integers and returns a new list containing the squares of each number.
list =[10,12,9,3,2]
new_list = [x**2 for x in list]
print("Original List:", list)
print("List of Squares:", new_list)

#Create a Python function that accepts a string and returns the reverse of that string.
input_string= "Hello, World!"
reverse_string= input_string[::-1]
print("Original String:", input_string)
print("Reversed String:", reverse_string)
# how to read and print the content of a file?
# with open("example.txt",'r') as file:
#     content = file.read()
#     print("File Content:")  
#     print(content)
#create a program to copy the content of one file to another file.
file_1 = "example.txt"
file_2 = "copy_example.txt"
with open(file_1, 'r') as source_file:
    content = source_file.read()
    with open(file_2, 'w') as destination_file:
        destination_file.write(content)
        print(f"Content copied from {file_1} to {file_2} successfully.")

#output
l = [1, 0, 0, 2, 'hi', '', []]
print(list(filter(bool, l)))

        