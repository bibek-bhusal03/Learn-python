a = [[1, 2], [3, 4, 5], [5]]

count = 0
for elements in a:
    for ele in elements:
        count += 1

print(count)

a = [[1, 2], [3, 4, 5], [5]]
count = sum(len(elements) 
            for elements in a)
print(count)  # 6
