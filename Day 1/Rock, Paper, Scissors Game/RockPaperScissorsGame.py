import random

dic = {
    1:"Rock",
    2:"Scissors",
    3:"Paper"
}
ai_choice = random.randrange(1,3)
print(ai_choice)

print("Rock, Paper, Scissors Game!")
print("Make your choice below")

pl_choice = int(input("Type 1 for rock, 2 for scissors, or 3 for paper: "))

if pl_choice == ai_choice:
    print("You choose: " + dic[pl_choice] + "| Your opponent choose: " + dic[ai_choice])
    print("TIE")
elif pl_choice == 1 and ai_choice == 2:
    print("You choose: " + dic[pl_choice] + "| Your opponent choose: " + dic[ai_choice])
    print("YOU WIN")
elif pl_choice == 1 and ai_choice == 3:
    print("You choose: " + dic[pl_choice] + "| Your opponent choose: " + dic[ai_choice])
    print("YOU LOSE")
elif pl_choice == 2 and ai_choice == 1:
    print("You choose: " + dic[pl_choice] + "| Your opponent choose: " + dic[ai_choice])
    print("YOU LOSE")
elif pl_choice == 2 and ai_choice == 3:
    print("You choose: " + dic[pl_choice] + "| Your opponent choose: " + dic[ai_choice])
    print("YOU WIN")
elif pl_choice == 3 and ai_choice == 1:
    print("You choose: " + dic[pl_choice] + "| Your opponent choose: " + dic[ai_choice])
    print("YOU WIN")
elif pl_choice == 3 and ai_choice == 2:
    print("You choose: " + dic[pl_choice] + "| Your opponent choose: " + dic[ai_choice])
    print("YOU LOSE")