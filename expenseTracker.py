# expense tracker ----

print("------WELCOME TO EXPENSE TRACKER ------")
expenselist=[]

while True:
    print("====== MENU ======")
    print("1. Add expenses ")
    print("2. view all expenses")
    print("3. view total expense")
    print("4. exit ")

    Choice = int (input("Enter your choice : "))

# ADD EXPENSES :
    if(Choice==1):
        date = input("In which date you have expend money : ")
        category = input("In what you have expend your money :")
        description = input("Detail about your expenditure :")
        amount = float(input("Total amount of your expenses :"))

        expense ={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount,
        }
        expenselist.append(expense)
        print(" \n DONE YOUR EXPENDITURE IS ADDED ---")
        
# VIEW ALL EXPENSES :
    elif(Choice==2):
        if(len(expenselist)==0):
          print("NO expenditure") 
        else:
          print("YOUR EXPENSES ")
          count=1
          for eachexpense in expenselist:
            print(f"Expenditure number {count} : {eachexpense["date"]},{eachexpense["category"]},{eachexpense["description"]},{eachexpense["amount"]}")
            count=count+1

# VIEW TOTAL AMOUNT :
    elif(Choice==3):
        total=0
        for eachexpense in expenselist:
           total = total + eachexpense["amount"]
        print("\n YOUR TOTAL AMOUNT OF EXPENDITURE IS = ",total)

# EXIT:
    elif(Choice==4):
       print("\n THANYOU FOR USING EXPENSE TRACKER " )           
       break
    else:
       print("INVALID CHOICE")     



