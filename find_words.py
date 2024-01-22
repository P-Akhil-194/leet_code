words = ["cat","bt","hat","tree"]
chars = "atach"
l = 0
for i in words:
    r = 0
    n = chars
    for j in i:
        if j not in n:
            r = 0
            break
        else:
            n = n.replace(j,'',1)
            r = 1

    if r == 1:
        l += len(i)
print(l)