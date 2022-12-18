import random
game=True
while game==True:
    Num1=int(input("Choose one of the following:1 Rock,2 Paper,or 3 Scissors:")
    Num2=random.randint(1,3)
    if Num2==1:
        print("Computer choose Rock")
    elif Num2==2:
        print("Computer choose Paper")
    else:
        print("Computer choose Scissors")
    if Num1==Num2:
        print("It is a draw")
    elif Num1==1 and Num2==3:
        print("You win!")
    elif Num1==2 and Num2==1:
        print("You win!")
    elif Num1==3 and Num2==2:
        print("You win!")
    else:
        print("Computer wins")
    text=input("Play again? Y/N:")
    if text!="Y":
        game=False
