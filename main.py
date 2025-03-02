# greet the user
print("Hello there! This is a dinner Guest invation list.")
name = input("Before we get started, what is your name? ").capitalize()
print(f"Let's get started {name}!")

# Create the guest list
guest = []

# Ask how many people are coming
number_invations = int(input("How many number of invations would you ike to make? "))

# A loop runs untill everyone has been added
for num in range(number_invations):
    # Name of the guest that are coming
    name_guest = input(f"Name the guest that are invited: #{num + 1}: ")
    guest.append(name_guest)
    print("The peroson has been added to the guest list")

# Print a message to each person
print(f"Messaging {name_guest}")
for guest_name in guest:
    print(f"Hey {name_guest}! you have gotten a invatation to {name}'s dinner party")

# Remove person from guest list
while True:
    take_off = input("Is their anyone you would like to take off the guest list? [y] or [no]")
    if take_off == "y":
        eliminate = input("Please Enter the name of the person you want to take off from the guest list? ")
        if eliminate in guest:
            guest.remove(eliminate)
            print(f"{eliminate} is no longer on the guest list")
            print(guest)
            
            # Ask if they want to replace the person
            replace = input(f"Would you like to replace {eliminate} with someone else? [y] or [n]: ").lower()
            if replace == "y":
                join = input("Who would you like to invite instead? ").capitalize()
                guest.append(join)
                print(f"An invitation has been sent to {join}.")
            elif replace == "n":
                print("No replacement made.")

         



