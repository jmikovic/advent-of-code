import re

with open('day1_input.txt', 'r') as f:
    first_list, second_list = zip(*iter(
        (int(numbers[0]), int(numbers[1]))
        for line in f.readlines()
        if (numbers := re.split('\s+', line))
    ))

total_distance = sum(abs(f - s) for f, s in zip(sorted(first_list), sorted(second_list)))
similarity_score = sum((num * second_list.count(num) for num in first_list))

print(f'Total Distance: {total_distance}')
print(f'Similarity Score: {similarity_score}')
