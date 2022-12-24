# is_empty - проверка стека на пустоту. Метод возвращает True или False.
# push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
# pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
# peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
# size - возвращает количество элементов в стеке.


class Stack:

    def __init__(self, entity:str):
        self.entity = list(entity)
        pass

    def is_emty(self):
        if self.entity:
            return True
        else:
           return False

    def push(self, new:str):
        self.entity.append(new)


    def pop(self):
        pop = self.entity.pop()
        return pop

    def peek(self):
        return self.entity[-1]

    def size(self):
        return len(self.entity)




