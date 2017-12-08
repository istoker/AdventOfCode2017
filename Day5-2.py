def steps_until_out_of_instructions(steps, index, instruct):
    #print("steps: %d, index: %d" % (steps, index))
    steps = 0
    index = 0
    while index > -1 and index < len(instruct):
        new_index = index + instruct[index]
        if instruct[index] >= 3:
            instruct[index] -= 1
        else:
            instruct[index] += 1
        index = new_index
        steps += 1
    return steps

result = 0
instructions = []
with open("input-day5.txt") as rfile:
    instructions = [int(e.strip()) for e in rfile.readlines()]
print(steps_until_out_of_instructions(0, 0, instructions))