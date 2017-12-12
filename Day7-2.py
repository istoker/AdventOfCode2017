class Program(object):
    name = ""
    weight = 0
    stack = []

    def __init__(self, name, weight=0, stack=[]):
        self.name = name
        self.weight = weight
        self.stack = stack

    def get_stack_weight(self):
        if len(self.stack) == 0:
            return self.weight
        else:
            return self.weight + sum([elem.get_stack_weight() for elem in self.stack])
    
    def is_stack_balanced(self):
        if len(stack) == 0:
            return true, None
        else:
            weights = [elem.get_stack_weight() for elem in self.stack]
            '''check if weights are all the same'''


def main():
    pass

if __name__ == '__main__':
    main()