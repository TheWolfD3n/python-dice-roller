import random

def roll_dice(num_sides=6):
    """Simulates rolling a dice with a specified number of sides."""
    return random.randint(1, num_sides)

def main():
    """Gets user input and rolls the dice."""
    while True:
        try:
            num_dice = int(input("How many dice do you want to roll? "))
            if num_dice <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    while True:
        try:
            num_sides = int(input("How many sides on each die? "))
            if num_sides <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    for i in range(num_dice):
        result = roll_dice(num_sides)
        print(f"Die {i+1}: {result}")

if __name__ == "__main__":
    main()