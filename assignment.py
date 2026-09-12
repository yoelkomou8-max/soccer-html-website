name = input("What is your name? ")
favorite_food = input("What is your favorite food? ")
favorite_color = input("What is your favorite color? ")

message = (
    f"Name: {name}\n"
    f"Favorite food: {favorite_food}\n"
    f"Favorite color: {favorite_color}\n"
)

with open("my_information.txt", "w") as file:
    file.write(message)

print("Your information was saved to my_information.txt!")
