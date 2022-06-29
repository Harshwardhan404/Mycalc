#creating a calculator which takes 2 numbers from user and returs the output after performing calculations

print("Welcome to Mycalc")
print("To Add no1 and no2 press 1 ")
print("To Subtract no1 and no2 press 2 ")
print("To Multiply no1 and no2 press 3 ")
print("To Divide no1 and no2 press 4 ")
x = int(input("Enter your first number - "))
z = input("Enter the number of operation-")
y = int(input("Enter your second number - "))


#function to add two numbers
def funadd(): 
    print("The Addition of Number 1 and Number 2 is :-", x + y)

if z== '1':
   funadd()
   if z != '1':
    print("Wrong input")
   

#function to subtract two numbers
def funsub():
    print("The Substraction of Number 1 and Number 2 is :-", x-y)

if z== '2':
   funsub()
   if z != '2':
      print("Wrong input")

#function to Multiply two numbers
def funmul():
    print("The Multiplication of Number 1 and Number 2 is :-", x*y)

if z== '3':
   funmul()
   if z != '3':
      print("Wrong input")     

#function to Divide two numbers
def fundiv():
    print("The Dividation of Number 1 and Number 2 is :-", x/y)

if z== '4':
   fundiv()
   if z != '4':
      print("Wrong input")