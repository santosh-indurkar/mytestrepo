"""Finding max number in list."""
mylist = [12, 2, 33, 5, 17, 3, 55]

# 1: Using max()
def max_number(lis):
    return max(mylist)


result = max_number(mylist)
print(result)

# 2: Using sorted() or list.sort()
def max_number_2(lis):
    # return sorted(lis)[-1]
    lis.sort()
    return lis[-1]


result = max_number_2(mylist)
print(result)

# 3: Using for loop
def max_number_3(lis):
    lismax = lis[0]
    for x in lis:
        if x > lismax:
            lismax = x

    return lismax


result = max_number_3(lis=mylist)
print(result)
