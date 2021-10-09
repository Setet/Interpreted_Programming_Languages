def Main():
    Lifting_height = 0
    Numbers = []
    List = []
    d = 1
    s1 = 0
    print("Вводите числа через строку\n")
    while True:
        if d > s1:
            Numbers.append(int(input()))
            if Numbers[d - 1] == 0:
                break
            else:
                d += 1
    print("Полученно " + str(d) + " чисел.")
    Numbers[-1] = 0

    for i in range(len(Numbers) - 1):
        if Numbers[i] < Numbers[i + 1]:
            Lifting_height += Numbers[i + 1] - Numbers[i]
        else:
            List.append(Lifting_height)
            Lifting_height = 0

    max_number = max(List)
    print("Наибольшеая высота подъёма:", max_number)


Main()
