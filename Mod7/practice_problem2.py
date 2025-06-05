'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
(reads the same forward and backward, ignoring case). The function should
returns either True or False.
'''

def is_palindrome(s):
    lower_s = s.lower()
    rev_s = lower_s[::-1]
    return(print(lower_s == rev_s))


moon = "moon"
is_palindrome(moon)
moom = "moom"
is_palindrome(moom)
Moom = "Moom"
is_palindrome(Moom)
