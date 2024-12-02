with open('./2023/4.input', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

splits = []
for line in lines:
    winning, numbers = line.split(':', 1)[1].split('|')
    wins = {int(w) for w in winning.strip().split(' ') if w}
    nums = {int(n) for n in numbers.strip().split(' ') if n}
    splits.append((wins, nums))

cards = {i: 1 for i in range(len(splits))}

print(
    'Part1: '
    f'{sum(
        2 ** (common - 1)
        for wins, nums in splits
        if (common := len(wins.intersection(nums)))
    )}'
)

for i, split in enumerate(splits):
    common = len(split[0].intersection(split[1]))
    multiplicator = cards[i]
    for j in range(1, common + 1):
        cards[i+j] += multiplicator

print(f'Part2: {sum(cards.values())}')
