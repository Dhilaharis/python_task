weight=int(input("Please enter your current earth weight:\t"))
print("I have information for the following planets:")
print("     1.Venus     2.Mars      3.Jupiter")
print("     4.Saturn    5.Uranus    6.Neptune")
visit=int(input("Which planet are you visiting?\t"))
Venus=0.78*weight
Mars=0.39*weight
Jupiter=2.65*weight
Saturn=1.17*weight
Uranus=1.05*weight
Neptune=1.23*weight
if visit==1:
    print(f"Your weight would be {Venus} pounds on the planet")
elif visit==2:
    print(f"Your weight would be {Mars} pounds on the planet")
elif visit==3:
    print(f"Your weight would be {Jupiter} pounds on the planet")
elif visit==4:
    print(f"Your weight would be {Saturn} pounds on the planet")
elif visit==5:
    print(f"Your weight would be {Uranus} pounds on the planet")
elif visit==6:    
    print(f"Your weight would be {Neptune} pounds on the planet")
else:
    print("Enter the valid number")    
