#code to check if the following number is a power of 2

num=("Please enter a number:")   #user input

if num==0:
    print("The number is not a power of 2")
else:
    while num!=1:
        if num%2!=0:
            print("The number is not a power of 2")
            break
        num=num//2
    else:
        print("The number is a power of 2")
