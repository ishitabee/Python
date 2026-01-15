# program is to remove the duplicates from an input string.

phrase=input("Please enter a phrase: \n")  # user input
new_phrase=""                            # empty string to store new result
for char in phrase:                      #char = every alphabet of the phrase
    if char not in new_phrase:           #phrase will continue without the duplicate alphabet
        new_phrase+=char  
print("The new phrase without any duplicate alphabet will be",new_phrase)              