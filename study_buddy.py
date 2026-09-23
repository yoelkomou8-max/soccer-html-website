# Study Buddy Chatbot
# This chatbot helps students with studying.

name = "Yoel"

print("Welcome to Study Buddy!")
print("Hello, " + name + "! Nice to meet you.")
print("\nWhat would you like help with?")
print("1. Study tip")
print("2. Motivation")
print("3. Break suggestion")
print("4. Exit")

choice = input("Choose 1, 2, 3, or 4: ")
if choice == "1":
    print("Yoel, try studying for 25 minutes and then take a 5-minute break.")

elif choice == "2":
    print("Keep going, Yoel! You can do it!")

elif choice == "3":
    print("Yoel, take a short break, stretch, and drink some water.")

elif choice == "4":
    print("Goodbye, Yoel!")

else:
    print("Sorry, I did not understand your choice.")