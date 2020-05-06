import sys
sys.setrecursionlimit(10**8)

N,M,C=map(int, sys.stdin.readline().split())
game=dict()
visit=[[[[-1]*(C+1) for _ in range(C+1)] for _ in range(M)] for _ in range(N)]
dx=[0, 1]
dy=[1, 0]

def dfs(nowx, nowy, cnt, before):
    if cnt<0:
        return 0
    if nowx==N-1 and nowy==M-1:
        if cnt==1 and game.get((nowx, nowy)) and game[(nowx, nowy)]>before:
            return 1
        if cnt==0 and not game.get((nowx, nowy)):
            return 1
        return 0
    if visit[nowx][nowy][cnt][before]!=-1:
        return visit[nowx][nowy][cnt][before]
    visit[nowx][nowy][cnt][before]=0
    for i in range(2):
        nx=nowx+dx[i]
        ny=nowy+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if cnt>0 and game.get((nowx, nowy)) and game[(nowx, nowy)]>before:
            visit[nowx][nowy][cnt][before]+=dfs(nx, ny, cnt-1, game[(nowx, nowy)])
        elif not game.get((nowx, nowy)):
            visit[nowx][nowy][cnt][before]+=dfs(nx, ny, cnt, before)
    return visit[nowx][nowy][cnt][before]
for i in range(C):
    x,y=map(int, sys.stdin.readline().split())
    x-=1
    y-=1
    game[(x,y)]=i+1

for i in range(C+1):
    print(dfs(0, 0, i, 0)%1000007, end=' ')
print()
