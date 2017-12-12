def parse_line(line):
    splitted_program_and_stack = line.split('->')
    program = splitted_program_and_stack[0].split(' ')[0]
    stack = []
    if len(splitted_program_and_stack) > 1:
        stack = [elem.strip() for elem in splitted_program_and_stack[1].split(',')]
    return [program], stack

def get_programs_and_stack():
    programs = []
    stack = []
    with open('input-day7.txt') as rfile:
        for line in rfile.readlines():
            programs[len(programs):], stack[len(stack):] = parse_line(line)
    return programs, stack

def main():
    programs, stack = get_programs_and_stack()
    for program in programs:
        if program not in stack:
            print(program)
            break

if __name__ == '__main__':
    main()