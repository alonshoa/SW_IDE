l1 = [('i1','j1'),('i2','j2'),('i3','j3'),('i4','j4'),('i7','j7')]
l2 = [('i1','j1'),('i2','j2'),('i3','j3'),('i5','j5'),('i6','j6')]

def num_mutual_contain(l1,l2):
    l1_set = set(l1)
    l2_set = set(l2)
    return l1_set.intersection(l2_set)

print(num_mutual_contain(l1,l2))
