def deserialize_state(banks):
    return " ".join(list(map(str, banks)))

def spread_even_number_of_blocks(banks, remaining_blocks):
    number_to_spread = remaining_blocks // len(banks)
    banks = [elem + number_to_spread for elem in banks]
    remaining_blocks -= number_to_spread * len(banks)
    return banks, remaining_blocks

def reallocate_blocks(banks):
    remaining_blocks = max(banks)
    index = banks.index(max(banks))
    banks[index] = 0
    index += 1
    banks, remaining_blocks = spread_even_number_of_blocks(banks, remaining_blocks)
    while remaining_blocks != 0:
        if index >= len(banks):
            index = 0
        banks[index] += 1
        remaining_blocks -= 1
        index += 1
    return banks

def reallocate_routine(banks):
    previous_states = []
    while deserialize_state(banks) not in previous_states:
        previous_states[len(previous_states):] = [deserialize_state(banks)]
        banks = reallocate_blocks(banks)
        #print(previous_states)
    return deserialize_state(banks), previous_states

def get_number_of_steps_in_loop(banks):
    current_state, previous_states = reallocate_routine(banks)
    return len(previous_states) - previous_states.index(current_state)

#print(reallocate_routine([0, 2, 7, 0]))
with open("input-day6.txt") as rfile:
    print(get_number_of_steps_in_loop([int(x) for x in rfile.readline().strip().split("\t")]))
