TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

separator = "-" * 50

username = input("username ")
password = input("password: ")

if username in users and users[username] == password:
    print(separator)
    print(f"Welcome to the app, {username}.")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print(separator)
else:
    print(separator)
    print("Unregistered user, terminating the program.")
    print(separator)
    quit()

choice = input(f"Enten a number between 1 and {len(TEXTS)} to select: ")
if not choice.isdigit():
    print("Invalid input, terminating program.")
    quit()

choice = int(choice)

if choice < 1 or choice > len(TEXTS):
    print ("Invalid number, terminating program.")
    quit ()

text = TEXTS[choice - 1]

words = text.split()

titlecase = 0
uppercase = 0
lowercase = 0
numbers = []
lengths = {}

for word in words:
    clean = word.strip(",.:")

    if clean.istitle():
        titlecase += 1
    if clean.isupper():
        uppercase += 1
    if clean.islower():
        lowercase += 1
    
    if clean.isdigit():
        numbers.append(int(clean))
    
    length = len(clean)

    if length not in lengths:
        lengths[length] = 1
    else:
        lengths[length] += 1

print(separator)
print(f"There are {len(words)} words in the selected text.")
print(f"There are {titlecase} titlecase words.")
print(f"There are {uppercase} uppercase words.")
print(f"There are {lowercase} lowercase words.")
print(f"There are {len(numbers)} numeric strings")
print(f"The sum off all the numbers {sum(numbers)}")
print(separator)

print("LEN|  OCCURRENCES  |NR.")
print(separator)

for length in sorted(lengths):
    stars = "*" * lengths[length]
    print(f"{length:>3}|{stars:<20}|{lengths[length]}")