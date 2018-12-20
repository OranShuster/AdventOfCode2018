# def parse(data):
#     children, metas = data[:2]
#     data = data[2:]
#     scores = []
#     totals = 0
#
#     for i in range(children):
#         total, score, data = parse(data)
#         totals += total
#         scores.append(score)
#
#     totals += sum(data[:metas])
#
#     if children == 0:
#         return (totals, sum(data[:metas]), data[metas:])
#     else:
#         return (
#             totals,
#             sum(scores[k - 1] for k in data[:metas] if k > 0 and k <= len(scores)),
#             data[metas:],
#         )
#
#
# if __name__ == "__main__":
#     with open("input.txt") as file:
#         data = [int(x) for x in file.read().split()]
#
#
# total, value, remaining = parse(data)
#
# print("part 1:", total)
# print("part 2:", value)


def parse(data, totals):
    childs, metas = data[:2]
    data = data[2:]
    values = []

    for child in range(childs):
        data, total, value = parse(data, 0)
        totals += total
        values.append(value)

    metas_vals = data[:metas]
    totals += sum(metas_vals)
    data = data[metas:]
    if childs == 0:
        value = sum(metas_vals)
        return data, totals, value
    else:
        value = sum([values[k-1] for k in metas_vals if k <= len(values)])
        return data, totals, value


if __name__ == "__main__":
    with open("input.txt") as file:
        data = [int(x) for x in file.read().strip().split()]
    totals = 0
    data, total, score = parse(data, totals)
    print(total)
    print(score)