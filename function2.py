def average(a=9,b=1): # defult value
    print("the average is",((a+b)/2))
# average(2,4)
average()# if value given it will that value
#average(b=6, a=5) key value pair can do whatever
def average(*number):
    print(type(number))
    sum=0
    for i in number:
        sum=sum +i
    print("average is ",sum/len(number))
average(2,45)
def name(**name):
    print(type(name))
    print("Hello,", name["fname"],name["mname"],name["lname"])
name(mname=" ",fname="Jayant",lname="sinha")
def average(*number):
    print(type(number))
    sum=0
    for i in number:
        sum=sum +i
    return sum/len(number)
c=average(2,45)
print(c)