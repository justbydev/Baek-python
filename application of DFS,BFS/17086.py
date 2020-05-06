import sys
from collections import deque
dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, 1, 1, 1, 0, -1, -1, -1]
def bfs(N, M, shark, cal, stx, sty):
    visit=[[0]*M for _ in range(N)]
    queue=deque()
    queue.append([stx, sty, 0])
    visit[stx][sty]=1
    cal[stx][sty]=0
    while queue:
        nx, ny, cnt=queue.popleft()
        for i in range(8):
            nowx=nx+dx[i]
            nowy=ny+dy[i]
            if nowx<0 or nowx>=N or nowy<0 or nowy>=M or visit[nowx][nowy]==1 or cal[nowx][nowy]<=cnt+1:
                continue
            queue.append([nowx, nowy, cnt+1])
            visit[nowx][nowy]=1
            cal[nowx][nowy]=cnt+1
N,M=map(int, sys.stdin.readline().split())
shark=[]
for _ in range(N):
    shark.append(list(map(int, sys.stdin.readline().split())))
cal=[[101]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if shark[i][j]==1:
            bfs(N, M, shark, cal, i, j)
res=cal[0][0]
for i in range(N):
    for j in range(M):
        res=max(res, cal[i][j])
print(res)
