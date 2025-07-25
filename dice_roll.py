import random

def roll():
    user = input ("enter 'r' to roll the dice!......")
    if user != 'r' :
        return "invaild choice."
        
    system = random.choice([1, 2, 3, 4, 5, 6])
    print(f"you rolled a...: {system}")
    
    
roll()