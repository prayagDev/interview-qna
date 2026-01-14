# Check if a string is a palindrome

def get_rev_str(my_str):
    rev_str = ""
    for ch in my_str:
        rev_str = ch + rev_str
    return rev_str
    
my_str = "naman"
rev_str = get_rev_str(my_str)
print(my_str==rev_str)
