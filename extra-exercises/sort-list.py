# Sort the 2d list in descending order based on second element
 
 
# answer: [[5, 6], [3, 4], [1, 2]]


a = [[3, 4], [1, 2], [5, 6]]
b=a[:]

n = len(b)
for i in range(n):
    max_idx = i
    for j in range(i+1, n):
          if b[j][-1] > b[max_idx][-1]:
            max_idx = j
    
    b[i], b[max_idx] = b[max_idx], b[i]

print(b)

#old / wrong answer
# largest = 0 
# for element in a:
#         second_element = element[len(element)-1]
#         if(second_element> largest):
#             largest= second_element
#             b.insert(0,element)
#         else:
#               b.append(element)

# print(b)                    
 