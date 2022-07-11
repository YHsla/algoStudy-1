#https://www.acmicpc.net/problem/1012
from collections import deque

def bfs(x,y,visited,graph, cnt):
    queue = deque()
    if graph[x][y] == 1:
        queue.append((x,y))
        visited[x][y] = 1
        graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < M and 0<= ny < N:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    graph[nx][ny] = 0
    cnt+=1     
    return cnt

def solve():
    global dx, dy, M, N
    TC = int(input())
    M, N, K = map(int, input().split())
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    visited = [[0]*M in range(N)]

    for _ in range(TC):
        graph = [[0]*M in range(N)]
        cnt = 0

        for _ in range(K):    
            a, b = map(int, input().split())
            graph[a][b] = 1        
        
        for i in range(M):
            for j in range(N):
                if graph[i][j] == 1:
                    bfs(i, j, visited, graph, cnt)
        
        print(cnt)

    return


if __name__ == "__main__":
    solve()