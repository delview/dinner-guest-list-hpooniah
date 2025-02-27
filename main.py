# greet the user
print("Hello there! This is a dinner Guest invation list.")
name = input("Before we get started, what is your name? ").capitalize()
print(f"Let's get started {name}!")

# Create the guest list
guest = []

# Ask how many people are coming
while true:
    try:
        number_invations = int(input("How many number of invations would you ike to make? "))
    expect ValueError:
        print("Only type a integer!")

# A loop runs untill everyone has been added
for num in range(number_invations):
    # Name of the guest that are coming
        name_guest = input(" Name the guest that are invited: ")
        guest.append(number_invations)
        print("The peroson has been added to the guest list")

# Print a message to each person
for num in range(num_people): 
    print(f"Messaging {name_guest}")
    print(f"Hey {name_guest}! you have gotten a invatation to {name}'s dinner party")

# Remove person from guest list
while True:
    take_off = input("Is their anyone you would like to take off the guest list? [y] or [no]")
    if take_off == "y"
        eleminate = input("")




