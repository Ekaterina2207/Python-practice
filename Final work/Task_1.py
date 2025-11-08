class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('Стек пуст!')
        return self.items.pop()

    def get_top(self):
        if self.is_empty():
            raise IndexError('Стек пуст!')
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class Task:
    def __init__(self, name : str, priority : int):
        self.name = name
        self.priority = priority

    def __str__(self):
        return f"{self.priority} {self.name}"

class TaskManager:
    def __init__(self):
        self.tasks = Stack()
        self.temp = Stack()
        self.task_names = {}

    def new_task(self, task: Task):
        if task.name in self.task_names:
            print(f'Задача {task.name} уже существует')
            return

        while not self.tasks.is_empty():
            top_task = self.tasks.get_top()
            if top_task.priority >= task.priority or self.tasks.is_empty():
                break
            else:
                self.temp.push(self.tasks.pop())
        self.tasks.push(task)
        self.task_names[task.name] = True

        while not self.temp.is_empty():
            self.tasks.push(self.temp.pop())


    def delete_task(self):
        if self.tasks.is_empty():
            raise IndexError('Стек пуст!')
        self.tasks.pop()

    def __str__(self):
        if self.tasks.is_empty():
            return 'Стек пуст'

        last_priority = None
        row = ""
        rows = []
        while not self.tasks.is_empty():
            top_task = self.tasks.pop()
            self.temp.push(top_task)
            if last_priority is None:
                row = f"{top_task.priority} {top_task.name}; "
            elif top_task.priority == last_priority:
                row += f"{top_task.name}; "
            else:
                rows.append(row)
                row = f"{top_task.priority} {top_task.name}; "
            last_priority = top_task.priority
        rows.append(row)
        while not self.temp.is_empty():
            self.tasks.push(self.temp.pop())

        return '\n'.join(rows)


a = Stack()
a.push(1)
a.push(2)
a.push(3)
print(a.items)
a.pop()
print(a.items)
a.pop()
print(a.items)
a.pop()
try:
    a.pop()
except IndexError as ie:
    print(ie)

print()

manager = TaskManager()
manager.new_task(Task("сделать уборку", 4))
print(manager)
print()
manager.new_task(Task("помыть посуду", 4))
print(manager)
print()
manager.new_task(Task("отдохнуть", 1))
print(manager)
print()
manager.new_task(Task("поесть", 2))
print(manager)
print()
manager.new_task(Task("сдать дз", 2))
print(manager)
print()
manager.new_task(Task("отдохнуть", 1))
print(manager)
print()

manager.delete_task()
print(manager)
print()
manager.delete_task()
print(manager)
print()
manager.delete_task()
print(manager)
print()
manager.delete_task()
print(manager)
print()


manager.delete_task()
print(manager)
print()

try:
    manager.delete_task()
except IndexError as ie:
    print(ie)
