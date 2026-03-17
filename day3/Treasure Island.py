print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("")

choice1 = input("You are at a crossroad. Type 'left' or 'right': ").lower()

if choice1 == "right":
    print("You walked into a trap.")
    print("Game Over.")

elif choice1 == "left":
    print("")
    print("You arrive at a river.")
    choice2 = input("Do you want to 'swim', 'wait', or look for a 'bridge'? ").lower()

    if choice2 == "swim":
        print("A crocodile attacks you.")
        print("Game Over.")

    elif choice2 == "bridge":
        print("You find an old bridge.")
        choice3 = input("Do you want to 'cross' it or go 'back'? ").lower()

        if choice3 == "cross":
            print("The bridge breaks and you fall.")
            print("Game Over.")

        elif choice3 == "back":
            print("You go back and wait for a boat.")
            print("A boat takes you to the island.")
            print("")
            print("On the island, you see a cave and a hut.")
            choice4 = input("Do you go to the 'cave' or the 'hut'? ").lower()

            if choice4 == "hut":
                print("A pirate in the hut catches you.")
                print("Game Over.")

            elif choice4 == "cave":
                print("Inside the cave, you find a locked stone door.")
                print("To open it, solve this puzzle:")
                print("What comes next? 2, 4, 6, 8, ?")
                puzzle1 = input("Your answer: ").lower()

                if puzzle1 == "10":
                    print("The stone door opens.")
                    print("")
                    print("You enter a room with 3 boxes: red, blue, and yellow.")
                    choice5 = input("Which box do you open? ").lower()

                    if choice5 == "red":
                        print("The box is full of snakes.")
                        print("Game Over.")

                    elif choice5 == "blue":
                        print("The box explodes with smoke.")
                        print("Game Over.")

                    elif choice5 == "yellow":
                        print("You found a golden key!")
                        print("")
                        print("Ahead, there are 3 doors: red, blue, and yellow.")
                        choice6 = input("Which door do you choose? ").lower()

                        if choice6 == "red":
                            print("The room is full of fire.")
                            print("Game Over.")

                        elif choice6 == "blue":
                            print("The room fills with water.")
                            print("Game Over.")

                        elif choice6 == "yellow":
                            print("The key fits!")
                            print("You find the treasure chest.")
                            print("You Win!")

                        else:
                            print("That door does not exist.")
                            print("Game Over.")

                    else:
                        print("That box does not exist.")
                        print("Game Over.")

                else:
                    print("Wrong answer. The stone door stays locked.")
                    print("Game Over.")

            else:
                print("That place does not exist.")
                print("Game Over.")

        else:
            print("Invalid choice.")
            print("Game Over.")

    elif choice2 == "wait":
        print("A boat takes you safely to the island.")
        print("")
        print("On the island, you see a cave and a hut.")
        choice4 = input("Do you go to the 'cave' or the 'hut'? ").lower()

        if choice4 == "hut":
            print("A pirate in the hut catches you.")
            print("Game Over.")

        elif choice4 == "cave":
            print("Inside the cave, you find a locked stone door.")
            print("To open it, solve this riddle:")
            print("I have keys but no locks. I have space but no room.")
            puzzle2 = input("What am I? ").lower()

            if puzzle2 == "keyboard":
                print("Correct! The stone door opens.")
                print("")
                print("You see 3 doors: red, blue, and yellow.")
                choice5 = input("Which door do you choose? ").lower()

                if choice5 == "red":
                    print("The room is full of fire.")
                    print("Game Over.")

                elif choice5 == "blue":
                    print("The room fills with water.")
                    print("Game Over.")

                elif choice5 == "yellow":
                    print("You enter the final room.")
                    print("One last puzzle appears:")
                    print("What is 5 + 3?")
                    puzzle3 = input("Your answer: ").lower()

                    if puzzle3 == "8":
                        print("The treasure chest opens.")
                        print("You Win!")
                    else:
                        print("Wrong answer.")
                        print("Game Over.")

                else:
                    print("That door does not exist.")
                    print("Game Over.")

            else:
                print("Wrong answer.")
                print("Game Over.")

        else:
            print("That place does not exist.")
            print("Game Over.")

    else:
        print("Invalid choice.")
        print("Game Over.")

else:
    print("Invalid choice.")
    print("Game Over.")
