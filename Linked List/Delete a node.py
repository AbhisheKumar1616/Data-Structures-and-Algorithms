
# Approach 1
from sys import stdin


# Following is the Node class already written for the Linked List.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteNode(head, pos):
    if head is None:
        return head

    if pos == 0:
        return head.next

    count = 0
    currHead = head
    while currHead is not None and count < (pos - 1):
        count += 1
        currHead = currHead.next

    if (currHead is None) or (currHead.next is None):
        return head

    currHead.next = currHead.next.next

    return head


# Taking Input Using Fast I/O.
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


# To print the linked list.
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# Main.
t = int(stdin.readline().strip())

while t > 0:
    head = takeInput()
    pos = int(stdin.readline().rstrip())

    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1


# approach 2
from sys import stdin


# Following is the Node class already written for the Linked List.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):
    c = 0
    while head is not None:
        c += 1
        head = head.next
    return c


def deleteNode(head, pos):
    # Write your code here.
    c = length(head)
    if pos < 0 or pos > c:
        return head
    prev = None
    curr = head
    j = 0
    while j < pos:
        j += 1
        prev = curr
        curr = curr.next
    if pos == c:
        curr = None
        return head
    if prev is not None:
        prev.next = curr.next
    else:
        head = curr.next
    return head


# Taking Input Using Fast I/O.
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


# To print the linked list.
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# Main.
t = int(stdin.readline().strip())

while t > 0:
    head = takeInput()
    pos = int(stdin.readline().rstrip())

    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1
