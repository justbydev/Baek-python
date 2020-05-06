import sys
sys.setrecursionlimit(10**8)

N,M,C=map(int, sys.stdin.readline().split())
gamefind=dict()
visit=[[[[-1]*(C+1) for _ in range(C+1)] for _ in range(M)] for _ in range(N)]

def dfs(nowx, nowy, cnt, before):
    if nowx<0 or nowx>=N or nowy<0 or nowy>=M:
        return 0
    if nowx==N-1 and nowy==M-1:
        if gamefind.get((N-1, M-1)) and gamefind[(N-1, M-1)]>before and cnt==1:
            return 1
        if cnt==0 and not gamefind.get((N-1, M-1)):
            return 1
        return 0
    if visit[nowx][nowy][cnt][before]!=-1:
        return visit[nowx][nowy][cnt][before]
    visit[nowx][nowy][cnt][before]=0
    if gamefind.get((nowx, nowy)) and gamefind[(nowx, nowy)]>before:
        visit[nowx][nowy][cnt][before]+=(dfs(nowx, nowy+1, cnt-1, gamefind[(nowx, nowy)])+dfs(nowx+1, nowy, cnt-1, gamefind[(nowx, nowy)]))%1000007
    elif not gamefind.get((nowx, nowy)):
        visit[nowx][nowy][cnt][before]+=(dfs(nowx, nowy+1, cnt, before)+dfs(nowx+1, nowy, cnt, before))%1000007
    return visit[nowx][nowy][cnt][before]

for i in range(C):
    x,y=map(int, sys.stdin.readline().split())
    x-=1
    y-=1
    gamefind[(x,y)]=i+1

for i in range(C+1):
    print(dfs(0, 0, i, 0), end=' ')
print()

