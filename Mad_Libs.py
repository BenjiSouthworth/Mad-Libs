import Mad_Libs_Scenarios
from Mad_Libs_Scenarios import pizza, computer
print("\nWelcome to Mad-Libs! \nProvide answers to the questions below for some laugh out loud fun!\n")

choice = int(input("Choose scenario 1, 2 or 3: "))

if choice == 1:
    pizza()
elif choice == 2:
    computer()

elif choice == 3:
    print("Sorry also not avaiable yet.")
else:
    print("Error, Please select either 1, 2 or 3")