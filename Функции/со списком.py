import random
def random_list(long, a, b):
    lst = []
    for i in range(0, long, 1):
        lst.append(random.randint(a, b))

    return lst


new_lst = random_list(100, 0, 1)
new_lst2 = random_list(5, 0, 9)
print(new_lst)
print(new_lst2)