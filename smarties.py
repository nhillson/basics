# https://dmoj.ca/problem/ecoo15r1p1
# 10 test cases
for _ in range(10):
    smarties = {}
    time = 0
    color = ""
    while color != "end of box":
        # Take input and increment value in smarties dict
        color = input()
        if color in smarties:
            smarties[color] += 1
        elif color != "end of box":
            smarties[color] = 1
    # Loop through smarties dict accumulating time
    for smartieColor, smartieCount in smarties.items():
        # 13 seconds per group of 7, including non-full group
        if smartieColor != "red":
            time += (((smartieCount // 7) + 1) * 13)
        # 16 seconds per individual red smartie
        elif smartieColor == "red":
            time += (smartieCount * 16)
    # Print total time
    print(time)
