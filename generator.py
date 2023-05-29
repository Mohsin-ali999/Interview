# def evenNumbers(n):
#     i=1
#     while n:
#         yield 2*i
#         i+=1
#         n-=1

# it=evenNumbers(10)
# even_lst=[]
# while True:
#     try:
#         even_lst.append(next(it))
#     except StopIteration:
#         break

# print(even_lst)


#Without Loop

def even_numbers(n):
    i=1
    while n:
        yield 2*i
        i+=1
        n-=1

it= even_numbers(10)
lst =[]
# while True:
lst.append(next(it))
lst.append(next(it))
    
print(lst)
