import sys

T,W=map(int, sys.stdin.readline().split())
dp=[[[0]*2 for _ in range(W+1)] for _ in range(T)]
time=[0]*T
for i in range(T):
    tree=int(sys.stdin.readline())
    time[i]=tree
if time[0]==1:
    dp[0][0][0]=1
elif time[0]==2:
    dp[0][1][1]=1
for i in range(1, T):
    for j in range(0, W+1):
        for k in range(2):
            if j==0:
                if k==0:
                    if time[i]==1:
                        dp[i][j][k]=dp[i-1][j][0]+1
                    elif time[i]==2:
                        dp[i][j][k]=dp[i-1][j][0]
                elif k==1:
                    if time[i]==1:
                        dp[i][j][k]=dp[i-1][j][1]
                    elif time[i]==2:
                        dp[i][j][k]=dp[i-1][j][1]+1
            else:
                if k==0:
                    if time[i]==1:
                        dp[i][j][k]=max(dp[i-1][j][0]+1, dp[i-1][j-1][1]+1)
                    elif time[i]==2:
                        dp[i][j][k]=max(dp[i-1][j][0], dp[i-1][j-1][1])
                elif k==1:
                    if time[i]==1:
                        dp[i][j][k]=max(dp[i-1][j][1], dp[i-1][j-1][0])
                    elif time[i]==2:
                        dp[i][j][k]=max(dp[i-1][j][1]+1, dp[i-1][j-1][0]+1)

print(max(max(*dp[T-1])))       
