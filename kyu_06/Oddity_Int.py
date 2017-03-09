def find_it(seq):
    # print([ seq.count(my_char) % 2 for my_char in seq])
    return seq[[int(seq.count(my_char) % 2) for my_char in seq].index(1)]

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
