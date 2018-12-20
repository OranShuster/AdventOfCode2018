from collections import deque, defaultdict

if __name__ == "__main__":
    scores = defaultdict(int)
    circle = deque([0])
    max_players = 430
    max_marble = 71588 * 100
    for marble in range(1, max_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    print(max(scores.values())) if scores else 0
