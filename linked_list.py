class Node:
    def __init__(self, init_key, init_data):
        self.key = init_key
        self.data = init_data
        self.next = None

    def getData(self):
        return self.data

    def setNext(self,new_next):
        self.next = new_next

    def __str__(self):
        node_print = "[Key:{},Data:{}]".format(self.key, self.data)
        return str(node_print)


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, key):
        # searches and returns node with corresponding key
        current = self.head
        found = False
        stop = False
        found_node = None
        while (current is not None) and not found and not stop:
            if current.getKey() == key:
                found = True
                found_node = current
            else:
                if current.getKey() > key:
                    stop = True
                else:
                    current = current.getNext()

        return found_node

    def add(self, key, data):
        # adds a node with key and data to the list
        current = self.head
        previous = None
        stop = False
        while (current is not None) and not stop:
            if current.getKey() > key:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(key, data)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.getNext()

        return count

    def __str__(self):
        print_list=""
        current = self.head
        while current is not None:
            print_list += str(current)
            print_list += "->"
            current = current.next

        print_list +="None"

        return print_list
    