import itertools
mylist = [1, 4, 8, 2, 5, 7, 3, 9, 5, 1, 10, 11, 12]
for x,y in itertools.combinations(mylist, 2):
    print(x,y)
    