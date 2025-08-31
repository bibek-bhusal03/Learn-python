# Sort the dictionary based on the value (try both ascending and descending order)
 
a = {'a': 4, 'b': 1, 'c': 45}

b = list(a.items())

n = len(b)
for i in range(n):
    max_index= i
    for j in range(i+1, n):
        if b[j][1] > b[max_index][1]:
            max_index =j 
        
        b[i], b[max_index] = b[max_index], b[i]

print(b)



