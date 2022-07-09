#https://www.acmicpc.net/problem/2667
from collections import deque

def bfs(x,y, graph, visited):
    queue = deque()
    queue.append((x,y))
    complex = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0 <= nx < n and 0 <= ny < n):
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    complex+=1
                    visited[nx][ny]=1
                    queue.append((nx,ny))
        # if nx == n-1 and ny == n-1 :
    return (complex,x,y)

def solve():
    global dx, dy, n
    n = int(input())
    graph =[]
    visited=[[0]*n for _ in range(n)]
    dx = [-1,1,0,0] #좌,우,상,하
    dy = [0,0,1,-1]
    res = []
    for _ in range(n):
        graph.append(list(map(int,list(input()))))
    print(graph)
    x, y = 0, 0
    while x != n-1 and y != n-1:
        num, nx, ny = bfs(x,y,graph,visited)
        if graph[nx+1][ny] == 1:
            x,y = nx+1, ny
        elif graph[nx][ny+1] == 1:
            x,y = nx, ny+1
        else:
            x,y = nx+1, ny+1
        print(x,y)
        res.append(num)
    return print(res)

if __name__ == "__main__":
    solve()