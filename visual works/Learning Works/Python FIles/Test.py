# Input for 10 numbers and show even and odd

lame=[]
even=[]
odd=[]

for num in range(10):
    inp=int(input("Enter your number: "))
    lame.append(inp)
for x in lame:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print("Even number list is",even)
print("Odd number list is",odd)

