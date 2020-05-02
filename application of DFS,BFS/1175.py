import sys
from collections import deque

def bfs(N, M, mp, stx, sty, ex, ey, visit, dx, dy, beforedr):
    queue=deque()
    for i in range(4):
        nowx=stx+dx[i]
        nowy=sty+dy[i]
        if nowx<0 or nowx>=N or nowy<0 or nowy>=M or beforedr[0]==i or mp[nowx][nowy]=='#':
            continue
        if nowx==ex and nowy==ey:
            beforedr[0]=i
            return 1
        queue.append([nowx, nowy, i, 1])
        visit[i][nowx][nowy]=1
    while queue:
        nowx, nowy, dr, cnt=queue.popleft()
        for i in range(4):
            nx=nowx+dx[i]
            ny=nowy+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M or i==dr or mp[nowx][nowy]=='#':
                continue
            if visit[i][nx][ny]==1:
                continue
            if nx==ex and ny==ey:
                beforedr[0]=i
                return cnt+1
            queue.append([nx, ny, i, cnt+1])
            visit[i][nx][ny]=1
    return -1
N,M=map(int, sys.stdin.readline().split())
mp=[]
for i in range(N):
    mp.append(list(sys.stdin.readline().rstrip()))
stx=sty=cx1=cy1=cx2=cy2=-1
for i in range(N):
    for j in range(M):
        if mp[i][j]=='S':
            mp[i][j]='.'
            stx=i
            sty=j
        elif mp[i][j]=='C':
            mp[i][j]='.'
            if cx1==-1:
                cx1=i
                cy1=j
            else:
                cx2=i
                cy2=j
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
res1=res2=-1
beforedr=[-1]
visit=[[[0]*M for _ in range(N)] for _ in range(4)]
r=bfs(N, M, mp, stx, sty, cx1, cy1, visit, dx, dy, beforedr)
visit=[[[0]*M for _ in range(N)] for _ in range(4)]
r2=bfs(N, M, mp, cx1, cy1, cx2, cy2, visit, dx, dy, beforedr)
visit=[[[0]*M for _ in range(N)] for _ in range(4)]
beforedr=[-1]
r3=bfs(N, M, mp, stx, sty, cx2, cy2, visit, dx, dy, beforedr)
visit=[[[0]*M for _ in range(N)] for _ in range(4)]
r4=bfs(N, M, mp, cx2, cy2, cx1, cy1, visit, dx, dy, beforedr)
if r!=-1 and r2!=-1:
    res1=r+r2
if r3!=-1 and r4!=-1:
    res2=r3+r4
if res1==-1 and res2==-1:
    print(-1)
elif res1!=-1 and res2==-1:
    print(res1)
elif res1==-1 and res2!=-1:
    print(res2)
else:
    print(min(res1, res2))


                  
