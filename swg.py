import random
false =True
while(false):
    print(" Choose any one of the following for yourself:\n 0.Snake \t 1.Water \t 2.Gun")
    u=["snake","water","gun"]
    u=int(input("enter your option:"))
    print(" Choose any one of the following for your opponent/system\n 0. \t 1. \t 2.")
    s=["snake","water","gun"]
    s=random.randint(0,3)
    while(u<3):
    #     if(s==0):
    #         if(u==0):
    #             print(f"\"draw\" ")
    #             break
    #         elif(u==1):
    #             print(f"\"loose\" ")
    #             break
    #         elif(u==2):
    #             print(f"\"win\" ")
    #             break
    #         else:
    #             pass
    #         break
    #     elif(s==1):
    #         if(u==0):
    #             print(f"\"win\" ")
    #             break
    #         elif(u==1):
    #             print(f"\"draw\" ")
    #             break
    #         elif(u==2):
    #             print(f"\"loose\" ")
    #             break
    #         else:
    #             pass
    #         break
    #     elif(s==2):
    #         if(u==0):
    #             print(f"\"loose\" ")
    #             break
    #         elif(u==1):
    #             print(f"\"win\" ")
    #             break
    #         elif(u==2):
    #             print(f"\"draw\"")
    #             break
    #         else:
    #             pass
    #         break
        if (s==u):
            print("Draw")
            break
        elif( (s==0 and u==1) or (s==1 and u==2) or (s==2 and u==0) ):
            print("loose") 
            break
        else:
            print("Win")
            break
    print(f"since system has choosen:{s}")
else:
    print("enter :the number b/w 0-2")
