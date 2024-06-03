import random
import time

# Constants for grid dimensions
GRID_WIDTH = 20
GRID_HEIGHT = 10

# Constants for number of zombies and quicksand
ZOMBIE_COUNT = 4
QUICKSAND_COUNT = 8

# Set area of text and print title on screen.

def initialize_screen():
    # Display the game title
    print("......ZOMBIES")
    print()

# Print area of the ranch within which you and zombies can move.
def get_random_coordinate(limit):
      # Generate a random coordinate within the given limit
    return random.randint(1, limit)

# The starting positions of the zombies, which are randomly chosen, are shown.
def create_empty_grid(width, height):
    # Create an empty grid with the given width and height
    grid = []
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(' ')
        grid.append(row)
    return grid

# The randomly chosen quicksand traps are placed on the screen.
def draw_grid(human, zombies, quicksand):
    # Draw the grid with the current positions of the human, zombies, and quicksand

    # Create an empty grid
    grid = create_empty_grid(GRID_WIDTH, GRID_HEIGHT)

    # Place quicksand in the grid
    for x, y in quicksand:
        grid[y-1][x-1] = '*'
    
    # Place zombies in the grid
    for x, y in zombies:
        if x != 0 and y != 0:
            grid[y-1][x-1] = 'Z'
    
    # Place human in the grid
    human_x, human_y = human
    grid[human_y-1][human_x-1] = 'H'

    # Draw the grid with borders
    print("*"*(GRID_WIDTH+2))
    for row in grid:
        print("*" + ''.join(row) + "*")
    print("*"*(GRID_WIDTH+2))


# Your own position is placed on the screen.
def delay(seconds):
    # Delay for the given number of seconds
    time.sleep(seconds)

# Your choice of move is registered.
def get_keypress():
    # Get a single keypress from the user
    direction = input("Enter direction (W=up, X=down, s=stay, a=left, d=right, q=up-left, e=up_right, z=down_left, c=down_right): ")

    if direction == 'w':
        return (0, -1) # Up
    elif direction == 'x':
        return (0, 1) # Down
    elif direction == 's':
        return (0, 0) # Stay
    elif direction == 'a':
        return (-1, 0) # Left
    elif direction == 'd':
        return (1, 0) # Right
    elif direction == 'q':
        return (-1, -1) # Up-left
    elif direction == 'e':
        return (1, -1)  # Up-right
    elif direction == 'z':
        return (-1, 1) # Down-left
    elif direction == 'c':
        return (1, 1) # Down-right
    else:
        print("Invalid input. Please try again.")
        return get_keypress() # Try again if the input is invalid
        

# Check your new position and report if you hit quicksand, strayed into the swamp or were caught by zombies.

def main():
    
    # Initialize the screen
    initialize_screen()
    
    # Initialize the game state
    human = (get_random_coordinate(GRID_WIDTH), get_random_coordinate(GRID_HEIGHT))
    zombies = [(get_random_coordinate(GRID_WIDTH), get_random_coordinate(GRID_HEIGHT)) for _ in range(ZOMBIE_COUNT)]
    quicksand = [(get_random_coordinate(GRID_WIDTH), get_random_coordinate(GRID_HEIGHT)) for _ in range(QUICKSAND_COUNT)]
    
    human_x = get_random_coordinate(GRID_WIDTH-2)
    human_y = get_random_coordinate(GRID_HEIGHT-2)
    human = (human_x, human_y)

    # Main game loop
    while True:
        # Draw the grid
        draw_grid(human, zombies, quicksand)
        
        # Get the user's move
        direction = get_keypress()
        human_x += direction[0]
        human_y += direction[1]

        # Check if the human has escaped
        if zombies == [[0,0] for _ in range(ZOMBIE_COUNT)]:
            print("You have escaped the zombies! Congratulations!")
            break

        # Check if the human is out of bounds
        if human_x in {1, GRID_WIDTH} or human_y in {1, GRID_HEIGHT}:
            print("You are in the swamp!")
            continue

        # Check if the human is in quicksand
        if (human_x, human_y) in quicksand:
            print("You are in quicksand!")
            break

        # Check if the human is caught by a zombie
        if (human_x, human_y) in zombies:
            print("You are caught by a zombie!")
            break

        # Update the human's position based on the move
        human = (human_x, human_y)
        draw_grid(human, zombies, quicksand)
        delay(0.5)

        # Check for collisions with zombies and quicksand
        for i, (zombie_x, zombie_y) in enumerate(zombies):
            if zombie_x == 0:
                continue # Skip inactive zombies

            # Move the zombie closer to the human
            if human_x != zombie_x:
                zombie_x += (human_x - zombie_x) // abs(human_x - zombie_x)
            if human_y != zombie_y:
                zombie_y += (human_y - zombie_y) // abs(human_y - zombie_y)

            # Check if the zombie falls into quicksand
            if (zombie_x, zombie_y) in quicksand:
                zombies[i] = (0, 0) # Zombie falls into quicksand
                print("A zombie falls into quicksand!")
                continue

            # Check if zombie catches the human
            if (zombie_x, zombie_y) == human:
                print("A zombie catches you!")
                break
                
            # Update the zombie's position and redraw the grid
            zombies[i] = (zombie_x, zombie_y)
            draw_grid(human, zombies, quicksand)
            delay(0.5)

if __name__ == "__main__":
    main()