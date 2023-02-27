name=input("Hey what's your name?\t")
age=float(input(f"OK,{name},how old are you?"))
if age<16:
    print(f"you can't drive,{name}")
    print(f"you can't vote ,{name}")
    print(f"you can't rent a car,{name}")
elif age<18:
    print(f"you can't vote,{name}")
    print(f"you can't rent a car,{name}")
elif age<25:
    print(f"you can't rent a car,{name}")
else:
    print(f"you can do anything that's legal.")
