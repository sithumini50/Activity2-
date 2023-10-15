# Prompt the user to enter their age
age = int(input("Enter your age: "))

# Check if the user is eligible to vote
if age >= 18:
    # If eligible, encourage the user to vote and ask if they're registered
    print("You are eligible to vote. Exercise your right to vote!")
    registered = input("Have you registered to vote? (yes/no): ").lower()
    
    # Check if the user is registered
    if registered == "yes":
        print("Great! Make sure to cast your vote in the upcoming election.")
    else:
        print("Please consider registering to vote. It's an important civic duty."
else:
    # If not eligible, inform the user and calculate the years they need to wait
    print("Sorry, you are not eligible to vote yet.")
    years_to_wait = 18 - age
              
    # Provide information about the years they need to wait before they can vote
    if years_to_wait > 1:
        print(f"You'll be eligible to vote in {years_to_wait} years.")
    elif years_to_wait == 1:
        print("You'll be eligible to vote next year.")
    else:
        print("You'll be eligible to vote in the upcoming election.")

