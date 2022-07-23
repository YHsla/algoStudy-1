#https://www.acmicpc.net/problem/7576
from collections import deque

def solve():
    global M, N, dx, dy, cnt
    M, N = map(int, input().split())
    graph = []
    visited = [[0]*M for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    queue = deque()
    cnt = 0
    for _ in range(N):
        graph.append(list(map(int, input().split(" "))))
    
    for i in range(M):
        for j in range(N):
            if graph[j][i] == 1:
                queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        if graph[y][x] == 1:    
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    graph[ny][nx] = 1
                    queue.append((nx,ny))
        cnt +=1

    return

  
if __name__ == "__main__":
    solve()