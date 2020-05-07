import sys

N,K=map(int, sys.stdin.readline().split())
dp=[[[[0]*(N+1) for _ in range(N+1)] for _ in range(3)] for _ in range(N)]

dp[0][0][1][0]=dp[0][1][0][1]=dp[0][2][0][0]=1
for i in range(1, N):
    for j in range(3):
        if j==1:
            for k in range(i+2):
                for l in range(i+2-k):
                    dp[i][j][k][l]=(dp[i-1][0][k][l-1]+dp[i-1][2][k][l-1])%1000000007
        elif j==0:
            for k in range(i+2):
                for l in range(i+2-k):
                    dp[i][j][k][l]=(dp[i-1][0][k-1][l]+dp[i-1][1][k-1][l]+dp[i-1][2][k-1][l])%1000000007
        elif j==2:
            for k in range(i+2):
                for l in range(i+2-k):
                    dp[i][j][k][l]=(dp[i-1][0][k][l]+dp[i-1][1][k][l]+dp[i-1][2][k][l])%1000000007

res=0
for j in range(3):
    for k in range(N+1):
        for l in range(N+1):
            if k+l<N:
                if K==0:
                    if k==0:
                        res+=dp[N-1][j][k][l]
                elif k%K==0:
                    res+=dp[N-1][j][k][l]
print(res%1000000007)
