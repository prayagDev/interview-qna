# Find duplicate elements in a list

data = [10, 20, 30, 10, 40, 20]
duplicates = []
seen = []
for item in data:
    if item in seen:
        duplicates.append(item)
    else:
        seen.append(item)
        
print(data)
print(duplicates)
print(seen)
