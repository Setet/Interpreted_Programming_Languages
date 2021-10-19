def Main():
    Lifting_height = 0
    List = []
    file = open(r'C:\Users\user\Desktop\ps.txt')
    s = file.readline()
    Numbers = s.split(",")
    print(Numbers)

    for i in range(len(Numbers) - 1):
        if float(Numbers[i]) > float(Numbers[i + 1]):
            Lifting_height += 1
            if int(i) == range(len(Numbers) - 2):
                List.append(Lifting_height + 1)
        else:
            List.append(Lifting_height)
            if Lifting_height > 0:
                List.append(Lifting_height + 1)
                Lifting_height = 0
    List.sort(reverse=True)
    j = 0
    while j < len(List):
        if List[j] == 0:
            del List[j]
        j += 1

    f = open(r'C:\Users\user\Desktop\ps2.txt')
    f.write(str(List))


Main()
