'''
a='''This program will find out whether the given word is a palindrome or not. 
      A palindrome is a word that reads the same backward as forward.'''
print(a)
word = input("Enter a word: ").lower()

reversed_word = word[::-1]

if word == reversed_word:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
'''