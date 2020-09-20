class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):  
        self.head = None


# 2.1 Remove dups
    def removedups(self,head):
        current = second = self.head
        while current is not None:
            while second.next is not None:   
                if second.next.data == current.data:   
                    second.next = second.next.next   
                else:
                    second = second.next   
            current = second = current.next

# 2.2 Return kth to Last
    def returnkth(self, head, k):
        a = b = self.head
        i = 1
        while i<k:
            a = a.next
            i += 1
        
        while a.next is not None:
            b = b.next
            a = a.next
        
        return b.data

    def printLinked(self,head):
        curr = self.head
        while(curr!=None):
            print(curr.data)
            curr = curr.next

# 2.3 Delete middle node
    def delmid(self, n):
        n.data = n.next.data
        n.next = n.next.next

        return n

# 2.4 Partition
    def partition(self, head, k):
        l1 = self.head
        l2 = self.head
        l3 = self.head
        L1 = LinkedList()
        L2 = LinkedList()
        i = 1

        while i<=k:
            if i == k:
                l3.data = l1.data
                l3.next = l1.next
            else:
                l1.data = l1.next.data
                l1.next = l1.next.next

        while l1.next is not None:

            if l1.data < k:
                l2.data = l1.data
                l2.next = l1.next 
            else:
                l1.data = l1.next.data
                l1.next = l1.next.next
        
        
# 2.5 Sum List:
    def sumoflist(self, fir, sec):
        a = []
        b = []

        fir = self.head
        sec = self.head

        while fir is not None:
            a.append(fir.data)
            fir = fir.next
            print(a)
        
        while sec is not None:
            b.append(sec.data)
            sec = sec.next
            print(b)
        
        fi = [str(i) for i in a]
        se = [str(i) for i in b]

        fi = int("".join(fi))
        se = int("".join(se))

        su = fi+se

        return su


if __name__ == "__main__":
    LL = LinkedList()
    n = Node(2)
    n.next = Node(3)
    h = n.next.next = Node(4)
    n.next.next.next = Node(5)
    n.next.next.next.next = Node(6)
    n.next.next.next.next.next = Node(7)

    Fir = LinkedList()
    Sec = LinkedList()

    f = Node(2)
    f.next = Node(3)
    f.next.next = Node(5)

    s = Node(6)
    s.next = Node(8)
    s.next.next = Node(9)

    Fir.head = f
    Sec.head = s

    print(LL.sumoflist(Fir, Sec))


    k = 5

    LL.head = n
    LL.delmid(h)

    LL.printLinked(n)


