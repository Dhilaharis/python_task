name=input("Hey,what's your name? (Sorry, I keep forgetting.)\t")
age=int(input(f"OK,{name} .how old are you?\t"))
if age<16:
    print("You can't drive.",name)
elif age==16 or age==17:
    print("You can drive but not vote,",name)
elif age==18 or age<=24:
    print("You can vote but not rent a car,",name)
else:
    print("You can do pretty much anything,",name)
