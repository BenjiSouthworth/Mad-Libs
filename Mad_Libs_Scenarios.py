import Mad_Libs_Functions
from Mad_Libs_Functions import adjective, noun, national, person, pluralNoun, numbers, food, shapes

def pizza():
    qcount = 15

    def wordsLeft(count):
        count -= 1
        print(count, " questions left.")
        return count

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