import random
import time

def slow_print(text, delay=0.08):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
def design():       
       print("-------*°•_*°*°•_*°•_*°•_*°•_*°•*°•_*°•_*°•_*°•_*°•_*°•_-------")
       
def play():
        user = input (" 'r' for rock, 'p' for paper, 's' for scissors.....").lower()
        options = ['r' , 'p' , 's']
        if user not in options:
            return "invalid choice. Try again🥺"
        
        system = random.choice(options)
        print(f"opponent chooses: {system}")
        
        if user == system:
            return "it's a tie🫢!!"
        elif user =="r" and system =="p":
               return "oh no! 😛 you lost"
        elif user =="r" and system =="s":
               return "yayyyy!! you won🥳"
        elif user =="p" and system =="r":
               return "yayyyy!! you won🥳"
        elif user =="p"and system =="s":
               return "oh no! 😛 you lost"
        elif user =="s"and system =="r":
               return "oh no! 😛 you lost"
        elif user =="s"and system =="p":
               return "yayyy!! you won🥳"  

design()        
slow_print("welcome to the game of rock✊ paper🖐️ and scissors✌️. Make ur choice to play🗣️❤️‍🔥")

slow_print(play())

slow_print("do you wanna play again.....?🎮")
again= input ("yes/no......").lower()
if again not in["yes", "no"]:
    slow_print("invalid command❌")

while again == "yes":
        slow_print(play())
        slow_print("do you wanna play again.....🎮?")
        again= input ("yes/no......").lower()
        if again not in["yes", "no"]:
           slow_print("invalid command❌")
if again== "no":
    slow_print("thank you! for playing💕")
    print("-------*°•_*°*°•_*°•_*°•_*°•_*°•*°•_*°•_*°•_*°•_*°•_*°•_-------")

