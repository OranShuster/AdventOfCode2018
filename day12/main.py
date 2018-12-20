max_gen = 50000000000 + 1
cells_count = 5000
starting_index = cells_count // 2
if __name__ == "__main__":
    rules = {}
    with open("input.txt") as file:
        s = file.readline().strip().split("initial state: ")[1]
        file.readline()
        lines = file.readlines()

    for line in lines:
        splits = line.strip().split(" => ")
        rules[splits[0]] = splits[1]

    st = ["." for i in range(cells_count)]
    for ind, pot in enumerate(s):
        st[starting_index + ind] = s[ind]
    state: str = "".join(st)

    # print(f"{gen}  {state}")
    gen = 0
    last_counter = 0
    counter = 0
    for gen in range(1, 2001):
        next_state = ""
        for ind, pot in enumerate(state):
            window = state[ind - 2 : ind + 3]
            if len(window) < 5:
                next_state += pot
            else:
                if window in rules:
                    next_state += rules[window]
                else:
                    next_state += "."
        state = next_state
        # print(f"{gen}  {state}")
        last_counter = counter
        counter = 0
        for ind, pot in enumerate(state):
            real_ind = ind - starting_index
            if pot == "#":
                counter += real_ind

        print(f"{gen} {counter} change {counter-last_counter}")

    print(f"{counter + (50000000000 - 2000) * 81}")
