import random
#x=["makemytrip","goibibo","saksham","gurleen","vishwas","manish"]
x=["cyclone","bed","pankaj","entered","sport","antartica","entered","chloroflorocarbon"]
#x=["antartica","entered","chloroflorocarbon"]
#x=["asssssssss"]
y=random.choice(x)
empty=[]


print "\n"
print "rules:: "
print ""
print "1. you will get a chance to enter letter same as length of word."
print "2. you loose one attempt,if incorrect letter entered or more than single letter entered"
print "3. only correct letters were shown to you, after that you have to guess the correct word from letters you have entered."
print "\n"

#print(y)

def space():
    for i in range(len(y)):
        print "_",
    print("\n")

def user_info():
    print "\n"
    user_name=raw_input("enter first name: ")
    print "\n"
    print("welcome {}".format(user_name))
    print "\n"

def next():
    for i in range(30):
        print "",

user_info()

for j in range(len(y)):
    empty.append(" ")

for i in range(len(y)):
    next()
    print "\n"
    print i+1
    print "\n"
    print(empty)
    print "\n"
    if " " in empty:
        user_input=raw_input("enter single char: ")
        if user_input:
            if len(user_input) == 1:
                if user_input in y and y.find(user_input) >= 0:
                    if empty[y.find(user_input)] == " " and  empty[y.rfind(user_input)] == " ":
                        for i,c in enumerate(y):
                            if c == user_input:
                                empty[i]=user_input
                        #empty[y.find(user_input)]=user_input
                        #empty[y.rfind(user_input)]=user_input
                    else:
                        print "place already taken"
                else:
                    print "entered letter not present in word"
            else:
                print "enter a single character"
        else:
            print "please enter something"
    else:
        break

print "\n"
if empty == list(y):
    next()
    print empty
    print "wow you got it"
    print "\n"
else:
    next()
    print "\n"
    print "your chances are complete"
    print "\n"
    print empty
    print "\n"
    user_input1=raw_input("Now guess the word : ")
    if user_input1==y:
        print "\n"
        print("wow you got it :D")
        print "\n"
    else:
        print "\n"
        print("better luck next time :/")
        print "\n"
