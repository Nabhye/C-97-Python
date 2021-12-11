#python basic
x = "hello"
print(x)

myName = "Nabhye"
myAge = 14
print(myName)
print(myAge)

myFriendList = ["shreyash", "chandan", "Tahseen"]
print(myFriendList)

y = input("Enter Your Age: ")
print(y)

age = int(input("Enter Your Age: "))
if (age > 18) :
    print("You Are An Adult You Can Vote")
elif (age > 12): 
    print("You Are Teenager")
else :
    print("You are a kid")

myFriendList = ["shreyash", "chandan", "Tahseen"]
for friend in myFriendList:
    print(friend)

count = 500
while (count >=100):
    print(count)
    count = count-1
