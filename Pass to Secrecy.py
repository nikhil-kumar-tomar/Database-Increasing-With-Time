import pickle
print("A Program to convert your Passwords to a Secret Language")
print("Try Me")
list=[]
while True:# Loop for User Input
    user1=str(input("Enter your Input here!:- "))
    list.append(user1)
    print("Want to Enter more Stuff?")
    x=str(input("Write Yes or No!:-"))
    if x.upper()=="NO":
        break
fick=open("h.txt", "wb")#Opening File
pickle.dump(list,fick)#Dumping the Contents in the file
fick.close()#CLosing the FIle
print("Do You want to see the secret code?")
while True: #User Choice to see the Secret Code or Not
    y=input("Write Yes or No Here!:- ")
    if y.upper()=="YES":
        x=open("h.txt","rb")
        for i in x:
            print(i)
            n=input("You can Quit Now")        
            x.close()
            exit()
            break
    elif y.upper()=="NO":
        print("Okay, Have a Great Day")
        exit()
    else: 
        print("Didn't got it Try again:-")
        continue
