class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.before = None
        return

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def list_length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count

    def add_item_in_list(self, item):

        if  isinstance(item, Node):
            if self.head is None:
                self.head = item
                item.before = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.before = self.tail
                self.tail = item
        return

    def output_list(self):
        current_node = self.head
        output = []
        while current_node is not None:
            output.append(current_node.data)
            current_node = current_node.next
        print(output)

    def unordered_search(self, value):
        current_node = self.head
        node_id = 1
        results = []

        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)

            current_node = current_node.next
            node_id = node_id + 1
        return results

    def remove_list_item_by_id(self, item_id):
        current_id = 1
        current_node = self.head

        while current_node is not None:
            before_node = current_node.before
            next_node = current_node.next

            if current_id == item_id:
                if before_node is not None:
                    before_node.next = next_node
                    if next_node is not None:
                        next_node.before = before_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.before = None
                return
            current_node = next_node
            current_id = current_id + 1
        return


#other Methods
def add_random():
    import random
    length = int(input("Length?:"))
    for i in range(length):
        node_input = Node(random.randint(0,100))
        llst.add_item_in_list(node_input)


def output():
    print("lenght: %i" % llst.list_length())
    llst.output_list()


def delete():
    item_id = int(input("Which item should be removed?: "))
    llst.remove_list_item_by_id(item_id)
    output()


def search():
    item_value = int(input("Which value should be searched?: "))
    print(llst.unordered_search(item_value))


def menu():
    repeat = True
    answer = None
    while(repeat):
        answer = input("Delete [d] - Search[s] - Exit[any]").lower()
        if answer == "d":
            delete()
        elif answer == "s":
            search()
        else:
            repeat = False
            print("Exit")


if __name__ == '__main__':
    # Double-LinkedList:
    # Basic:
    llst = LinkedList()
    add_random()
    output()

    # Addition
    menu()