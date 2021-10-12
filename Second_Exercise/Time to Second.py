print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('Hi')
print('HINT: Enter Time in this Format pls => Hour:Minute:Second')
print('---------------------------------------------')
Temp=input("ENTER YOUR TIME:")

Hour , Minute , Sec = Temp.split(":")
Second = int(Hour)*3600 + int(Minute)*60 + int(Sec)
print("\nYour Entered Time converted to Second!!! =>",Second)

print('\n   ---- MADE BY MAJID-MSH :)----\n\t<----GOODLUCK---->\n--------------------------------------------')