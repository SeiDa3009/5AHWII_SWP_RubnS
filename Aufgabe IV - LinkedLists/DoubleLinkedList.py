class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("Error ... Node not in List")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def insert_before(self, after_node, new_data):
        if after_node is None:
            print("Error ... Node not in List")
            return

        new_node = Node(new_data)
        if after_node == self.head:
            new_node.prev = None
            self.head = new_node
        else:
            new_node.prev = after_node.prev.next
        new_node.next = after_node
        after_node.prev.next = new_node
        after_node.prev = new_node


    def delete_after(self, prev_node):
        if prev_node.next is None:
            return
        temp = prev_node.next
        after_del_node = temp.next
        prev_node.next = after_del_node
        after_del_node.prev = prev_node


    def delete_before(self, before_node):
        if before_node.prev is None:
            print("Error")
            return
        last = before_node.prev
        if last.prev is None:
            print("Error")
            return
        before_last = last.prev
        before_node.prev = before_last
        before_last.next = before_node


    def find(self, node_to_find):
        current_node = self.head
        while current_node != None:
            if current_node.data == node_to_find:
                return True, current_node
            current_node = current_node.next
        return False, None

    def print_output(self):
        current_node = self.head
        output = []
        while current_node is not None:
            output.append(current_node.data)
            current_node = current_node.next
        return output, len(output)


def add_start():
    import random
    length = int(input("Length:"))
    for i in range(length):
        item = int(random.randint(0, 100))
        llst.append(item)


def input_data():
    return int(input("Value: "))


def input_position(llst):
    new_data = int(input("Target-Value: "))
    if llst.find(new_data)[0]:
       return llst.find(new_data)[1]
    else:
        return None


def output():
    print("Length: ",llst.print_output()[1])
    print(llst.print_output()[0])


if __name__ == '__main__':
    llst = DoubleLinkedList()
    add_start()
    print(llst.print_output()[0])

    print("\nInsert_After")
    llst.insert_after(input_position(llst), input_data())
    output()

    print("\nInsert_Before")
    llst.insert_before(input_position(llst), input_data())
    output()

    print("\nDelete_After")
    llst.delete_after(input_position(llst))
    output()

    print("\nDelete_Before")
    llst.delete_before(input_position(llst))
    output()

    print("\nFind")
    print("Gefunden: ", llst.find(input_data())[0])