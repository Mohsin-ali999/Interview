import copy

a =[1,2,3,[4,5]]

print(a)
b= copy.copy(a)  # shallow copy
c= copy.deepcopy(a) # deep copy


a[3][0] = 45

print(a)
print(b)
print(c)