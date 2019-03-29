import random

CHARACTER_COUNT = 5

NAMES = ['John', 'William', 'James', 'George', 'Charles', 'Frank', 'Joseph', 'Henry', 'Robert', 'Thomas', 'Edward',
         'Harry', 'Walter', 'Arthur', 'Fred', 'Albert', 'Samuel', 'Clarence', 'Louis', 'David', 'Mary', 'Anna', 'Emma',
         'Elizabeth', 'Margaret', 'Minnie', 'Ida', 'Bertha', 'Clara', 'Alice', 'Annie', 'Florence', 'Bessie', 'Grace',
         'Ethel', 'Sarah', 'Ella', 'Martha', 'Nellie', 'Mabel', 'Eyram']


def random_matching(names, character_count):
    matching_list = []

    group_number = len(names)/character_count

    for group in range(group_number):
        generate_random_names = random.sample(names, k=character_count)
        matching_list.append((group+1, generate_random_names))

        names = [item for item in names if item not in generate_random_names]

    return matching_list



