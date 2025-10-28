hour = int(input("Enter the hour (0-23) :"))
if hour <0 or hour > 23:
    print("ERROR! write a number and it should be in it's interval!!!'")
else:
    if 5<=hour<=11:
        print("MORNING")
    elif 12<=hour<=16:
        print("AFTERNOON")
    elif 17<=hour<=20:
        print("EVENING")
    else:
        print("NIGHT")            
        