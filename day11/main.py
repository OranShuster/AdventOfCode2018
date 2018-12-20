ser = 9005


def cell_power_level(x, y):
    rack_id = x + 10
    power_level = rack_id * y + ser
    power_level *= rack_id
    power_level = power_level // 100 % 10
    return power_level - 5


if __name__ == "__main__":
    power_levels = {}
    strips = {}
    strip_size = 3
    board_size = 300
    for x in range(1, board_size + 1):
        for y in range(1, board_size + 1):
            power_levels[(x, y)] = cell_power_level(x, y)

    # for y in range(1, board_size + 1):
    #     for x in range(1, board_size + 1):
    #         print(f"{power_levels[(x,y)]} ", end="")
    #     print("")
    #
    # print("strips")
    #
    # for y in range(1, board_size + 1 - 2):
    #     for x in range(1, board_size + 1):
    #         print(f"{strips[(x,y)]} ", end="")
    #     print("")

    m = -100
    mxy = 0
    for size in range(1, board_size + 1):
        for x in range(1, board_size + 1):
            for y in range(1, board_size + 1 - (size - 1)):
                p = 0
                for s in range(size):
                    p += power_levels[(x, y + s)]
                strips[(x, y)] = p

        for y in range(1, board_size + 1 - (size - 1)):
            current_power_level = 0
            for s in range(size):
                current_power_level += strips[(1 + s, y)]
            if m < current_power_level:
                m = current_power_level
                mxy = (1, y, size)
            for x in range(2, board_size + 1 - (size - 1)):
                current_power_level -= strips[(x - 1, y)]
                current_power_level += strips[x + size - 1, y]
                if m < current_power_level:
                    m = current_power_level
                    mxy = (x, y, size)

    print("max")
    print(m)
    print(mxy)
