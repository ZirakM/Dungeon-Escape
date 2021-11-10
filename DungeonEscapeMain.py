# -------------------------------------------------------------------------------
# Purpose:     This is a text based adventure game that takes the player through
#              many obstacles and events, with the player's main objective being
#              trying to escape from a dungeon full of dangerous creatures.

# Author:      Zirak Mughal

# Created:     11/09/2021
# -------------------------------------------------------------------------------

# While loop to restart game if player wishes to play again.
while True:

    # Importing sys module to utilize sys exit() function to end game when player loses all of their health.
    # Importing time module to utilize sleep() function to delay execution of code

    import sys
    import time

    # Setting variables for player's score and health.
    score = 0
    health = 100

    # Asking the user for his/her name.
    name = input("What is your name? ")
    name = (str(name))
    print("--------------------------------------------------------------------------")

    # Welcoming the user to the game.
    print("Welcome " + name + "! You are now playing DUNGEON ESCAPE.")
    print("--------------------------------------------------------------------------")

    time.sleep(2)

    # Introducing the game's story to the user.
    print("")
    print("You are a prisoner in a dungeon full of dangerous creatures.")
    print("")
    print("Your main objective is to escape the dungeon.")
    print("")
    print("")

    # Part 1/7
    time.sleep(3)

    print("You wake up in the middle of the night and discover that the lock on your")
    print("cell is slightly bent, and that there may be a way to open it.")
    print(" ")

    time.sleep(3)

    print("The other prisoners and the guards are still fast asleep.")
    print(" ")

    time.sleep(2)

    print("In your cell, there is a large boulder and a piece of cloth.")
    print(" ")

    # Asking the user to select an option as an answer for Part 1/7.
    time.sleep(2)

    print("-----------------------------------------------")
    print("Select the most efficient way to open the lock.")
    print("-----------------------------------------------")
    print(" ")

    time.sleep(1)

    print("1. Use your hands to fidget with the lock and open it.")
    print("2. Use the piece of cloth to slowly tug on the lock and open it.")
    print("3. Take the boulder and smash it on the lock to open it.")
    print(" ")
    print(" ")

    part1 = input("Please enter a number as your answer. (1, 2, or 3) ")

    num = False

    while not num:
        try:
            part1 = (int(part1))
            if part1 > 3 or part1 < 1:
                print("Invalid Input")
                part1 = input("Please enter a number as your answer. (1, 2, or 3) ")
            else:
                num = True
        except:
            print("Invalid Input")
            part1 = input("Please enter a number as your answer. (1, 2, or 3) ")

    # Outputting the result of the user's answer for Part 1/7
    if part1 == 1:
        print("")
        print("")
        print("You get the lock to open, but not in the most efficient way.")
        print("The lock also injures your hands.")
        print("You lose 10 health points.")
        health -= 10
        print("You gain 10 points.")
        score += 10

    elif part1 == 2:
        print("")
        print("")
        print("You get the lock to open, and you do so in the most efficient way.")
        print("You gain 20 points.")
        score += 20

    elif part1 == 3:
        print("")
        print("")
        print("You get the lock to open, but you almost wake up the guards!")
        print("The boulder also partially lands on your foot.")
        print("You lose 30 health points.")
        health -= 30
        print("You gain 0 points.")
        score += 0

    # Part 2/7
    time.sleep(4)

    print(" ")
    print("...")
    print(" ")

    time.sleep(1)

    print("You continue walking through a dimly lit hallway and find three,")
    print("large doors.")
    print(" ")

    # Asking the user to select an option as an answer for Part 2/7.
    time.sleep(2)

    print("-----------------------------------------------")
    print("Select the door you choose to enter.")
    print("1. Door #1")
    print("2. Door #2")
    print("3. Door #3")
    print("-----------------------------------------------")
    print(" ")

    time.sleep(1)
    part2 = input("Please enter a number as your answer. (1, 2, or 3) ")

    num = False

    while not num:
        try:
            part2 = (int(part2))
            if part2 > 3 or part2 < 1:
                print("Invalid Input")
                part2 = input("Please enter a number as your answer. (1, 2, or 3) ")

            else:
                num = True
        except:
            print("Invalid Input")
            part2 = input("Please enter a number as your answer. (1, 2, or 3) ")

    # Outputting result of the user's answer for Part 2/7
    if part2 == 1:
        print("")
        print("")
        print("You enter the doorway and fall into a well.")
        print("You lose 30 health points.")
        print("You gain 0 points.")
        print(" ")
        health -= 30
        score += 0
        time.sleep(2)
        print("There is a small light coming from a crack in the wall, big enough for")
        print("you to fit through.")
        print("You enter through the crack and end up in a room with a lit fireplace,")
        print("wooden table, and piece of cheese.")

    elif part2 == 2:
        print("")
        print("")
        print("The door is hard to push and takes a lot of physical strength.")
        print("You lose 15 health points.")
        health -= 15
        time.sleep(2)
        print(" ")
        print("You push hard enough and end up in a room with a lit fireplace,")
        print("wooden table, and piece of cheese.")
        print("You gain 10 points.")
        score += 10

    elif part2 == 3:
        print("")
        print("")
        print("You open the door and make your way through.")
        print("You gain 20 points.")
        print(" ")
        score += 20
        time.sleep(2)
        print("You end up in a room with a lit fireplace, wooden table, and")
        print("piece of cheese.")

    else:
        print("That is an Invalid Input!")

    # Part 3/7
    time.sleep(2)

    print(" ")
    print("You pick up the piece of cheese and observe it.")
    print(" ")
    print("The cheese is slightly mouldy, but you are very hungry.")
    print(" ")

    # Asking the user to select an option as an answer for Part 3/7.
    time.sleep(4)

    print("--------------------------------------------------------------------------")
    print("What do you want to do with the cheese?")
    print(" ")
    print("1. Eat it.")
    print("2. Put it in your pocket and save it for later.")
    print("3. Put it back on the table where you found it.")
    print("--------------------------------------------------------------------------")
    print(" ")
    part3 = input("Please enter a number as your answer. (1, 2, or 3) ")
    print(" ")
    num = False

    while not num:
        try:
            part3 = (int(part3))
            if part3 > 3 or part3 < 1:
                print("Invalid Input")
                part3 = input("Please enter a number as your answer. (1, 2, or 3) ")
                print(" ")

            else:
                num = True
        except:
            print("Invalid Input")
            part3 = input("Please enter a number as your answer. (1, 2, or 3) ")
            print(" ")

    # Outputting the result of the user's answer for Part 3/7
    if part3 == 1:
        print("You eat the cheese and it instantly upsets your stomach.")
        print("You lose 30 health points.")
        health -= 30
        print("You gain 0 points.")
        print(" ")
        score += 0

    elif part3 == 2:
        print("You put the cheese in your pocket to save for later.")
        print("The smell of the cheese slightly intoxicates you.")
        print("You lose 10 health points.")
        health -= 10
        print("You gain 10 points.")
        score += 10

    elif part3 == 3:
        print("You put the cheese back on the table where you found it.")
        print("You gain 20 points.")
        score += 20

    else:
        print("That is an Invalid Input.")

    print(" ")
    print(" ")

    # RANDOM EVENT 1/3
    time.sleep(3)

    from random import randint
    randomevent1 = (randint(1, 3))
    if randomevent1 == 1:
        print("All of a sudden, twenty bats fly out of the ceiling and attack you.")
        print("You lose 10 health points.")
        health -= 10
        print("You gain 0 points.")
        score += 0
        if health <= 0:
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again? (Yes or No) ")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again? (Yes or No) ")

    elif randomevent1 == 2:
        print("You find a magical healing potion and drink it.")
        print("You gain 30 health points.")
        health += 30
        print("You gain 10 points.")
        score += 10
        if health <= 0:
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again? (Yes or No ")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again? (Yes or No ")

    else:
        print("You find a perfectly good apple and decide to eat it.")
        print("You gain 10 health points.")
        health += 10
        print("You gain 5 points.")
        score += 5
        if health <= 0:
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again?")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again?")

    # Part 4/7
    time.sleep(3)

    print(" ")
    print(" ")
    print("You hear two guards coming down the hallway.")
    print(" ")

    # Asking the user to select an option as an answer for Part 4/7.
    time.sleep(4)

    print("--------------------------------------------------------------------------")
    print("What do you do next?")
    print(" ")
    print("1. Hide underneath the table and hope that the guards don't see you as")
    print("   they pass by the room.")
    print("2. Try to make a run for it and exit the room before the guards see you.")
    print("3. Give up and allow the guards to find you.")
    print("--------------------------------------------------------------------------")
    print(" ")
    part4 = input("Please enter a number as your answer. (1, 2, or 3) ")
    num = False

    while not num:
        try:
            part4 = (int(part4))
            if part4 > 3 or part4 < 1:
                print("Invalid Input")
                part4 = input("Please enter a number as your answer. (1, 2, or 3) ")

            else:
                num = True
        except:
            print("Invalid Input")
            part4 = input("Please enter a number as your answer. (1, 2, or 3) ")

    # Outputting the result of the user's answer for Part 4/7
    if part4 == 1:
        print(" ")
        print("The guards pass by the room and don't suspect a thing.")
        print("You gain 20 points")
        score += 20
        if health <= 0:
            print(" ")
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again? (Yes or No ")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again? (Yes or No")

    elif part4 == 2:
        print(" ")
        print("The guards spot you running away and shoot an arrow at you.")
        print("You lose 100 health points.")
        health -= 100
        print("You gain 0 points.")
        if health <= 0:
            print(" ")
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again? (Yes or No) ")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again? (Yes or No) ")
    elif part4 == 3:
        print(" ")
        print("The guards find you and kill you on the spot.")
        print("You lose 100 health points.")
        health -= 100
        print("You gain 0 points.")
        if health <= 0:
            print(" ")
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again? (Yes or No) ")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again? (Yes or No) ")

    else:
        print("That is an Invalid Input!")

    # Part 5/7
    time.sleep(3)

    print(" ")
    print(" ")
    print("...")

    time.sleep(1)

    print(" ")
    print(" ")
    print("You exit the room and enter the hallway that the guards were walking")
    print("through.")
    print(" ")
    print(" ")

    # RANDOM EVENT 2/3
    time.sleep(1)

    randomevent2 = (randint(1, 3))
    if randomevent2 == 1:
        print("You find a dagger!")
        print("You gain 10 points.")
        score += 10

    elif randomevent2 == 2:
        print("You find a sword!")
        print("You gain 15 points.")
        score += 15

    else:
        print("You find a metal flail!")
        print("You gain 20 points.")
        score += 20

    print(" ")
    print(" ")

    # Part 5/7 Continued
    time.sleep(3)

    print("You make your way down the hallway and it ends at an intersection.")
    print(" ")
    print("There is a large, arrow shooting statue with red glowing eyes seperating")
    print("you from the other side of the hallway.")
    print(" ")
    print(" ")

    # Asking the user to select an option as an answer for Part 5/7.
    time.sleep(3)

    print("--------------------------------------------------------------------------")
    print("How are you going to make it to the other side?")
    print(" ")
    print("1. Get on the floor and crawl to the other side. ")
    print("2. Run across as fast as you can and hope you don't get hit.")
    print("3. Run across while using your weapon to try and block the arrows.")
    print("--------------------------------------------------------------------------")
    print(" ")

    part5 = input("Please enter a number as your answer. (1, 2, or 3) ")
    print(" ")
    print(" ")
    num = False

    while not num:
        try:
            part5 = (int(part5))
            if part5 > 3 or part5 < 1:
                print("Invalid Input")
                part5 = input("Please enter a number as your answer. (1, 2, or 3) ")
            else:
                num = True
        except:
            print("Invalid Input")
            part5 = input("Please enter a number as your answer. (1, 2, or 3) ")

    # Outputting the result of the user's answer for Part 5/7
    if part5 == 1:
        print("You make it across without getting hit!")
        print("You gain 20 points.")
        score += 20
        if health <= 0:
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again? (Yes or No) ")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again? (Yes or No) ")

    elif part5 == 2:
        print("You make it across but get hit by an arrow.")
        print("You lose 40 health points.")
        health -= 40
        print("You gain 0 points.")
        score += 0
        if health <= 0:
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again? (Yes or No) ")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again? (Yes or No) ")

    elif part5 == 3:
        print("You make it across while only partially blocking the arrow that")
        print("shoots at you.")
        print("You lose 20 health points.")
        health -= 20
        print("You gain 10 points.")
        score += 10
        if health <= 0:
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again? (Yes or No) ")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again? (Yes or No) ")

    else:
        print("That is an Invalid Input!")

    print(" ")
    print(" ")

    time.sleep(3)

    print("...")
    print(" ")
    print(" ")

    # Part 6/7
    time.sleep(4)

    print("You walk down the second part of the hallway and find a cave entrance.")
    print("The cave entrance is blocked by a large wooden barrel.")
    print(" ")
    print(" ")

    # Asking the user to select an option as an answer for Part 6/7.
    print("--------------------------------------------------------------------------")
    print("How are you going to get past the wooden barrel?")
    print(" ")
    print("1. Grab it and climb over it.")
    print("2. Use your weapon to break it apart.")
    print("3. Use your strength to push it over.")
    print("--------------------------------------------------------------------------")
    print(" ")
    part6 = input("Please enter a number as your answer. (1, 2, or 3) ")
    num = False

    while not num:
        try:
            part6 = (int(part6))
            if part6 > 3 or part6 < 1:
                print("Invalid Input")
                part6 = input("Please enter a number as your answer. (1, 2, or 3) ")

            else:
                num = True
        except:
            print("Invalid Input")
            part6 = input("Please enter a number as your answer. (1, 2, or 3) ")

    print(" ")

    # Outputting the result of the user's answer for Part 6/7
    if part6 == 1:
        print(")You make it over the wooden barrel, but end up with many splinters")
        print("in your hand.")
        print("You lose 10 health points.")
        health -= 10
        print("You gain 10 points.")
        score += 10
        if health <= 0:
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again?")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again?")

    elif part6 == 2:
        print("You break apart the wooden barrel and 3 goblins pop out!")
        print("The goblins attack you and then run away.")
        print("You lose 30 health points.")
        health -= 30
        print("You gain 0 points.")
        score += 0
        if health <= 0:
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again?")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again?")

    elif part6 == 3:
        print("You manage to push the wooden barrel over into the cave entrance.")
        print("You gain 20 points.")
        score += 20
        if health <= 0:
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again?")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again?")

    else:
        print("That is an Invalid Input!")

    print(" ")
    print(" ")

    # Part 7/7
    time.sleep(3)

    print("...")
    print(" ")

    time.sleep(2)

    print("You enter the cave and find a fire breathing dragon inside.")
    print(" ")
    print("The fire breathing dragon is standing in front of a doorway that leads")
    print("to the exit of the dunegeon.")
    print(" ")
    print(" ")

    # RANDOM EVENT 3/3
    time.sleep(3)

    randomevent3 = (randint(1, 3))
    if randomevent3 == 1:
        print("The dragon starts breathing fire all over the cave.")
        print("You get slightly burnt from the fire.")
        print("You lose 20 health points.")
        health -= 20
        if health <= 0:
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again?")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again?")

    elif randomevent3 == 2:
        print("The dragon starts stomping on the the ground.")
        print("You lose your balance and fall over.")
        print("You lose 15 health points.")
        health -= 15
        if health <= 0:
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again?")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again?")

    else:
        print("The dragon loses balance and falls over.")
        print("You get startled and your heart almost stops.")
        print("You lose 5 health points.")
        health -= 5
        if health <= 0:
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again?")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again?")

    print(" ")
    print(" ")

    # Asking the user to select an option as an answer for Part 7/7.
    time.sleep(2)

    print("--------------------------------------------------------------------------")
    print("How are you going to get past the fire breathing dragon?")
    print(" ")
    print("1. Throw your weapon at it and try to slay it.")
    print("2. Run as fast as you can, through its legs, towards the doorway.")
    print("3. Slowly walk along the sides of the cave towards the doorway and hope")
    print("that it doesn't notice you.")
    print("--------------------------------------------------------------------------")
    print(" ")

    part7 = input("Please enter a number as your answer. (1, 2, or 3) ")
    num = False

    while not num:
        try:
            part7 = (int(part7))
            if part7 > 3 or part7 < 1:
                print("Invalid Input")
                part7 = input("Please enter a number as your answer. (1, 2, or 3) ")

            else:
                num = True
        except:
            print("Invalid Input")
            part7 = input("Please enter a number as your answer. (1, 2, or 3) ")

    print(" ")

    # Outputting the result of the user's answer for Part 7/7
    if part7 == 1:
        print("Your weapon slays the dragon and it falls to its death.")
        print(" ")
        print("You make it across, into the doorway leading towards the exit of the")
        print("dungeon.")
        print(" ")
        print("You gain 100 points")
        score += 100
        if health <= 0:
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again?")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again?")

    elif part7 == 2:
        print("You make it across, into the doorway leading towards the exit of the")
        print("dungeon, but the dragon breathes fire in your direction and severely")
        print("burns you.")
        print("You lose 60 health points.")
        health -= 60
        print("You gain 0 points")
        score += 0
        if health <= 0:
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again?")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again?")

    elif part7 == 3:
        print("The dragon notices you before you can make it across into the doorway")
        print("leading towards the exit of the dungeon.")
        print(" ")
        print("The dragon takes its foot and stomps on you.")
        print(" ")
        print("You lose 100 health points.")
        health -= 100
        print("You gain 0 points")
        score += 0
        if health <= 0:
            print("Game Over, you have no health remaining.")
            restart = input("Would you like to play again?")
            if restart == "Yes" or restart == "yes":
                continue
            elif restart == "No" or restart == "no":
                break
            else:
                print("That is an Invalid Input!")
                restart = input("Would you like to play again?")

    else:
        print("That is an Invalid Input!")

    print(" ")
    print(" ")

    # Ending the game and congratulating the user
    time.sleep(4)

    print("Congratulations " + name + ", you escaped the dungeon!")
    print(" ")

    # Displaying Points Scored and Remaining Health
    print("You ended off with " + str(health) + " health points remaining.")
    print("You scored a total of " + str(score) + " points!")

    print(" ")

    # Giving a unique message to the user depending on his/her number of points
    if score <= 50:
        print("You finished at PEASANT status.")

    elif 50 <= score <= 100:
        print("Nice job, you finished at MERCHANT status.")

    elif 100 <= score < 150:
        print("Great job, you finished at KNIGHT status.")

    elif score >= 150:
        print("Amazing job! You finished at WARRIOR status.")

    else:
        print(" ")

    print(" ")

    # Asking the user if they would like to play again
    restart = input("Would you like to play again?")

    if restart == "Yes" or restart == "yes":
        continue

    elif restart == "No" or restart == "no":
        break

    else:
        print("That is an Invalid Input!")
        restart = input("Would you like to play again?")


