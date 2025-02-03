# Dice Game

print(
    """ ~~~~~~~~~~ Game of Dice ~~~~~~~~~~
 
Instructions:
 
1. The dice will select any random number from 1 to 6.
2. Each player will get 2 rolls per round for a total of 5 rounds.
3. While rolling, if the sum of the two numbers rolled by a player is even, then 10 points will be added to their score.
   If the sum of the two numbers rolled by a player is odd, then 5 points will be subtracted from their score.
4. In case of a tie, an additional round will be provided to both players untill one of them wins.
5. The player with maximum points wins. """
)

print("\n---------- Start Game ----------")

import random


def User_Authorisation(username):
    with open(r"Y:\CS\Test\Users.txt", "r") as D:
        authorized_usernames = [line.strip() for line in D]
        return username in authorized_usernames


Player_1 = input("Enter Name of Player 1:").strip()
if User_Authorisation(Player_1):
    print(f"Access granted. Welcome, {Player_1}!")
else:
    print("Access denied. Your name is not on the authorized list.")
    exit()

Player_2 = input("Enter Name of Player 2:").strip()
if User_Authorisation(Player_2):
    print(f"Access granted. Welcome, {Player_2}!")
else:
    print("Access denied. Your name is not on the authorized list.")
    exit()


def Game():
    score_1 = 0
    score_2 = 0
    rounds = 1
    max_rounds = 6
    points_1 = 0
    points_2 = 0

    while rounds != max_rounds:
        print(f"\n----------Round {rounds} Begins ----------")
        player1_roll_1 = random.randint(1, 6)
        player1_roll_2 = random.randint(1, 6)
        player2_roll_1 = random.randint(1, 6)
        player2_roll_2 = random.randint(1, 6)

        print(
            f"{Player_1} Rolled:",
            player1_roll_1,
            " & ",
            player1_roll_2,
            f"\n{Player_2} Rolled:",
            player2_roll_1,
            " & ",
            player2_roll_2,
        )
        points_1 = player1_roll_1 + player1_roll_2
        points_2 = player2_roll_1 + player2_roll_2

        if (points_1) % 2 == 0:
            score_1 += 10

        elif (points_1) % 2 != 0:
            if score_1 < 10:
                score_1 = 0
            else:
                score_1 -= 5

        if (points_2) % 2 == 0:
            score_2 += 10

        elif (points_2) % 2 != 0:
            if score_2 < 10:
                score_2 = 0
            else:
                score_2 -= 5

        rounds += 1
        print(f"\nScore of {Player_1} =", score_1, f"\nScore of {Player_2} =", score_2)

        if rounds == max_rounds and score_1 == score_2:
            max_rounds += 1

    # Result of Match

    print("\n~~~~~~~~~~ Result ~~~~~~~~~~")

    if score_1 > score_2:
        print(
            f"\nCongratulations! {Player_1} won the Game by",
            score_1 - score_2,
            "points.",
        )
        with open("Y:\\CS\Test\Winners.txt", "a") as F:
            F.write(f"{Player_1} won with a score of {score_1} points\n")

    elif score_2 > score_1:
        print(
            f"\nCongratulations! {Player_2} won the Game by",
            score_2 - score_1,
            "points.",
        )
        with open("Y:\\CS\Test\Winners.txt", "a") as F:
            F.write(f"{Player_2} won with a score of {score_2} points\n")


def Winners():
    with open("Y:\\CS\Test\Winners.txt", "r") as F:
        L = F.read()
        print("\n~~~~~~~~~~Past Winners of Game of Dice~~~~~~~~~~\n")
        print(L)


Game()
Winners()
