
from stack_and_queue.stack_and_queue import Stack

def validate_brackets(string:str):
    """declare some important variables and arrays"""
    stack_brackets = Stack()
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    brackets_in_stack = True

    for i in string:
        """push the values into the stack"""
        if i in open_brackets:
            stack_brackets.push(i)

        """pop values and and compare the strings"""
        if i in close_brackets:
            if not stack_brackets.is_empty():
                bracket_pop = stack_brackets.pop()
                if close_brackets.index(i) != open_brackets.index(bracket_pop):
                    # print('brecket_pop',bracket_pop)
                    # print('close_brackets.index(i)',close_brackets.index(i))
                    # print('open_brackets.index(bracket_pop)',open_brackets.index(bracket_pop))
                    return False
                else:
                    continue
            else:
                return False
    """Comparing to return boolen"""
    if brackets_in_stack:
        if stack_brackets.is_empty():
            return True
        else:
            return False

if __name__ == "__main__":
    print(validate_brackets('{}'))
    print(validate_brackets('{}(){}'))
    print(validate_brackets('()[[Extra Characters]]'))
    print(validate_brackets('(){}[[]]'))
    print(validate_brackets('{}{Code}[Fellows](())'))
    print(validate_brackets('[({}]'))
    print(validate_brackets('(]('))
    print(validate_brackets('{(})'))
    print(validate_brackets('{'))
    print(validate_brackets(')'))
    print(validate_brackets('[}'))