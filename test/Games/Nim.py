import random

# print(
#     """ ------------ NIM -------------

# Instructions:

# 1. You have to select any random number from 1 to 6.
# 2. The computer will also select a number.
# 3. While batting, if the number selected by you and computer is different, then your number will add to your runs.
#    If the number selected by you and computer is same, then you will lose your wicket.
# 4. While bowling, if the number selected by you and computer is different, then the computer's number will add to its runs.
#    If the number selected by you and computer is same, then the computer will lose its wicket.
# 5. Each player will get 2 wickets and 2 overs (12 balls) for batting and bowling.
# 6. The innings will end after either the three wickets fell or the overs end.
# 7. The player with maximum runs wins. """
# )

# print("\n---------- Start Game ----------")


# Player gets to choose if they wanna play first or second.
def Initialisation():
    while True:
        position = int(input("Choose Player 1 or Player 2: "))
        rows = int(input("Rows in the game: "))
        # You can enter a very large number in max_removable_sticks if you want the player to be able to pickup any number of sticks from a single row
        max_removable_sticks = int(input("max removable Sticks in a single turn: "))
        if (position in [1, 2]) and rows > 1 and max_removable_sticks > 0:
            break
        else:
            print("The position must be 1 or 2.")
            print("The Row number must be greater than 1.")
            print("The max removable sticks must be greater than 0")
            print()
    total_sticks = 0
    for sticks in range(1, 2 * rows, 2):
        total_sticks += sticks
    return position, rows, max_removable_sticks, total_sticks


def Board(rows, total_sticks):
    current_row = rows  # Makes the top most row the current row
    sticks_placed = 0
    
    while current_row and total_sticks >= sticks_placed:
        sticks_to_place = 2 * current_row - 1
        remaining_sticks = total_sticks - sticks_placed
        # We just printout the remaing sticks instead of printing out the actual possible sticks of that row
        if sticks_to_place >= remaining_sticks:
            print("   " * (rows - current_row), end="")
            print(" | " * remaining_sticks)
            return remaining_sticks
        else:
            print("   " * (rows - current_row), end="")
            print(" | " * sticks_to_place)
            sticks_placed += sticks_to_place
            current_row -= 1


def GamePlay(position,rows, max_removable_sticks, total_sticks,remaining_sticks):
    current_position = 1
    # Using p for player and c for computer. To go back and forth during turns.
    while total_sticks > 1:
        if current_position == position or current_position == 'p':
            if remaining_sticks < max_removable_sticks:
                sticks_to_remove = int(input(f"Enter sticks to remove[1-{remaining_sticks}]: "))
            else:
                sticks_to_remove = int(input(f"Enter sticks to remove[1-{max_removable_sticks}]: "))
            if sticks_to_remove > max_removable_sticks or sticks_to_remove > remaining_sticks:
                print("Please enter a valid value.")
            else:
                total_sticks-=sticks_to_remove
                remaining_sticks=Board(rows,total_sticks)
                print()
                current_position='c'
        else:
            if total_sticks <= max_removable_sticks:
                sticks_to_remove = total_sticks - 1
            elif remaining_sticks < max_removable_sticks:
                sticks_to_remove = random.randint(1,remaining_sticks)
            else:
                sticks_to_remove = random.randint(1,max_removable_sticks)
            total_sticks-=sticks_to_remove
            remaining_sticks=Board(rows,total_sticks)
            print("Removed Sticks: ",sticks_to_remove)
            print()
            current_position='p'
    
    if total_sticks<2:
        if current_position=='p':
            if total_sticks==1:
                print("You Lost.")
            else:
                print("Congratulations, You Won.")
        if current_position=='c':
            if total_sticks==1:
                print("Congratulations, You Won.")
            else:
                print("You Lost.")
        exit()


def main():
    position, rows, max_removable_sticks, total_sticks = Initialisation()
    remaining_sticks = Board(rows, total_sticks)
    GamePlay(position,rows,max_removable_sticks,total_sticks, remaining_sticks)


main()
