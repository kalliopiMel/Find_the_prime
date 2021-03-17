# https://www.tutorialspoint.com/divmod-in-python-and-its-application
# https://www.w3schools.com/python/python_operators.asp

continued="y"
while continued=="y":
    x = 3
    prime = True
    print("Give me the number you would like to check.")
    number = int(input())
    if number==2 :
        prime=True
    elif number%2==0:
        prime=False
        print(number, "was divided by", 2)
    else:
        while x**2 <=number:
            if number % x == 0:
                prime = False
                print(number,"was divided by",x)
                break
            else: x+=1
    if prime == False:
        print(number, " is not a prime")

    else:
        print(number, " is a prime")
    print("If you want to check another number press y (yes) alse press n (no)")
    continued = input()

#or number==3 or number==5 or number==7 or number==11
