number = int(input("Enter a number: "))

if number == 0:
    print("Binary version = 0")
else:
    binary_num= ""  #empty string to store binary number

    while number > 0:
        if number % 2 == 0:
            binary_num =  binary_num + "0"
        else:
            binary_num = binary_num + "1"

        #floor division to obtain quotient only
        number = number // 2

    #[::-1] is used to reverse the string
    print("Binary version=", binary_num[::-1])