# https://www.acmicpc.net/problem/2178

def solve():
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, list(input()))))

    print(graph)

    return

if __name__ == "__main__":
    solve()