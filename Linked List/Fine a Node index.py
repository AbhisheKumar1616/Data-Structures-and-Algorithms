
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findNode(head, n):
    curr = head
    cnt = 0
    while curr is not None:
        if curr.data == n:
            return cnt
        cnt += 1
        curr = curr.next

    return -1