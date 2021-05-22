y=int(input("Enter the year you want check whether the year is leap year or not\n"))
if y%4==0 and y%100!=0:
    print(y,"is leap year")
elif y%400==0:
    print(y,"is leap year")
else:
    print(y,"is not a leap year")
