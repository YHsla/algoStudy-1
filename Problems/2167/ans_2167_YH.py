#https://www.acmicpc.net/problem/2167

def solve():
    N, M = map(int, input().split())
    arry = []
    for _ in range(N):
        arry+=list(map(int,input().split()))
    K = int(input())
    for _ in range(K):
        i,j,x,y = map(int, input().split())
        res = sum(arry[((i-1)*(N)+(j-1)):((x-1)*(N)+(y+1))])
        print(res)
    return

if __name__ =="__main__":
    solve()