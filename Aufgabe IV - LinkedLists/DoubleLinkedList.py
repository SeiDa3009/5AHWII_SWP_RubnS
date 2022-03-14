class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #---     ADD     ---

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, prev_node, new_data):
        new_node = Node(new_data)
        if prev_node is None:
            print("Error")
            return
        if prev_node.next is None:
            self.tail = new_node
        new_node.prev = prev_node
        if prev_node.next is not None:
            new_node.next = prev_node.next
            new_node.next.prev = new_node
        prev_node.next = new_node

    def insert_before(self, after_node, new_data):
        new_node = Node(new_data)
        if after_node is None:
            print("Error")
            return
        if after_node == self.head:
            self.head = new_node
        else:
            new_node.prev = after_node.prev
            after_node.prev.next = new_node
            after_node.prev = new_node
        new_node.next = after_node

    #---     DELETE     ---

    def delete_after(self, prev_node):
        if prev_node.next is None:
            print("Error")
            return
        if prev_node.next.next is None:
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node.next.prev = prev_node
            prev_node.next = prev_node.next.next

    def delete_before(self, before_node):
        if before_node.prev is None:
            print("Error")
            return
        if before_node.prev.prev is None:
            before_node.prev = None
            self.head = before_node
        else:
            before_node.prev = before_node.prev.prev
            before_node.prev.next = before_node

    #---     FIND     ---

    def find_by_value(self, node_to_find):
        current_node = self.head
        while current_node != None:
            if current_node.data == node_to_find:
                return True, current_node
            current_node = current_node.next
        return False, None

    def find_by_index(self, index):
        temp = self.head
        count = 0
        while temp.next is not None:
            count += 1
            if count == index:
                return temp
            temp = temp.next
            if temp.next is None:
                return self.tail
        return "Error"

    #---     SORT     ---

    def sort_ASC(self):
        if self.head is None:
            return
        else:
            current = self.head
            while current.next != None:
                index = current.next
                while index != None:
                    if current.data > index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next

    def sort_DESC(self):
        if self.tail is None:
            return
        else:
            current = self.tail
            while current.prev != None:
                index = current.prev
                while index != None:
                    if current.data > index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.prev
                current = current.prev

    #---     OUTPUT     ---

    def print_output(self):
        current_node = self.head
        output = []
        while current_node is not None:
            output.append(current_node.data)
            current_node = current_node.next
        return output, len(output)


def add_start(llst:DoubleLinkedList, length = None):
    import random
    if length is None:
        length = int(input("Length:"))
    for i in range(length):
        item = int(random.randint(0, 100))
        llst.append(item)


def input_data():
    return int(input("Value: "))

def input_position(llst):
    new_data = int(input("Target-Value: "))
    if llst.find_by_value(new_data)[0]:
       return llst.find_by_value(new_data)[1]
    else:
        return None

def input_values(llst:DoubleLinkedList, values:[]):
    for i in values:
        llst.append(i)

def output(llst):
    print("Length: ",llst.print_output()[1])
    print(llst.print_output()[0])

def task_24_02(llst:DoubleLinkedList()):
    add_start(llst)
    print(llst.print_output()[0])

    print("\nInsert_After")
    llst.insert_after(input_position(llst), input_data())
    output(llst)

    print("\nInsert_Before")
    llst.insert_before(input_position(llst), input_data())
    output(llst)

    print("\nDelete_After")
    llst.delete_after(input_position(llst))
    output(llst)

    print("\nDelete_Before")
    llst.delete_before(input_position(llst))
    output(llst)

    print("\nFind")
    print("Gefunden: ", llst.find_by_value(input_data())[0])

def task_03_03(llst:DoubleLinkedList()):
    add_start(llst)

    print("\nInsertionsort_ASC")
    llst.sort_ASC()
    output(llst)

    print("\nInsertionsort_DESC")
    llst.sort_DESC()
    output(llst)

def task_17_03(llst:DoubleLinkedList(), values:[]):
    import time
    time_start = time.time()
    input_values(llst, values)
    time_after_input = time.time()
    llst.sort_ASC()
    time_end = time.time()
    print("\nZeit-Messung [Double LinkedList]:")
    print("Ab Start: {:.4f} Sekunden".format(time_end-time_start))
    print("Ab Sortierung: {:.4f} Sekunden".format(time_end-time_after_input))

