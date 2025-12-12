# simple calculator in python :-

print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
choice = int(input("enter an operation from above  : "))

if(choice in [1,2,3,4]):
  num1 = float(input("enter first number : "))
  num2 = float(input("enter second number : "))
  if(choice==1):
        result= num1 +num2
        print("the addition is : ", result)
  elif(choice==2):
        result= num1 -num2
        print("the subtraction is : ", result)
  elif(choice==3):
        result= num1 *num2
        print("the multiplication is : ", result)
  elif(choice==4):
        result= num1 /num2
        print("the division is : ", result)


else:
    print("invalid operation") 
