a = [[1, 2], [3, 4], [5, 6]]
 
# reverse the element in the list
# answer: [[2, 1], [4, 3], [6, 5]]


b=[]
for sub in a:
    b.append(sub[::-1])

print(b)