
pin=12345
tries=0

print("WELCOME TO THE BANK OF MITCHELL.")
while tries<3:
    entry=int(input("ENTER YOUR PIN: "))
    tries +=1
    if entry ==pin:
        print("PIN ACCEPTED. YOU NOW ACESS TO YOUR ACCOUNT.")
        break
    else:
        print("INCORRECT PIN. TRY AGAIN.")