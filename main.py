from stack import Stack
from data import arr



def check_parenthesis(line):

    suport_stack_1 = Stack('')
    suport_stack_2 = Stack('')
    suport_stack_3 = Stack('')

    key = { '}':1, '{':1, ')':2,'(':2, ']':3, '[':3}
    suport_dict = {1: suport_stack_1, 2: suport_stack_2, 3: suport_stack_3}
    
    stack = Stack(line)


    while stack.is_emty():

        el = stack.pop()

        if el in ['}',')',']']:
            suport_dict[key[el]].push(el)
        if el in ['{', '(', '[']:
            if suport_dict[key[el]].is_emty():
                suport_dict[key[el]].pop()
           

    if not suport_dict[1].is_emty() and not suport_dict[2].is_emty() and not suport_dict[3].is_emty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"

    
def test():
    assert check_parenthesis(arr[0]) == "Сбалансированно"
    assert check_parenthesis(arr[1]) == "Сбалансированно"
    assert check_parenthesis(arr[2]) == "Сбалансированно"
    assert check_parenthesis(arr[3]) == "Несбалансированно"
    assert check_parenthesis(arr[4]) == "Несбалансированно"
    assert check_parenthesis(arr[5]) == "Несбалансированно"


if __name__ == '__main__':

    test()