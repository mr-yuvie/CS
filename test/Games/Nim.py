import random

def Instructions():
    print(
        """ ------------ NIM -------------

    Instructions:

    1. The Objective of the Game is to leave the other player with the Last Stick.
    2. You can choose your Starting Position as P1 or P2.
    3. Choose number of Rows in the Game.
    4. Choose max number of Sticks that can be removed in a Single Turn.
    5. Player 1 starts the Game and the Game goes back and forth until the Last Stick.
    6. The Player with the Last Stick Loses the Game.
    7. If you accidentally pick up the Last Stick, You Lose. """
    )

    print("\n---------- Start Game ----------\n")


def Initialisation():
    while True:
        position = int(input("Choose Player 1 or Player 2: "))
        rows = int(input("Rows in the Game: "))
        # You can enter a very large number in max_removable_sticks if you want the player to be able to pickup any number of sticks from a single row
        max_removable_sticks = int(input("Max Removable Sticks in a Single Turn: "))
        if (position in [1, 2]) and rows > 1 and max_removable_sticks > 0:
            break
        else:
            print("The position must be 1 or 2.")
            print("The Row number must be greater than 1.")
            print("The max removable sticks must be greater than 0")
            print()
    total_sticks = 0
    # Counting the number of sticks to place row wise, where each row has increasing odd number of sticks
    for sticks in range(1, 2 * rows, 2):
        total_sticks += sticks
    return position, rows, max_removable_sticks, total_sticks


def Board(rows, total_sticks):
    current_row = rows  # Makes the top most row the current row
    sticks_placed = 0
    
    while current_row and total_sticks >= sticks_placed:
        # Counts the odd number of sticks to place in the current row
        sticks_to_place = 2 * current_row - 1
        remaining_sticks = total_sticks - sticks_placed
        # We just printout the remaing sticks instead of printing out the actual possible sticks of that row
        if sticks_to_place >= remaining_sticks:
            # This is just to shift each row to the right to make it look like an actual nim pyramid
            print("   " * (rows - current_row), end="")
            print(" | " * remaining_sticks)
            return remaining_sticks
        else:
            print("   " * (rows - current_row), end="")
            print(" | " * sticks_to_place)
            sticks_placed += sticks_to_place
            current_row -= 1


def GamePlay(position,rows, max_removable_sticks, total_sticks,remaining_sticks):
    # P1 always starts the game obviously
    current_position = 1
    # Using p for player and c for computer. To go back and forth during turns.
    while total_sticks > 1:
        # Checks if the player chose to be P1 or if it's player's turn
        if current_position == position or current_position == 'p':
            # If the remaining sticks in the current row are less than max removable sticks, then you are only allowed to remove the remaining sticks
            if remaining_sticks < max_removable_sticks:
                sticks_to_remove = int(input(f"Enter sticks to remove[1-{remaining_sticks}]: "))
            else:
                sticks_to_remove = int(input(f"Enter sticks to remove[1-{max_removable_sticks}]: "))
            if sticks_to_remove > max_removable_sticks or sticks_to_remove > remaining_sticks:
                print("Please enter a valid value.")
            else:
                total_sticks -= sticks_to_remove
                remaining_sticks = Board(rows, total_sticks)
                print("Removed Sticks: ",sticks_to_remove)
                print()
                # Passes the turn to the Computer
                current_position ='c'
        else:
            # Makes it so the computer always removes all the sticks but 1 if it can, so you always lose if you don't play well
            if total_sticks <= max_removable_sticks:
                sticks_to_remove = total_sticks - 1
            elif remaining_sticks < max_removable_sticks:
                sticks_to_remove = random.randint(1,remaining_sticks)
            else:
                sticks_to_remove = random.randint(1,max_removable_sticks)
            total_sticks -= sticks_to_remove
            remaining_sticks = Board(rows,total_sticks)
            print("Removed Sticks: ",sticks_to_remove)
            print()
            # Passes the turn to the Player
            current_position ='p'
    
    # Checks for all the ending possibilities
    if total_sticks < 2:
        if current_position == 'p':
            if total_sticks == 1:
                print("You Lost.")
            else:
                print("Congratulations, You Won.")
        elif current_position == 'c':
            if total_sticks == 1:
                print("Congratulations, You Won.")
            else:
                print("You Lost.")
        exit()


def main():
    Instructions()
    position, rows, max_removable_sticks, total_sticks = Initialisation()
    remaining_sticks = Board(rows, total_sticks)
    GamePlay(position, rows, max_removable_sticks, total_sticks, remaining_sticks)


main()
