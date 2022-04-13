#https://www.acmicpc.net/problem/2164
#
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class queue:
    def __init__(self):
        self.front = Node(None)
        self.rear = Node(None)
        self.front.next = self.rear.prev
        self.size = 0
    def qsize(self):
        return self.size
    def enqueue(self, data):
        NewNode = Node(data)
        NewNode.prev = self.rear
        self.rear = NewNode
        NewNode.next = self.rear
        self.size+=1
    def dequeue(self):
        if self.size > 0:
            temp = self.front.data
            self.front = self.front.next
            self.size-=1
            return temp


def solve():
    N = int(input())
    numbers = [n for n in range(1,N+1)]
    Queue = queue()
    for x in numbers:
        Queue.enqueue(x)
    i = 0
    while (Queue.size > 0):
        i+=1
        temp = Queue.dequeue()
        if i%2 == 0:
            Queue.enqueue(temp)

    return print(temp)

if __name__ == "__main__":
    solve()