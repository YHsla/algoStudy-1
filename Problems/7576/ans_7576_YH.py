#https://www.acmicpc.net/problem/7576
from collections import deque

def solve():
    M, N = map(int, input().split())
    graph = []
    visited = [[0]*M for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    queue = deque()
    for _ in range(N):
        graph.append(list(map(int, input().split(" "))))
    
    isfull = True
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i,j,0))
                visited[i][j] = 1
            elif graph[i][j] == -1:
                visited[i][j] = 1
            else:
                isfull = False
    # print(queue)

    while queue:
        temp = len(queue)
        x, y, cnt = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    graph[nx][ny] = 1
                    queue.append((nx,ny,cnt+1))
    
    if isfull == True:
        print(0)
    elif visited != [[1]*M for _ in range(N)]:
        print(-1)
    else:
        print(cnt)
  
if __name__ == "__main__":
    solve()