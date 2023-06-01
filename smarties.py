# https://dmoj.ca/problem/ecoo15r1p1
smarties = {"orange": 0, "blue": 0, "green": 0, "yellow": 0, "pink": 0, "violet": 0, "brown": 0, "red": 0}
time = 0
# 10 test cases
for _ in range(10):
    while True:
        # Take input and increment value in smarties dict
        color = input()
        if color == "end of box":
            break
        smarties[color] += 1
    # Loop through smarties dict accumulating time
    for smartie in smarties:
        # 13 seconds per group of 7, including non-full group
        if smartie != "red" and smarties[smartie] != 0:
            time += (((smarties[smartie] // 7) + 1) * 13)
        # 16 seconds per individual red smartie
        elif smartie == "red":
            time += (smarties[smartie] * 16)
    # Print total time and reset dict + time variables
    print(time)
    smarties = {"orange": 0, "blue": 0, "green": 0, "yellow": 0, "pink": 0, "violet": 0, "brown": 0, "red": 0}
    time = 0
