import ArrayList
import SimpleLinkedList
import DoubleLinkedList

def create_values():
    import random
    values = []
    for i in range(10000):
        values.append(random.randint(0,100000))
    return values

if __name__ == '__main__':
    llst = DoubleLinkedList.DoubleLinkedList()
    alst = ArrayList.ArrayList()
    sllst = SimpleLinkedList.SimpleLinkedList()

    #Task for 24.02 [Douple LinkedList]:
    #DoubleLinkedList.task_24_02(llst)
    #SimpleLinkedList.task_24_02(sllst)

    #Task for 03.03:
    #DoubleLinkedList.task_03_03(llst)

    #Task for 10.03:
    #ArrayList.task_10_03(alst)

    #Task for 17_03:
    values = create_values()
    ArrayList.task_17_03(alst, values)
    DoubleLinkedList.task_17_03(llst, values)

