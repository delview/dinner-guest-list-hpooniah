def dinner_invitation():
    # Greet the user and ask for their name
    print("Hello there! This is a dinner guests invitation list.")
    name = input("Before we get started, what is your name? ").capitalize()
    print(f"Let's get started {name}!")

    # Create the guests list
    guest = []

    # Ask how many people are coming
    while True:
        try:
            number_invitation = int(input("How many guests would you like to invite? "))
            break # exit loop if it is not invalid
        except ValueError:
            print("Please enter a valid number.")

    # A loop runs untill everyone has been added
    for num in range(number_invitation):
        # Name of the guest that are coming
        name_guest = input(f"Enter the name of the guests: #{num + 1}: ").capitalize()
        guest.append(name_guest) # add guests to list
        print(f"Guest {name_guest} has been added to the guest list")

    # Print a message to each person
    print(f"Messaging")
    for guest_name in guest:
        print(f"Hey {guest_name}! You have received a invitation to {name}'s dinner party")

    # Remove person from guest list
    while True:
        take_off = input("Is there anyone you would like to remove from the guest list? [y] or [n]").lower()
        if take_off == "y":
            eliminate = input("Enter the name of the guests you want to remove? ").capitalize()
            if eliminate in guest:
                guest.remove(eliminate)
                print(f"{eliminate} is no longer on the guest list")
                print(f"Updated guests list: {guest}")
                    
                # Ask if they want to replace the person
                replace = input(f"Would you like to replace {eliminate} with someone else? [y] or [n]: ").lower()
                if replace == "y":
                    join = input("Who would you like to invite instead? ").capitalize()
                    guest.append(join)
                    guest.sort() # guests are alphabetically sorted
                    print(f"An invitation has been sent to {join}.")
                elif replace == "n":
                    print("No replacement made.")
            else:
                print(f"{eliminate} was not on the list.")
        elif take_off == "n":
            print("No changes made to the guest list.")
            break

        else:
            print("Please enter [y] or [n]. ")
    # Print the list after the adjustments
    print("Here is the final guest list")
    guest.sort() 
    for guest_name in guest:
        print(f"Hey {guest_name}! You have received an invitation to {name}'s dinner party.")

    # Print the number of guests invited
    print(f"Total number of guests invited: {len(guest)}")

while True:
    # Ask the user if they want to play again
    play_again = input("\nWould you like to create another dinner invitation list? [y/n]: ").lower()
    if play_again != "y":
        print("Thank you for using this website for your dinner invitation!")
        break
    dinner_invitation()
