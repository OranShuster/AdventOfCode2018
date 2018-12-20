import re

if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.read().strip().split("\n")
    lines = [[int(i) for i in re.findall(r"-?\d+", l)] for l in lines]
    I = 10300

    for l in lines:
        l[0] += l[2] * I
        l[1] += l[3] * I
    for i in range(I, I + 700):
        maxx = max(x for x, y, vx, vy in lines)
        maxy = max(y for x, y, vx, vy in lines)
        minx = min(x for x, y, vx, vy in lines)
        miny = min(y for x, y, vx, vy in lines)
        # print(maxx - minx, maxy - miny)
        if minx + 100 >= maxx and miny + 100 >= maxy:
            print(i)
            for y in range(miny - 1, maxy + 1):
                for x in range(minx - 1, maxx + 1):
                    if [x, y] in [[px, py] for px, py, _, _ in lines]:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print("")
            input()

        for l in lines:
            l[0] += l[2]
            l[1] += l[3]
