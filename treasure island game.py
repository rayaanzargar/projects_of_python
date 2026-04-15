print("Welcome to Kashmir, a paradise on earth!")
print("Your goal here is to find the great 'Kounsarnag Lake'.")
Place = input('We have booked you bus tickets. Where would you like to go? "Jammu" or "Kashmir"?: ').upper()
if Place == "KASHMIR":
    print("HAHA! Great choice. You surely know places.")
else:
    print("HAHA! You are a fucking idiot. Jammu is not even close to Kashmir")
District = input("Oh No! The bus driver died. Take the control of the bus. You are provided with the map, Take a look of the map and see which district looks most promising (Hint it starts with 'K').: ").upper()
if District == "KULGAM":
    print("Great! You found the place.....But we have a problem...!")
else:
    print("HAHA! Cant even read the map properly, you dont deserve to be here :0")
Contact = input("OH NO! Wait! You are stuck here due to bad weather. Contact a person ASAP to save yourself from the strome. Who would you like to call? 'Rayaan', 'Mehbooba Mufti' or 'Omar abdullah': ").upper()
if Contact == "RAYAAN":
    print(''' Great choice! You are now safe. The great Rayaan made sure you reach the home safely. Thank him!;)''')
    thankyou = input("Thank him here: ")
    print("Haha! it was fun. No worries")
elif Contact == "OMAR ABDULLAH":
    print("Oh NO! He couldn't even save his to'op(cap) :(")
elif Contact == "MEHBOOBA MUFTI":
    print("Oh No! You choose the wrong person :( Shes busy calling modi ")
else:
    print("You choose a wrong person. sorry, you are dead")



