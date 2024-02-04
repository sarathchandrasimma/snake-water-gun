print(" Choose any one of the following for yourself:\n 0.Snake \t 1.Water \t 2.Gun")
u=["snake","water","gun"]
u=int(input("enter your option:"))
print(" Choose any one of the following for your opponent/system\n 0. \t 1. \t 2.")
s=["snake","water","gun"]
s=int(input("enter your option:"))
while(u<3):
    if(s==0):
        if(u==0):
            print(f"\"draw\" ")
            break
        elif(u==1):
            print(f"\"loose\" ")
            break
        elif(u==2):
            print(f"\"win\" ")
            break
        else:
            pass
        break
    elif(s==1):
        if(u==0):
            print(f"\"win\" ")
            break
        elif(u==1):
            print(f"\"draw\" ")
            break
        elif(u==2):
            print(f"\"loose\" ")
            break
        else:
            pass
        break
    elif(s==2):
        if(u==0):
            print(f"\"loose\" ")
            break
        elif(u==1):
            print(f"\"win\" ")
            break
        elif(u==2):
            print(f"\"draw\"")
            break
        else:
            pass
        break
else:
    print("enter the number b/w 0-2")