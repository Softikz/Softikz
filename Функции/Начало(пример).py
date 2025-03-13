
def find_min(a,b):
    if a <b :
        return a
    elif b < a:
        return b
    else:
        return a,b

result = find_min(int(input()),int(input()))
print(result)
print(find_min(9,7))
