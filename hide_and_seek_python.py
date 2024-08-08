import random

def hide_and_seek():
    print("Welcome to Hide and Seek!")
    print("Try to guess where the computer is hiding.")
    
    # Define possible hiding spots
    spots = ["under the bed", "in the closet", "behind the curtain", "under the table", "in the cabinet"]
    
    # Randomly choose a hiding spot for the computer
    hiding_spot = random.choice(spots)
    
    # Allow the player a number of attempts to guess the hiding spot
    attempts = 3
    
    while attempts > 0:
        # Ask the player to make a guess
        guess = input("Where do you think the computer is hiding? ").strip().lower()
        
        if guess in spots:
            if guess == hiding_spot:
                print("Congratulations! You found the hiding spot!")
                break
            else:
                attempts -= 1
                print(f"Not quite! Try again. You have {attempts} {'attempts' if attempts > 1 else 'attempt'} left.")
        else:
            print("That's not a valid spot. Please choose from the following options:")
            print(", ".join(spots))
    
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The hiding spot was '{hiding_spot}'.")

# Run the game
hide_and_seek()
