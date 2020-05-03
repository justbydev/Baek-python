import sys

N,L,R=map(int, sys.stdin.readline().split())
dp=[[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[1][1][1]=1
if N==1:
    if L==1 and R==1:
        print(1)
    else:
        print(0)
elif N==2:
    if (L==1 and R==2) or (L==2 and R==1):
        print(1)
    else:
        print(0)
else:
    dp[2][1][2]=dp[2][2][1]=1
    for i in range(3, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                dp[i][j][k]=dp[i-1][j-1][k]+dp[i-1][j][k-1]+dp[i-1][j][k]*(i-2)
    print(dp[N][L][R]%1000000007)
