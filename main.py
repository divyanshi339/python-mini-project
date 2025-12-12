# RULE BASED AI CHATBOT

import datetime
import time

name = input("hiee..!! please enter your name : ")
presenthour=datetime.datetime.now().hour

if 5<=presenthour<=12 :
    print(f"GOOD MORNING {name}...!! Hope you have a beautiful morning.")
    
elif 12<=presenthour<=15:
    print(f"GOOD AFTERNOON {name}...!! Hope you have a beautiful afternoon.")

elif 16<=presenthour<=20 :
    print(f"GOOD EVENING {name}...!! Hope you have a beautiful evening.")

else:
    print(f"GOOD NIGHT {name}...!! Hope you have a beautiful night.") 
time.sleep(1)
print("=== WELCOME TO YOUR RULE BASED CHATBOOT ===")       

responses = {
    "hello":"hi there !! How can i assist you ?",
    "how are you":" I'am doing great !! thanks for asking ,what about you ?",
    "i am fine":"Nice to hear that !! How can i help you ?",
    "your name":"I'am chatbuddy your rule based AI chatboot.",
    "who created you":"I am simply created by python through divyanshi.",
    "what are you doing":"just chatting with you .",
    "motivate me":"KEEP GOING, every bug of your code making you better developer."
}    

# function to get response 
def getresponses(userquestion):
   for eachkey in responses:
      if eachkey in userquestion:
          time.sleep(1)
          return responses[eachkey]
      
   return"chatbot response : SORRY , I didn't get that ,Ask me something else  !!"
          
# calling 

while True:
    userinput=input("Please ask me your question..?") 
    reply=getresponses(userinput)
    print("chatbot response :",reply)  

    if "exit" in userinput:
     print("thankyou for using chatbot---)")
     break 
