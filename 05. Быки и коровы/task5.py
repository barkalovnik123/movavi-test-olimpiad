a,b = input().split()
 
buki = 0
korovi = 0
 
for s in a:
    if s in b:
        if a.index(s) == b.index(s):
            buki += 1
        else:
            korovi += 1
print(buki,korovi)    