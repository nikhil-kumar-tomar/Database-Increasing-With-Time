import pyperclip
print("""Email Starters:-
         1.Composing Email
         2.Replying Email
         3.Composing Files Email""")
Option=str(input("Enter Serial No your Choice:- "))
if Option=="1":
    x=("Greetings,\nThis Email is in regard with\n\n\n[Body]\n\n\nSincerely,\nNikhil Kumar Tomar" )
    print(x)
    pyperclip.copy(str(x))
elif Option=="2":
    x=("Greetings,\nThank You for the Reply Regarding\n\n\n[Body]\n\n\nSincerely,\nNikhil Kumar Tomar" )
    print(x)
    pyperclip.copy(str(x))
elif Option=="3":
    print("Is this Email for Replying or Composing \n")
    y=str(input("Press 1 for Replying & 2 for Composing:- "))
    if y=="1":
        x=("Greetings,\nThank You for the Reply Regarding\n\n\n[Body]\n\n\nAll the files regarding this email are attached below\n\nSincerely,\nNikhil Kumar Tomar" )
        print(x)
        pyperclip.copy(str(x))
    elif y=="2":
        x=("Greetings,\nThis Email is in regard with\n\n\n[Body]\n\n\nAll the files regarding this email are attached below\n\nSincerely,\nNikhil Kumar Tomar" )
        print(x)
        pyperclip.copy(str(x))
