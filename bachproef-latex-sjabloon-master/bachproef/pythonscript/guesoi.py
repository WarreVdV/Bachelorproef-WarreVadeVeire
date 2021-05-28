import random
  
def raadspel():
    print(f"Welkom bij het raad spel! Kies een getal tussen 1 en 100: ")
    startSpel = input("Als je klaar bent om te beginnen, druk 'j'. Als je wilt stoppen, druk 'n'. ").capitalize()

    if startSpel == "J":
        print(f"{startSpel}")
        lageRand = 1
        hogeRand = 100
        feedback = ""
        teller = 0
        while(feedback!="G"):
            print(f"Ik denk dat jouw getal ligt tussen {lageRand} en {hogeRand}. Ik heb momenteel {teller} keer geraden.")
            gok = random.randint(lageRand, hogeRand)
            feedback = input(f"Is jouw getal hoger (H) of lager (L) dan {gok}? Of heb ik het getal geraden? (G)?: ").capitalize()
            if feedback == "L":
                hogeRand = gok-1
            elif feedback == "H":
                lageRand = gok+1
            teller=teller+1
        print(f"Yay, we hebben jouw getal ({gok} geraden) in {teller} beurten!")
    
    print("Vaarwel :)")
    
raadspel()