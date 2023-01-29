import inspect
with open("E:\\Creative Works\\Visual Works\\Learning Works\\Python FIles\\Examine Modules.txt","w") as f:
    x=[1,24,32,14,23,234,23,432,4,234,234,23,432,432]
    src=inspect.getsource(sorted)
    f.writelines(src)
