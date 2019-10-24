# Program to print out whether this string is a palindrome or not
__author = "Mohamed Abouelsaadat"

Word = input("Please enter a word: ")
Wrd = str(Word)
# Reversing string
WrdRev = Wrd[::-1]
if(Wrd == WrdRev):
    print("Palindrome")
else:
    print("Not palindrome")