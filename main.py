import random

# ************************

n = int(input("Введите количество слов\n"))
i = 1
S = ""

while i <= n:
    w = str(input("Введите слово\n"))
    S = S + w + " "
    i += 1

print(S)

# ************************

w = ""
S = ""

while w != "stop":
    w = str(input("Введите слово\n"))
    if w != "stop":
        S = S + w + " "

print(S)

# ************************

w = str(input("Введите слово\n"))

if "ф" in w:
    print("Ого! Это редкое слово!")
else:
    print("Эх, это не очень редкое слово...")

# ************************

score = 0
mistake = 0

while mistake < 3:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = a + b
    print(a, " + ", b, " = ?")
    d = int(input())

    if c == d:
        print("Правильно!")
        score += 1
    else:
        print("Ответ неверный")
        mistake += 1

print("Игра окончена. Правильных ответов: ", score)

# ************************
