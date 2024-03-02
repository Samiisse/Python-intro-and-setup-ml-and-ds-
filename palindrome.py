#Create a Python function to check if a given string is a palindrome

def palindrome(str):
    if (str == str[::-1]):
        return ('This is a palindrome!')
    else:
        return ('This is not a palindrom!')

#Enter input str
str = input('Enter a palindrome word: ')
print (palindrome(str))

