# https://dmoj.ca/problem/ecoo15r1p1
smarties = {"orange": 0, "blue": 0, "green": 0, "yellow": 0, "pink": 0, "violet": 0, "brown": 0, "red": 0}
time = 0
for _ in range(10):
    while True:
        color = input()
        if color == "end of box":
            break
        smarties[color] += 1
    for smartie in smarties:
        if smartie != "red" and smarties[smartie] != 0:
            time += (((smarties[smartie] // 7) + 1) * 13)
        elif smartie == "red":
            time += (smarties[smartie] * 16)
    print(time)
    smarties = {"orange": 0, "blue": 0, "green": 0, "yellow": 0, "pink": 0, "violet": 0, "brown": 0, "red": 0}
    time = 0
