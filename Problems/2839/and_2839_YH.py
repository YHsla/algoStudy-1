#https://www.acmicpc.net/problem/2839

#Bottom-Up 방식
def solve1():
    N = int(input())
    dp = [-1]*5001 
    # 초기값 설정으로 입력값이 최대 5000 Kg이기 때문에 dp의 크기가 5000이하인 경우, Index error가 발생
    dp[3], dp[5] = 1, 1
    for i in range(6,N+1):
        if dp[i-5] == -1 and dp[i-3] == -1 : # 5kg, 3kg로 정확하게 만들 수 없는 경우
            dp[i] = -1
        elif dp[i-5] == -1:
            dp[i] = dp[i-3]+1
        elif dp[i-3] == -1:
            dp[i] = dp[i-5]+1
        else:
            dp[i] = min(dp[i-3], dp[i-5])+1
    print(dp[N])

#Top-Down 방식 - 어렵군...
# def solve2():
#     N = int(input())
#     global memo
#     memo ={}

# def dp(n):
#     if n not in memo:
#         result = min(dp(n-3), dp(n-5))+1
#         memo[n] = result
#     return memo[n]


if __name__ == "__main__":
    solve()