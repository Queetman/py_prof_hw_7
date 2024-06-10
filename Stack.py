class Stack:
    def __init__(self):
        self.arr = []

    # проверка стека на пустоту. Метод возвращает True или False.
    def isEmpty(self) -> bool:
        pass

    # добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self, element) -> None:
        self.arr.insert(0, element)

    # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self) -> None:
        if len(self.arr) == 0:
            pass
        else:
            self.arr.pop(0)

    # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self) -> None:
        if len(self.arr) == 0:
            return None
        else:
            return self.arr[0]

    # возвращает количество элементов в стеке.
    def size(self) -> int:
        return len(self.arr)
