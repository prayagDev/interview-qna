# Reverse a string without using built-in functions

def get_rev_str(my_str):
    rev_str = ""
    for ch in my_str:
        rev_str = ch + rev_str
    return rev_str
    
print(get_rev_str("abcd"))
