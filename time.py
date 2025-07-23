import time

def enter(work) :
    input( "write"  + work +  "to continue..." )
    
    
def slow_print(text, delay=0.08):
       for char in text:
             print(char, end='', flush=True)
             time.sleep(delay)
       print()
       
def design():       
       print("-------*°•_*°*°•_*°•_*°•_*°•_*°•*°•_*°•_*°•_*°•_*°•_*°•_-------")

design()       
slow_print("beep! beep! beep!.......")
slow_print ("welcome user!!!! 🥳 you have entered the world of mythical adventures🌲✨🔮🧙‍♂️")
slow_print ("your current location is in the middle of evergreen forest♻️🍃")
time.sleep(1)

enter(" enter ")

slow_print("You look around the area and find a tree with weird fruit🍇🍈🍉🥝🥑")
slow_print ("Your hunger gives you three choices🤤")
slow_print ("choice-1: eat the fruit")
slow_print ("choice-2: observe the fruit")
slow_print ("choice-3: don't eat and keep looking around")
time.sleep(1)

fruit = input ("enter your choice: (1/2/3) ")

if fruit == "1":
   slow_print("you've eaten a poisonous fruit. you died💀")
   slow_print("GAME OVER!!!")
   design()
   
elif fruit == "2":
    slow_print ("You've observed the fruit closely and found some old fruit eaten by birds, indicating the fruit is safe to eat")
    slow_print ("You've eaten the fruit and satisfied your hunger")
    
elif fruit == "3":
    slow_print ("You've refused to eat tge fruit and found nothing else to consume as result you suffered death by starvation💀")
    slow_print ("GAME OVER!!!")
    design()

else:
    slow_print("Invalid choice.Try again")


