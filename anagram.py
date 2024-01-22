from collections import Counter
def anagram(s:str, t:str) -> str:
    # create dictionary where letter:count

    s_dict = dict(Counter(s)) 
    t_dict = dict(Counter(t))
    
    # equate the two dictionaries
    if s_dict == t_dict:
        return True
    return False

s = 'books'
t = 'skoob'

print(anagram(s,t))

