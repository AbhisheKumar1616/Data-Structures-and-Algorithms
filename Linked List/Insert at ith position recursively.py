class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def takeInput():
    a=list(map(int,input("enter list: ").split()))
    i=int(input("enter Pos: "))
    d=int(input("enter data: "))
    head,tail=None,None
    for j in a:
        if j == -1:
            return None,None,None
        newnode=Node(j)
        if head is None:
            head=newnode
            tail=newnode
        else:
            tail.next=newnode
            tail=newnode

    return head,i,d
def length(head):
    c=0
    while head is not None:
        c+=1
        head=head.next
    return c
def insertith(head,i,d):
    if i==0:
        newnode=Node(d)
        newnode.next=head
        return newnode
    currhead=insertith(head.next,i-1,d)
    head.next=currhead
    return head

def printLL(head):
    while head is not None:
        print(head.data,end=" ")
        head=head.next

head,i,d=takeInput()
newhead=insertith(head,i,d)
printLL(newhead)
