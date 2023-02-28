h=float(input("Your height in m:"))
w=float(input("Your weight in kg:"))
bmi=w/h**2
print(f" your BMI is {bmi}")
if bmi<18.5:
     print("underweight")
elif bmi==18.5 or bmi<=24.9:
    print("normal weight")
elif bmi==25.0 or bmi<=29.9:
    print("overweight")
else:
    print("obese")