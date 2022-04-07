#https://www.acmicpc.net/problem/1158
from re import M


MAX_QSIZE = N

class CircularQueue:
    
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.queue = [None] * MAX_QSIZE
    def isempty(self):
        return (self.front == self.rear)
    def isfull(self):
        return (self.front == (self.rear+1) % MAX_QSIZE)
    def enqueue(self, data):
        if not self.isfull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.queue[self.rear] = data
    def dequeue(self):
        if not self.isempty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.queue[self.front]

def solve():
    global N
    N, K = map(int, input().split())
    Queue = CircularQueue()
    res = []
    for i in range(1,N+1):
        Queue.enqueue(i)
    
    while True:
        i+=1
        if i%MAX_QSIZE == 3:
            res.append(Queue.dequeue)
            i=0
        else:
            temp = Queue.dequeue
            Queue.enqueue(temp)
        if Queue.isempty:
            break
    #




    return

if __name__ =="__main__":
    solve()