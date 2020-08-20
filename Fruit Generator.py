import random  # Importing random to have random <number> <color> <fruit type> be generated
from datetime import datetime

random.seed(datetime.now())  # Generating random seed to mix up results


# Beginning of Class "Fruit"
class Fruit:

    def __init__(self):  # Initialization of the class so it runs when just the class is called.
        self.main = Fruit.main2()

    def main2():
        color = ["Red", "Green", "Orange", "Yellow"]  # Selection of available colors as fruit will be sorted by color selected.

        fruit1 = ["Pear", "Apple"]  # Fruit 1 is designated to be randomly selected when color "Green" is selected.

        fruit2 = ["Lemon", "Apple", "Pear"]  # Fruit 2 is designated to be randomly selected when color "Yellow" is selected.

        color_choice = random.choice(color)  # This will randomly select the color and then enter a scenario of if statements to determine random fruit type.

        #  Beginning of Fruit selection process based on color
        if color_choice == 'Red':
            product = color_choice + " " + 'Apple'
        if color_choice == 'Green':
            product = random.choice(fruit1)
            if product == 'Pear':
                product = color_choice + " " + product
            else:
                product = color_choice + " " + product
        if color_choice == 'Orange':
            product = 'Orange'  # If color choice is orange, only product that could be orange is an Orange.
        if color_choice == 'Yellow':
            product = random.choice(fruit2)  # If color choice is yellow, Randomization of Fruit2 will occur.
            if product == 'Lemon':
                product = 'Lemon'
            elif product == 'Apple':
                product = color_choice + " " + 'Apple'
            else:
                product = color_choice + " " + 'Pear'
        return product  # Return product to be stored in class initialization.

    def __str__(self):  # Define String so that class objects appear as string and not memory location.
        self.fruit = Fruit.main2()
        return f'{self.fruit}'


# End of Class.


# Beginning of actual program.


# List Appendage
count = 0
lst = []  # Empty list to store 1000 Fruit class instances.
while count < 1000:
    lst.append(str(Fruit()))
    count += 1
# End of List Appendage


# Counter Variables being determined by use of lst.count.

gpc = lst.count('Green Pear')
ypc = lst.count('Yellow Pear')
rac = lst.count('Red Apple')
gac = lst.count('Green Apple')
yac = lst.count('Yellow Apple')
orac = lst.count('Orange')
lemc = lst.count('Lemon')

# End of Counter Variable Section.


# Sorting Section.

lst2 = [gpc, ypc, rac, gac, yac, orac, lemc]  # Putting counter variables in lst 2.
lst2 = sorted(lst2, reverse=True)  # Sorting lst 2 to sort counter variables in descending order.

# Loop to determine which element in lst2 is recognized by which counter variable. Once recognized, it will
# output a print statement based on which variable was chosen and if there is either one or more then one instance
# of that color / fruit type combination.
i = 0
while i < 7:
    if gpc == lst2[i]:
        if lst2[i] == 1:
            print(str(gpc) + " Green Pear found in the list")
        else:
            print(str(gpc) + " Green Pears found in the list")
    elif ypc == lst2[i]:
        if lst2[i] == 1:
            print(str(ypc) + " Yellow Pear found in the list")
        else:
            print(str(ypc) + " Yellow Pears found in the list")
    elif rac == lst2[i]:
        if lst2[i] == 1:
            print(str(rac) + " Red Apple found in the list")
        else:
            print(str(rac) + " Red Apples found in the list")
    elif gac == lst2[i]:
        if lst2[i] == 1:
            print(str(gac) + " Green Apple found in the list")
        else:
            print(str(gac) + " Green Apples found in the list")
    elif yac == lst2[i]:
        if lst2[i] == 1:
            print(str(yac) + " Yellow Apple found in the list")
        else:
            print(str(yac) + " Yellow Apples found in the list")
    elif orac == lst2[i]:
        if lst2[i] == 1:
            print(str(orac) + " Orange found in the list")
        else:
            print(str(orac) + " Oranges found in the list")
    else:
        if lst2[i] == 1:
            print(str(lemc) + " Lemon found in the list")
        else:
            print(str(lemc) + " Lemons found in the list")
    i += 1

# End of Loop & Sorting Section.


# End of Program.

# Thank you for your consideration in me and I am looking forward to receive your feedback.
