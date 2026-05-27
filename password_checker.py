import re
common_passwords =["123456","password","admin"]
passwords = (input("enter password:"))
score = 0
if passwords.lower() in common_passwords:
    print("Very weak password")
    print("Reason: commonly used password")
    exit()
if len(passwords)>=8:
    score +=1
if re.search(r"[A-Z]",passwords):
    score +=1
if re.search(r"[a-z]",passwords):
    score +=1    
if re.search(r"[0-9]",passwords):
    score +=1
print("\nPassword Analysis Result" )
if score ==5:
    print("Strength:Strong password")
    print("Estimated crack time :years")
elif score >=3:
    print("Strenth:Medium password") 
    print("Estimated crack time:few days")
else :
    print("Strength:weak password")
    print("Estimated crack time :few minutes")
print("\nSuggestion:")                        
if len(passwords)<8:
    print("-use at least 8 characters")
if not re.search(r"[A-Z]", passwords):
    print("-Add uppercase letters")
if not re.search(r"[0-9]",passwords) :       
    print("-Add numbers")
if not re.search(r"[@#$%*^]",passwords):
    print("-Add special characters")    