"""
lists, .append(), .sort(), indexing lists
"""

x = ['Adrien', 'Jeremy', 'Hannah']
x.append('Harold') #.append adds whatever is inside the bracket into the list

print(x)

x = [5,2,5,4,7,3,8]
#x.sort() - sorts the list from smaller to bigger
print(x)

#if we only want to print 2
print(x[1]) # 5 is the 0th item, 2 is the 1st item, 5 is the 3rd item

x[2] = 7 #modify the 2nd item, which is 5, into 7
print(x)

print(x[1:3])