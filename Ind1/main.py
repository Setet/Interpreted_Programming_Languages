import random


def Main():
    Lifting_height = 0
    Numbers = []
    Aboba = []
    a = random.randint(0, 100)
    print("Полученно "+str(a)+" чисел.")
    for i in range(a):
        Numbers.append(random.randint(0, 1000))
    Numbers[-1] = 0
    # print(Numbers)

    for i in range(len(Numbers)-1):
        if Numbers[i] < Numbers[i + 1]:
            Lifting_height += 1
        else:
            Aboba.append(Lifting_height)
            Lifting_height = 0
    # print(Aboba)

    max_number = max(Aboba)
    print("Наибольшеая высота подъёма:", max_number)

Main()