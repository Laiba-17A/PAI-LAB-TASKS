def is_palindrome(text):
    text = text.casefold()  # convert to lowercase
    words = text.split()    # split by spaces
    text = ''.join(words)   # join without spaces

    reverse = ''
    for ch in text:
        reverse = ch + reverse  # build reversed string

    if text == reverse:
        return True
    else:
        return False

# Take input from the user
word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print("Yes, it is a palindrome!")
else:
    print("No, it is not a palindrome.")
