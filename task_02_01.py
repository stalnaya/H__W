def is_palindrome(s):
    s1=str(s)
    x= s1[::-1].lower().replace(' ', '')
    y= s1.lower().replace(' ', '')
    return x==y
