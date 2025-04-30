#This game is Snake Water Gun

import random

comp_choice = random.choice([-1, 0, 1])
p_choice = input("Enter your choice (s for Snake, w for Water and g for Gun) : ")

if p_choice  not in ["s","w","g"]:
    print("Something went wrong!!!")

else:
    game_dict = {"s": -1,
                "w": 0,
                "g":1}

    rev_dict = {-1: "Snake",
                0 : "Water",
                1 : "Gun"}

    num_player = game_dict[p_choice]
    player_choice = game_dict[p_choice]

    print(f"You chose {rev_dict[num_player]}")
    print(f"Computer chose {rev_dict[comp_choice]}")

    if comp_choice == player_choice:
        print("This is a Draw")

    elif (comp_choice == -1):
        if player_choice == 0:
            print("Computer Wins!")
        else:
            print("You Win!")

    elif (comp_choice == 0):
        if player_choice == -1:
            print("You Win!")
        else:
            print("Computer Wins!")

    elif(comp_choice == 1):
        if player_choice == -1:
            print("Computer Wins!")
        else:
            print("You Win!")
