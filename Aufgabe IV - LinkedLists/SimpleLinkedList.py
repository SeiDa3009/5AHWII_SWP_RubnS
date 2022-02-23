class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        return

class SimpleLinkedList:
    def __init__(self):
        self.head = None

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

    def delete_after(self, previous_node):
        if previous_node is None:
            print("Error ... Node not in List")
            return

        if previous_node.next is None:
            return

        temp = previous_node.next
        after_del_node = temp.next
        previous_node.next = after_del_node

    def find(self, node_to_find):
        current_node = self.head
        while current_node != None:
            if current_node.data == node_to_find:
                return True, current_node
            current_node = current_node.next
        return False, None

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


def add_start(llst):
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


def print_output(llst):
    llst.print_length()
    llst.print_list()


def print_main_oppo():
    print("Delete [d]")
    print("Find [f]")
    print("Add [a]")
    print("Exit [any other]")


def print_del_oppo():
    print("After [a]")


def print_add_oppo():
    print("After [a]")
    print("Push [p]")


def add_menu():
    repeat = True
    answer = None
    print_add_oppo()
    while(repeat):
        answer = input("Answer: ").lower()
        if answer == "a":
            llst.insert_after(input_position(llst))
            print_output(llst)
        elif answer == "p":
            llst.push(input_data())
            print_output()
        else:
            repeat = False
            menu()


def delete_menu():
    repeat = True
    answer = None
    print_del_oppo()
    while(repeat):
        answer = input("Answer: ").lower()
        if answer == "a":
            llst.delete_after(input_position(llst))
            print_output(llst)
        else:
            repeat = False
            menu()


def menu():
    repeat = True
    answer = None
    print_main_oppo()
    while(repeat):
        answer = input("Answer: ").lower()
        if answer == "d":
            delete_menu()
        elif answer == "f":
            print("Gefunden: ", llst.find(input_data())[0])
        elif answer == "a":
            add_menu()
        else:
            repeat = False
            print("Exit")


if __name__ == '__main__':
    llst = SimpleLinkedList()
    add_start(llst)
    llst.print_list()
    menu()








