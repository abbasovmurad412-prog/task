
number = int(input("Müsbət tam ədəd daxil edin: "))

steps = 0

print(number, end="")

while number != 1:

    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1

    print(" ->", number, end="")
    steps += 1

print()
print("Addımların sayı:", steps)

