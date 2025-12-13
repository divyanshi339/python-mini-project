# CREATE A CONTACT BOOK :

print("------WELCOME TO CONTACT BOOK------")
contactlist=[]

while True:
    print("====== MENU ======")
    print("1. Add contact ")
    print("2. view all contact")
    print("3. search by name")
    print("4. delete contact ")
    print("5. exit")

    Choice = int (input("Enter your choice : "))

# ADD CONTACT

    if(Choice==1):
        name=input("enter name :")
        number=int(input("enter phone number :"))
        Email=input("enter email :")

        contact={
            "name":name,
            "number":number,
            "Email":Email,
        }

        contactlist.append(contact)
        print("=== CONTACT  ADDED SUCCESSFULLY===")


# VIEW CONTACT
    elif(Choice==2):
        
        if(len(contactlist)==0):
          print("NO contact") 
        else:
          print("YOUR CONTACT ")
          count=1
          for eachcontact in contactlist:
            print(f"Contact number {count} : NAME : {eachcontact["name"]}  NUMBER : {eachcontact["number"]} EMAIL : {eachcontact["Email"]}")
            count=count+1  

# SEARCH CONTACT
    elif(Choice==3):
       search_name=input("enter name to be search :")
       for eachcontact in contactlist:
          if contact["name"]==search_name:
            print("contact found successfully :")
            print(f" Name : {contact["name"]}")
            print(f" Number : {contact["number"]}")
            print(f" Email : {contact["Email"]}")
          else:
              print("No contact found ")
                   

# DELETE CONTACT 

    elif(Choice==4):
       delete_name=input("enter contact name to be deleted :").lower() 
       for eachcontact in contactlist:
          if contact["name"] ==delete_name:
           contactlist.remove(contact)  
           print("contact deleted successfully ") 
# EXIT
    else:
       if(Choice==5):
          print("THANKYOU FOR USING IT :")
       else:
          print("Invalid choice ! please try again")



                