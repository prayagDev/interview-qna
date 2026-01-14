# Count character frequency in a string

my_str = "naman"

freq = {}

for ch in my_str:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
        
print(freq)
