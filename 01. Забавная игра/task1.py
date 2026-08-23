m = int(input())

# Двоичная запись без префикса '0b'
s = bin(m)[2:]
n = len(s)

# Находим максимальное значение среди всех циклических сдвигов
max_val = 0
for i in range(n):
    # Циклический сдвиг: берём суффикс и приклеиваем префикс
    rotated = s[i:] + s[:i]
    val = int(rotated, 2)
    if val > max_val:
        max_val = val
        
print(max_val)
