def Func1(a, b, n):
    print("Числа,в деапазоне от " + str(a) + " до " + str(b) + " чья сумма цифр равна " + str(n) + " :")
    for i in range(a, b):
        summ = 0
        for digit in str(i):
            summ += int(digit)
        if summ == n:
            print(i)

def Func2(a, b):
    print("Числа,в деапазоне от " + str(a) + " до " + str(b) + " которые являются полиндромами :")
    for i in range(a, b):
        if str(i) == str(i)[::-1]:
            print(i)

def Func3(a, b):
    print("Числа,в деапазоне от " + str(a) + " до " + str(b) + " в которых ровно 3 одинаковые цифры :")
    for i in range(a, b):
        mi = map(str, range(0, 10))
        for num in mi:
            if str(i).count(num) == 3:
                print(i)

def Func4():
    spisok = [1, 2, 3, 4, 3, 2, 5, 2, 3, 5, 2, 3]

    if spisok[0] > spisok[1]:
        check = True
        c = 0
    else:
        check = False
        c = 1

    for i in range(len(spisok)-1):

        if check:
            if spisok[i] < spisok[i + 1]:
                c += 1
                check = False
        else:
            if spisok[i] > spisok[i + 1]:
                c += 1
                check = True
    print("Колличество монотонных фрагментов = %d" % c)

def Func5():
    spisok = [1, 3, 2, 5, 6, 5]
    count = 0

    for i in range(len(spisok) - 2):
        if spisok[i] < spisok[i+1] and spisok[i+1] > spisok[i+2]:
            count += 1
    print("Колличество локальных максимумов = %d" % count)

def Func6():
    spisok = [1, 3, 1, 1, 5, 3, 1, 1, 1, 2, 1]
    min = 0

    for i in range(len(spisok) - 2):
        if spisok[i] < spisok[i+1] > spisok[i+2]:
            a = i

def Func7():
    kid1 = set()
    kid2 = set()
    a = int(input("Кол-во цветов для ребёнка 1 : "))
    b = int(input("Кол-во цветов для ребёнка 2 : "))

    for i in range(int(a)):
        kid1.add(input("%d Цвет для ребёнка 1 : " % i))
    for i in range(int(b)):
        kid2.add(input("%d Цвет для ребёнка 2 : " % i))

    rez = set.intersection(kid1,kid2)
    print("Цвета ", str(rez))
    print("Кол-во детей = %d" % len(rez))

def Func8():
    interLang = set()
    unionLang = set()
    curLang = set()

    n = int(input("Задайте кол-во детей : "))
    a = int(input("Задайте кол-во языков для ребенка : "))

    if n > 1:
        for i in range(a):
            interLang.add(input("%d Язык который знает ребенок № " % i))
    n -= 1
    unionLang = set.union(unionLang, interLang)

    while n > 0:
        a = int(input("Задайте кол-во языков для нового ребенка : "))
        for i in range(a):
            curLang.add(input("%d Язык который знает ребенок № " % i))
        n -= 1
    interLang = set.intersection(curLang, interLang)
    unionLang = set.union(curLang, unionLang)
    set.clear(curLang)

    print("Языки, которые знает хоть 1 : ", str(unionLang))
    print("Языки, которые знает каждый : ", str(interLang))

Lesson1 = [Func1, Func2, Func3]
Lesson2 = [Func4, Func5, Func6]
Lesson3 = [Func7, Func8]