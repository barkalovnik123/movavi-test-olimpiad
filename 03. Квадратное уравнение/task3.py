a, b, c = map(int, input().split())
d = b ** 2 - 4 * a * c
if a == 0:
    if b == 0:
        if c == 0:
            print(-1)
        else:
            print(0)
    else:
        print(1)
        print(-c / b)
elif d < 0:
    print(0)
elif d == 0:
    print(1)
    print(-b/(2*a))
else:
    print(2)
    print((-b - d ** 0.5) / (2 * a))
    print((-b + d ** 0.5) / (2 * a))