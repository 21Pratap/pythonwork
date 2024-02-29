a=int(input("write a your 1st no:"))
b=int(input("write a your 2st no:"))
c=int(input("write a your 3st no:"))

if(a<b and b>c):
    print("2nd is the greatest of the three number",b)
elif(a<c and b<c):
    print("3rd is the greatest of the three number",c)
else:
    print("1st is the greatest of the three number",a)
