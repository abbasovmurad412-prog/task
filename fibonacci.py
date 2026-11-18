
a = 0
b = 1

count = 0

while a < 989:
    print(a)

    a, b = b, a + b

    count += 1

print("Ədədlərin sayı:", count)
