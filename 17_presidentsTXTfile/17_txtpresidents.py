with open('States.txt', 'r') as file:
    highest_population = 0
    highest_population_state = ''

    for line in file:
        parts = line.split()
        if parts[1] == 'Midwest':
            population = int(parts[2])
            if population > highest_population:
                highest_population = population
                highest_population_state = parts[0]
    print('Highest population state in the Midwest is:', highest_population_state, highest_population)

print(" ")

from collections import defaultdict

with open('USPresidents.txt', 'r') as file:
    presidents_by_state = defaultdict(list)
    for line in file:
        parts = line.split()
        presidents_by_state[parts[0]].append(parts[1])

    most_presidents_state = ''
    most_presidents_count = 0
    for state, presidents in presidents_by_state.items():
        if len(presidents) > most_presidents_count:
            most_presidents_count = len(presidents)
            most_presidents_state = state

    num_presidents = len(presidents_by_state[most_presidents_state])

    print('The state with the most presidents is', most_presidents_state, 'with', num_presidents, 'presidents:')
    for president in presidents_by_state[most_presidents_state]:
        print(president.replace('_', ' '))

print(" ")

presidents_by_state = defaultdict(list)
with open('USPresidents.txt') as f:
    for line in f:
        state, president = line.strip().split()
        president = president.replace('_', ' ')
        presidents_by_state[state].append(president)

state_counts = {state: len(presidents_by_state[state]) for state in presidents_by_state}

populous_states = {'CA', 'TX', 'FL', 'NY', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI'}

president_birth_states = populous_states & set(presidents_by_state.keys())

president_birth_state_counts = {state: state_counts[state] for state in president_birth_states}

print(f"{len(president_birth_states)} of the 10 high population states have had presidents born in them:")
for state, count in sorted(president_birth_state_counts.items()):
    print(f"{state} {count}")

'''Execution results:
Highest population state in the Midwest is: IL 12802000

The state with the most presidents is VA with 8 presidents:
George Washington
James Madison
James Monroe
John Tyler
Thomas Jefferson
William Henry Harrison
Woodrow Wilson
Zachary Taylor

8 of the 10 high population states have had presidents born in them:
CA 1
GA 1
IL 1
NC 2
NY 5
OH 7
PA 1
TX 2'''

print("end of program.")