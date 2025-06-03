#Basic While loop use for Basic ATM pin example
cpin = "0000"
attempt = 0 
while attempt < 3:
    pin = input("Enter Your pin:  ")
    if pin == cpin :
      print("Access Granted!")
      break 
    else : 
      print("Incorrect Pin")
      attempt += 1
      print()
      print(f"{3-attempt} Attempts Left!")

if attempt == 3 :
 print("Card Blocked!")
    
