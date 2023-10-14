age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote. Exercise your right to vote!")
    registered = input("Have you registered to vote? (yes/no): ").lower()
    if registered == "yes":
        print("Great! Make sure to cast your vote in the upcoming election.")
    else:
        print("Please consider registering to vote. It's an important civic duty."
else:
        print("Sorry, you are not eligible to vote yet.")

    years_to_wait = 18 - age
    if years_to_wait > 1:
        print(f"You'll be eligible to vote in {years_to_wait} years.")
    elif years_to_wait == 1:
        print("You'll be eligible to vote next year.")
    else:
        print("You'll be eligible to vote in the upcoming election.")

