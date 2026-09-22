def show_help():
    print("Type 'help' to see this list again")
    print("Type 'see' to get a list of all the animals in the zoo")
    print("Type 'pet' followed by the animal's name to pet a particular animal")
    print("Type 'bye' to exit the zoo")

def show_all_animals():
    print("The animals in the zoo are:")
    print("• Clover the Bunny 🐇")
    print("• Coco the Baby Goat 🐐")
    print("• Arno the Alligator 🐊")


def pet_animal(animal):
    if animal == "clover":
        print("Clover is so happy! ❤️")
    elif animal == "coco":
        print("Coco the Baby Goat thanks you! 🥰")
    elif animal == "arno":
        print("Actually, we cannot allow you to pet Arno. ⛔️")
    else:
        print("Sorry, I don't know that animal")


print("Welcome to the Petting Zoo!")
print("Type 'help' to get a list of all the things you can do")
print()

keep_going = True
while keep_going:
    response = input("What would you like to do? ").strip().lower()
    if response == "help":
        show_help()
    if response == "see":
        show_all_animals()
    if response.startswith("pet "):
        animal = response[4:]
        pet_animal(animal)
    elif response == "bye":
        print("Goodbye!")
        keep_going = False
    else:
        print("Sorry, I don't understand the command. Please try again. ")
