class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        return

class SimpleLinkedList:
    def __init__(self):
        self.head = None

    #---     ADD     ---

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, previous_node, new_data):
        if previous_node is None:
            print("Error ... Node not in List")
            return
        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    #---     DELETE     ---

    def delete_after(self, previous_node):
        if previous_node is None:
            print("Error ... Node not in List")
            return

        if previous_node.next is None:
            return

        temp = previous_node.next
        after_del_node = temp.next
        previous_node.next = after_del_node

    #---     FIND     ---

    def find_by_value(self, node_to_find):
        current_node = self.head
        while current_node != None:
            if current_node.data == node_to_find:
                return True, current_node
            current_node = current_node.next
        return False, None

    #---     OUTPUT     ---

    def print_length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        print("Length: ", count)

    def print_list(self):
        current_node = self.head
        output = []

        while current_node is not None:
            output.append(current_node.data)
            current_node = current_node.next
        print(output)

    #---     SUM     ---

    def sum(self):
        key = self.head
        sum = 0
        while key.next is not None:
            sum = key.data + sum
            key = key.next
        return sum

def add_start(llst, length = None):
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


def print_output(llst):
    llst.print_length()
    llst.print_list()

def task_24_02(llst:SimpleLinkedList):
    add_start(llst)
    print_output(llst)

    print("\nInsert_After")
    llst.insert_after(input_position(llst), input_data())
    print_output(llst)

    print("\nDelete_After")
    llst.delete_after(input_position(llst))
    print_output(llst)

    print("\nPush")
    llst.push(input_data())
    print_output(llst)

    print("\nFind")
    print("Gefunden: ", llst.find_by_value(input_data())[0])











