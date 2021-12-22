import random

print("Total skill allotment: 300 points")
strength = input("Strength: power of the body and flesh, 1-100\n>")
if int(strength) > 100 or int(strength) < 0:
    print("What a shame")
    exit()
pointOne = 300 - int(strength)
print("Points remaining " + pointOne)
dexterity = input("Dexterity: skill and speed, 1-100\n>")
if int(dexterity) > 100 or int(dexterity) < 0:
    print("What a shame")
    exit()
pointTwo = int(pointOne) - int(dexterity)
print("Points remaining " + pointTwo)
intelligence = input("Intelligence: power of the mind and will, 1-100\n>")
if int(intelligence) > 100 or int(intelligence) < 0:
    print("What a shame")
    exit()
pointThree = int(pointTwo) - int(intelligence)
print("Points remaining " + pointThree)
faith = input("Faith: power of soul and belief, 1-100\n>")
if int(faith) > 100 or int(faith) < 0:
    print("What a shame")
    exit()
pointFour = int(pointThree) - int(faith)
print("Points remaining " + pointFour)
vitality = input("Vitality: bodily health and endurance, 1-100\n>")
if int(vitality) > 100 or int(vitality) < 0:
    print("What a shame")
    exit()
pointFive = int(pointFour) - int(vitality)
print("Points remaining " + pointFive)
attunement = input("Attunement: capability for magic, 1-100\n>")
if int(attunement) > 100 or int(attunement) < 0:
    print("What a shame")
    exit()
pointSix = int(pointFive) - int(attunement)
print("Points remaining " + pointSix)
if int(strength)+int(dexterity)+int(intelligence)+int(faith)+int(vitality)+int(attunement) > 300:
    print("What a shame")
    exit()

def skillList():
    print("Strength " + strength + "\n> Dexterity " + dexterity + "\n> Intelligence " + intelligence + "\n> Faith " + faith + "\n> Vitality " + vitality + "\n> Attunement " + attunement)

skillList()

print("You are faced with a wall of indomitable presence, what must you do?")
print("1. Break the wall")
print("2. Climb the wall")
print("3. Outwit the wall")
print("4. Convert the wall to your faith")
print("5. Join the wall in it's vigil")
print("6. Magic the wall")

choice = input("What do you choose, 1-6")

if int(choice) == 1:
    roll = random.randrange(0,int(strength))
    if roll > 20:
        print("The wall broke beneath your unstoppable strength, denting and cracking, proving you the victor.")
        if int(strength) <= 90:
            strength = int(strength) + 10
            print("+10 strength")
    else:
        print("The wall broke you instead, shattering your poor form under its weight, what a shame.")
        exit()

elif int(choice) == 2:
    roll2 = random.randrange(0,int(dexterity))
    if roll2 > 20:
        print("The wall seemed tiny under your deft hands, mounted and easily overcame, proving you the victor.")
        if int(dexterity) <= 90:
            dextreity = int(dexterity) + 10
            print("+10 dexterity")
    else:
        print("The wall was too high for you, blocking your path for the rest of time, what a shame.")
        exit()

elif int(choice) == 3:
    roll3 = random.randrange(0,int(intelligence))
    if roll3 > 20:
        print("The wall was no match for your mind, and was stumped by your queries, proving you the victor.")
        if int(intelligence) <= 90:
            intelligence =  int(intelligence) + 10
            print("+10 intelligence")
    else:
        print("The wall was suprisingly witty, condemning you to a fate of confusion and embarrassment, what a shame.")
        exit()

elif int(choice) == 4:
    roll4 = random.randrange(0,int(faith))
    if roll4 > 20:
        print("The wall saw the light, and is now a true believer, proving you the victor.")
        if int(faith) <= 90:
            faith = int(faith) + 10
            print("+10 faith")
    else:
        print("The wall's pagan ways proved unchangeable, slowly converting you instead, what a shame.")
        exit()

elif int(choice) == 5:
    roll5 = random.randrange(0,int(vitality))
    if roll5 > 20:
        print("The wall was impressed by your unmovable patience and will, proving you the victor.")
        if int(vitality) <= 90:
            vitality =  int(vitality) + 10
            print("+10 vitality")
    else:
        print("The wall was shamed by your impatience, standing steadfast where you could not, what a shame")
        exit()

elif int(choice) == 6:
    roll6 = random.randrange(0,int(attunement))
    if roll6 > 20 and int(strength) > 20:
        print("The wall broke under your projected force, an ethereal fist smashing it, proving you the victor.")
        if int(attunement) <= 90:
            attunement =  int(attunement) + 10
            print("+10 attunement")
    elif roll6 > 20 and int(intelligence) > 20:
        print("The wall was broken by your crystal sorceries, spearing it through and clearing the way, proving you the victor.")
        if int(attunement) <= 90:
            attunement =  int(attunement) + 10
            print("+10 attunement")
    elif roll6 > 20 and int(faith) > 20:
        print("The wall was blessed and comforted by your divine magic, proving you the victor.")
        if int(attunement) <= 90:
            attunement =  int(attunement) + 10
            print("+10 attunement")
    elif roll > 20 and int(attunement) > 30:
        print("The wall was confused and stunned by your splendid magic, proving you the victor.")
        if int(attunement) <= 90:
            attunement = int(attunement) + 10
            print("+10 attunement")
    else:
        print("The wall was unmoved by your paltry party tricks, what a shame.")
        exit()

else:
    print("What a shame")
    exit()

skillList()

print("The wall surpassed, your journey continues, for the next challenge draws near.")

print("Your next challenge came, in the form of the unexpected bridge, guarded by an immovable guardian, who asked you for a piece of knowledge.")
print("1. Explain the inticacies of pilates")
print("2. Explain the intricacies of climbing different architectural styles")
print("3. Enlighten him to the subtleties of integral calculus and its numerous ties to both differential calculus and algebra, and the numerous ways it can be applied in anyone's life, including his.")
print("4. Tell him a story from the great holy book, enlightening him to the glories of your lord.")
print("5. Explain your skin care and dietary routine")
print("6. Detail the lengthy history of Mortimer the Third, the famed sorcerer responsible for killing a Demon Lord and absorbing its hateful soul.")