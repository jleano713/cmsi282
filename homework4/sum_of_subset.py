def sum_of_subset(lst,target):
    lst.sort()
    length = len(lst)+1
    target +=1
    subset = [[0 for i in xrange(length)] for j in xrange(target)]
    for i in xrange(length):
        subset[0][i] = True
    for i in xrange(1,target):
        subset[i][0] = False
    for i in xrange(1,target):
        for j in xrange(1,length):
            subset[i][j] = subset[i][j-1]
            if (i >= lst[j-1] and lst[j-1] >= 0):
                subset[i][j] = subset[i][j] or subset[i-lst[j-1]][j-1]
    return subset[target-1][length-1]

list = [1, 3, 2, 4, -2, 1, 7]
print(sum_of_subset(list, 12))
print(sum_of_subset(list, 100))
print(sum_of_subset(list, -1))
