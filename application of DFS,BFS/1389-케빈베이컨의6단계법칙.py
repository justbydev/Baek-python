import sys
from collections import deque

def bfs(visit, nw, graph, num):
    queue=deque()
    queue.append([nw, 0])
    while queue:
        now, cnt=queue.popleft()
        for key in graph[now].keys():
            if visit[key]==1:
                continue
            queue.append([key, cnt+1])
            visit[key]=1
            num[nw][key]=cnt+1
N,M=map(int, sys.stdin.readline().split())
graph=[dict() for _ in range(N+1)]
for _ in range(M):
    a,b=map(int, sys.stdin.readline().split())
    if not graph[a].get(b):
        graph[a][b]=1
        graph[b][a]=1
num=[[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    visit=[0]*(N+1)
    visit[i]=1
    bfs(visit, i, graph, num)

res=1
sm=sum(num[1])

for i in range(2, N+1):
    if sum(num[i])<sm:
        res=i
        sm=sum(num[i])
print(res)
    
