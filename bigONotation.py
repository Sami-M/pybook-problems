#
# Self Check
# Write two Python functions to find the minimum number in a list. The first 
# function should compare each number to every other number on the list. 
# O(n2)O(n2). The second function should be linear O(n)O(n).
#

def minInListQuadratic(array):
    for n in array:
        for j in array:
            if(j < n):
                f = j
    return f

def minInListLinear(array):
    f = array[0]
    for n in array[1:]:
        if(f > n):
            f = n
    return f

print(minInListQuadratic([4,2,6,5,5]))
print(minInListLinear([4,2,6,5,5]))