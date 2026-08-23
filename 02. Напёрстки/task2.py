a = input()
l, c, r = 1, 0, 0
for e in a:
    if e == "A":
        l, c = c, l
    elif e == "B":
        r, c = c, r
    else:
        l, r = r, l
if l: print(1)
if c: print(2)
if r: print(3)