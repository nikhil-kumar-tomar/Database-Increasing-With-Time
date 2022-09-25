f=open("h.txt","w")
Start_Number=int(input("Enter your Starting Number:- "))
Limit_Number=int(input("Enter your Limiting Number:- "))
Tuple=[]
if Limit_Number>=Start_Number:
    while Start_Number<=Limit_Number:
        print(Start_Number)
        Tuple.append(Start_Number)
        Start_Number+=1
    for x in Tuple:
        f.write(str(x)+'\n')
    f.close()
elif Limit_Number<=Start_Number:
    while Limit_Number<=Start_Number:
        print(Start_Number)
        Tuple.append(Start_Number)
        Start_Number-=1
    for x in Tuple:
        f.write(str(x)+'\n')
    f.close()
else:print("Read file Name")