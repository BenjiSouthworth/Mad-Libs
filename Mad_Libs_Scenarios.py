import Mad_Libs_Functions
from Mad_Libs_Functions import adjective, noun, national, person, pluralNoun, numbers, food, shapes
from Mad_Libs_Functions import presentVerb, pluralBody
def wordsLeft(count):
    count -= 1
    print(count, " questions left.")
    return count

def pizza():
    qcount = 15

    adj1 = adjective()
    qcount = wordsLeft(qcount)
    nat = national()
    qcount = wordsLeft(qcount)
    per = person()
    qcount = wordsLeft(qcount)

    noun1 = noun()
    qcount = wordsLeft(qcount)
    adj2 = adjective()
    qcount = wordsLeft(qcount)
    noun2 = noun()
    qcount = wordsLeft(qcount)


    adj3 = adjective()
    qcount = wordsLeft(qcount)
    adj4 = adjective()
    qcount = wordsLeft(qcount)
    pnoun = pluralNoun()
    qcount = wordsLeft(qcount)

    noun3 = noun()
    qcount = wordsLeft(qcount)

    num1 = numbers()
    qcount = wordsLeft(qcount)
    shape = shapes()
    qcount = wordsLeft(qcount)

    food1 = food()
    qcount = wordsLeft(qcount)
    food2 = food()
    qcount = wordsLeft(qcount)

    num2 = numbers()


    print("\n\nPizza was invented by a " + adj1 + " " + nat + " chef named " + per + ".")
    print("To make pizza, you need to take a lump of " + noun1 + ", and make a thin, round " + adj2 + " " + noun2 + ".")
    print("Then you cover it with " + adj3 + " sauce, " + adj4 + " cheese, and freshly chopped " + pnoun + ".")
    print("Next you have to bake it in a very hot " + noun3 + ".")
    print("When it is done, cut it into " + num1 + " " + shape + ".")
    print("Some kids like " + food1 + " pizza the best, but my favorite is " + food2 + " pizza.")
    print("If i could, I would eat pizza " + num2 + " times a day!\n")

def computer():
    ccount = 8

    noun1 = noun()
    ccount = wordsLeft(ccount)

    pnoun = pluralNoun()
    ccount = wordsLeft(ccount)

    pverb1 = presentVerb()
    ccount = wordsLeft(ccount)

    pverb2 = presentVerb()
    ccount = wordsLeft(ccount)
    pob1 = pluralBody()
    ccount = wordsLeft(ccount)
    
    adj1 = adjective()
    ccount = wordsLeft(ccount)
    pnoun2 = pluralNoun()
    ccount = wordsLeft(ccount)
    adj2 = adjective()

    print("\n\nToday, every student has a computer small enough to fit into his " + noun1 + ".")
    print("He can solve any math problem by simply pushing the computers little " + pnoun + ".")
    print("Computers can add, multiply, divide, and " + pverb1 + ".")
    print("They can also " + pverb2 + " better than a human. Some computers are " + pob1 + ".")
    print("Others have a/an " + adj1 + " screen that shows all kinds of " + pnoun2 + " and " + adj2 + " figures.")