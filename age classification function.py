age = float(input("how old are you?:"))
if age < 0:
    print("not born yet!!")
elif age <= 12:
    print("child")
elif age <= 17:
    print("teenager")
elif age <= 64:
    print("adult")
elif age >= 65:
    print("senior citizen")
else:
    print("couldn't process")                