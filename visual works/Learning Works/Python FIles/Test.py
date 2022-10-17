from operator import index
import pandas as pd
ip_list=[]
mac_list=[]
user_list=[]
# Input for 10 numbers and show even and odd

# lame=[]
# even=[]
# odd=[]

# for num in range(10):
#     inp=int(input("Enter your number: "))
#     lame.append(inp)
# for x in lame:
#     if x%2==0:
#         even.append(x)
#     else:
#         odd.append(x)
# print("Even number list is",even)
# print("Odd number list is",odd)


# rows=int(input("Enter your Rows: "))
# columns=int(input("Enter your columns: "))
# for tim in range(rows):
#     for l in range(columns):
#         print("*",end="")
#     print("\n")
    

def data():
    pd.options.display.max_rows = 50000
    df = pd.read_csv("E:\Creative Works\Visual Works\Learning Works\Python FIles\Server_Information.csv")
    mac_list.extend(df['Mac_Address'].tolist())
    ip_list.extend(df["IP_Address"].tolist())
    user_list.extend(df["SSH_Users"].tolist())
data()
print(mac_list)
print(ip_list)
print(user_list)
    