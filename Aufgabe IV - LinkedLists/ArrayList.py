import random

class ArrayList:
    def __init__(self):
        self.list = []

    #---     ADD     ---

    def append(self, new_data):
        self.list.append(new_data)

    def push(self, new_data):
        self.list.append(0, new_data)

    def insert_after(self, index, new_data):
        self.list.insert(index+1, new_data)

    def insert_before(self, index, new_data):
        if index - 1 >= 0:
            self.list.insert(index-1, new_data)

    #---     DELETE     ---

    def delete_after(self,index):
        if len(self.list) > index + 1:
            self.list.pop(index+1)

    def delete_before(self, index):
        if index - 1 >= 0:
            self.list.pop(index-1)

    #---     FIND     ---

    def find(self, value):
        index = []
        for i in range(0, len(self.list)):
            if self.list[i] == value:
                index.append(i)
        return "Value {} at index {}".format(self.list[i], index)


    #---     SORT     ---

    def sort_ASC(self):
        for i in range(1, len(self.list)):
            key = self.list[i]
            j = i-1
            while j >= 0 and key < self.list[j]:
                self.list[j+1] = self.list[j]
                j -= 1
            self.list[j+1] = key

    def sort_DESC(self):
        for i in range(1, len(self.list)):
            key = self.list[i]
            j = i-1
            while j >= 0 and key > self.list[j]:
                self.list[j+1] = self.list[j]
                j -= 1
            self.list[j+1] = key

    #---     OUTPUT     ---

    def print_output(self):
        return self.list, len(self.list)

def add_start(alst:ArrayList, length = None):
    import random
    if length is None:
        length = int(input("Length:"))
    for i in range(length):
        item = int(random.randint(0, 100))
        alst.append(item)

def input_values(alst:ArrayList, values:[]):
    for i in values:
        alst.append(i)

def output(alst:ArrayList):
    print(alst.print_output()[0])
    print(alst.print_output()[1])

def task_10_03(alst:ArrayList):
    add_start(alst, 5)
    output(alst)

    print("\nInsert_After")
    alst.insert_after(2, 3)
    output(alst)

    print("\nInsert_Before")
    alst.insert_before(3, 5)
    output(alst)

    print("\nDelete_After")
    alst.delete_after(2)
    output(alst)

    print("\nDelete_Before")
    alst.delete_before(3)
    output(alst)

    print("\nFind")
    print("Gefunden: ", alst.find(3))

    print("\nInsertionsort_ASC")
    alst.sort_ASC()
    output(alst)

    print("\nInsertionsort_DESC")
    alst.sort_DESC()
    output(alst)

def task_17_03(alst:ArrayList, values:[]):
    import time
    time_start = time.time()
    input_values(alst, values)
    time_after_input = time.time()
    alst.sort_ASC()
    time_end = time.time()
    print("Zeit-Messung [ArrayList]:")
    print("Ab Start: {:.4f} Sekunden".format(time_end-time_start))
    print("Ab Sortierung: {:.4f} Sekunden".format(time_end-time_after_input))







