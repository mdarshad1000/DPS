import math
from typing import List


def snakeTable(userArray: List[int]) -> None:
    """
    Prints a snake table based on the given userArray.
    The snake table is created by arranging the elements of userArray in a zigzag pattern.

    Args:
        userArray (List[int]): The list of integers to be arranged in the snake table.

    Returns:
        None

    Example:
        Enter the number: 123456
        145
        236

    """
    size = math.ceil(len(userArray) / 2) 

    # Initalize an empty 2D array
    snakeTable = [['' for _ in range(size)] for _ in range(2)]
    
    flag = True
    row = 0
    col = 0

    for i in range(len(userArray)):
        if flag:
            snakeTable[row][col] = userArray[i]
            if row < 1:
                row += 1
            else:
                row -= 1
            flag = False
        else:
            snakeTable[row][col] = userArray[i]
            col += 1
            flag = True

    for row in snakeTable:
        print(''.join(str(element) for element in row))


# Take user input as a string
userInput = input("Enter the number: ")

# Convert the string into a list
userArray = list(map(int, userInput))

snakeTable(userArray)
