from collections import defaultdict

from toposort import toposort_flatten


with open('2024/day5-input.txt', 'r') as f:
    rules, manuals = f.read().split('\n\n')

rule_map = defaultdict(set)
for rule in [rule.strip().split('|') for rule in rules.split('\n')]:
    rule_map[int(rule[0])].add(int(rule[1]))
manuals = [[int(page) for page in manual.split(',')] for manual in manuals.split('\n') if manual]

correct_manuals_mid = 0
incorrect_manuals = []
for manual in manuals:
    for i, p in enumerate(manual[:-2]):
        if p in rule_map and not set(manual[i+1:]).issubset(rule_map[p]):
            incorrect_manuals.append(manual)
            break
    else:
        correct_manuals_mid += manual[len(manual) // 2]

print(correct_manuals_mid)
corrected_manuals_mid = 0

for manual in incorrect_manuals:
    order = toposort_flatten({p: rule_map[p] for p in manual})
    corrected_manual = [p for p in order if p in manual]
    corrected_manuals_mid += corrected_manual[len(corrected_manual) // 2]

print(corrected_manuals_mid)
