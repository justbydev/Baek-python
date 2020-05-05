import sys
sys.setrecursionlimit(10**8)
def dfs(N, num, visit, check, T, res, nw):
    nx=num[nw]
    check[nw]=1
    visit[nw]=1
    if visit[nx]==0:
        dfs(N, num, visit, check, T, res, nx)
    elif visit[nx]==1:
        if check[nx]==1:
            res[T]+=1
            check[nw]=0
        else:
            return
T=int(sys.stdin.readline())
res=[0]*T
for t in range(T):
    N=int(sys.stdin.readline())
    num=list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        num[i]-=1
    visit=[0]*N
    check=[0]*N
    for i in range(N):
        if visit[i]==0:
            dfs(N, num, visit, check, t, res, i)
for i in range(T):
    print(res[i])
