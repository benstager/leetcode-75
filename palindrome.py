# check if input string is a palindrome

def palindrome(s:str) -> bool:
    #create new string of only alphanumeric characters, check if same as reversed
    s_new = ''

    for i in s:
        if i.isalnum():
            s_new += i.lower()
    
    #check by reversing string using list comprehension
    if s_new == s_new[::-1]:
        return True
    
    return False

s = "A man, a plan, a canal: Panama"
print(palindrome(s))