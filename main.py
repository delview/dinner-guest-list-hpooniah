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
    print(f"Hey {guest_name}! you have gotten a invatation to {name}'s dinner party")

# Remove person from guest list
while True:
    take_off = input("Is their anyone you would like to take off the guest list? [y] or [no]")
    if take_off == "y":
        eliminate = input("Please Enter the name of the person you want to take off from the guest list? ")
        if eliminate in guest:
            guest.remove(eliminate)
            print(f"{eliminate} is no longer on the guest list")
            print(f"Updated guest list: {guest}")
            
            # Ask if they want to replace the person
            replace = input(f"Would you like to replace {eliminate} with someone else? [y] or [n]: ").lower()
            if replace == "y":
                join = input("Who would you like to invite instead? ").capitalize()
                guest.append(join)
                print(f"An invitation has been sent to {join}.")
            elif replace == "n":
                print("No replacement made.")
        else:
            print(f"{eliminate} was not on the list.")
    elif take_off == "n":
        print("No chnages made to the guest list.")
        break

    else:
        print("Please enter [y] or [n]. ")
# Print the list after the ajustments
print("Final Guest List")
guest.sort() 
for guest_name in guest:
    print(f"Hey {guest_name}! You have received an invation to {name}'s dinner party.")

# Print the number of guest invited
print(f"Total number of guest invited: {len(guest)}")


         


