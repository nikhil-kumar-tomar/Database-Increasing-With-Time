f=open("h.txt","w")
while True:
    Start_Number=int(input("Enter your Starting Number(Atleast 10 Digits):- "))
    if len(str(Start_Number))==10:
        break
    else:
        print("Write again") 
        continue
while True:
    Limit_Number=int(input("Enter your Limiting Number:- "))
    if len(str(Limit_Number))>=10 :
        break
    else:
        print("Write Again") 
        continue
Tuple=[]
while Start_Number<=Limit_Number:
    print(Start_Number)
    Tuple.append(Start_Number)
    Start_Number+=1
for x in Tuple:
    f.write(str(x)+'\n')
f.close()