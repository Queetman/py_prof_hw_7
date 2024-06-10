input = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}',
    '}{}',
    '{{[(])]}}',
    '[[{())}]'

]


def get_balance(data) -> bool:
    sums = [0, 0, 0]

    for d in data:
        if d == '(' or d == ')':
            sums[0] += appender('(', ')', d)

        if d == '[' or d == ']':
            sums[1] += appender('[', ']', d)

        if d == '{' or d == '}':
            sums[2] += appender('{', '}', d)

    return True if sums == [0, 0, 0] else False


def appender(s1, s2, data):
    if s1 == data:
        return 1
    if s2 == data:
        return -1


for i in range(len(input)):
    if get_balance(input[i]) == True:
        print(f'скобка {i} сбалансирована')
    else:
        print(f'скобка не {i} сбалансирована')
