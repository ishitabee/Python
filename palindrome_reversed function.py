#palindrome using for loop


word=str(input("Enter a word or a number to check if it is a palindrome: ").lower())
word_reverse = ""                           #empty string to store the reversed string

for i in word:
        word_reverse = i + word_reverse    #reversing the string

if word == word_reverse:
    print(word, "is a palindrome.")        #checking if the original string is equal to the reversed string
else:
    print(word, "is not a palindrome.")    #if not equal, then it is not a palindrome