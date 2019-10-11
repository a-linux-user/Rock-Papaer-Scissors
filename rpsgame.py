# Rock, Paper, Scissors game
# rock blunts scissors
# scissors cut paper
# paper cover rock
# Define options: 
# 1 = Rock, 2 = Paper, 3 = Scissors

from random import randint

# function to determine the winner:

def winner(player,  computer):
     # args should be two integers, each 1, 2 or 3
    if player==computer:
         print("Draw! Play again.")
    elif player==1 and computer==2:
         print("Rock blunts scissors. You Win! :)")
    elif player==1 and computer==3:
        print("Rock covered by scissors. You loose :( Try again!")
    elif player==2 and computer==1:
        print("Paper covers rock. You Win! :)" )
    elif player==2 and computer==3:
        print("Paper cut by scissors. You loose :( Try again!")
    elif player==3 and computer==1:
        print("Scissors blunt by rock. You loose :( Try again!")
    elif player==3 and computer==2:
        print("Scissors cut paper! You Win! :)")

def convert_to_string(turn_int):
    turn_string=""
    if turn_int == 1:
        turn_string = "Rock"
    elif turn_int == 2:
        turn_string = "Paper"
    elif turn_int ==3:
        turn_string = "Scissors"    
    
    return turn_string
        

def main():
    while (True):
        # user plays:
        player_input = input("\n Rock (1), Paper (2), or Scissors (3)?")
        try:
            turn = int(player_input)
        except:
            print("Make sure you enter a number between 1 and 3!")  
            continue
        if turn<1 or turn>3:
            print("Make sure you enter a number between 1 and 3!")
            continue
            
        # computer plays:
        computer = randint(1, 3)
        
        computer_string = convert_to_string(computer)
        turn_string = convert_to_string(turn)
        print("You played %s, computer played %s." % (turn_string,  computer_string))
        
        winner(turn,  computer)
        
main() 
