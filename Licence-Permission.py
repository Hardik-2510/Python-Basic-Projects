print("---------------------------------")
print("\tLicence Manager 🪪")
print("---------------------------------")

try:
    age = int(input("Enter Your Age : "))
except ValueError:
    print("Invalid age! Please enter a number.")
    exit()

print("---------------------------------")

if age < 18:
    print("You should wait until 18 to apply for a licence.")
else:
    choice = input("Do you have a licence? (Y/N): ").strip().upper()
    print("---------------------------------")

    if choice == "Y":
        print("Thank you!")
    elif choice == "N":
        print("You need to apply for a licence.")
    else:
        print("Invalid input! Please enter Y or N.")

print("---------------------------------")
print("Thanks for using Licence Manager 💐")
print("---------------------------------")
print("Software Designed By\n\t~ H a c k y B o y")
print("---------------------------------")
print("Developer - Hardik Patel")
