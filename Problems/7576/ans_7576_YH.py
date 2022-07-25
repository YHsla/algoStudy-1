#https://www.acmicpc.net/problem/7576
from collections import deque

def solve():
    M, N = map(int, input().split())
    graph = []
    visited = [[0]*M for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    queue = deque()
    cnt = 0
    for _ in range(N):
        graph.append(list(map(int, input().split(" "))))
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()   
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                graph[nx][ny] = 1
                queue.append((nx,ny))
        print(queue)
        if (x+y) != (nx+ny):
            cnt +=1

    return print(cnt)

  
if __name__ == "__main__":
    solve()