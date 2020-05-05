import sys
sys.setrecursionlimit(10**8)

def dfs(N, oneway, visit, visitstack, now):
    visit[now]=1
    visitstack[now]=1
    cycle=0
    for nx in oneway[now]:
        if visit[nx]==0:
            if dfs(N, oneway, visit, visitstack, nx):
                return 1
        elif visit[nx]==1 and visitstack[nx]==1:
            cycle=1
            break
    visitstack[now]=0
    return cycle
N=int(sys.stdin.readline())
graph=[]
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))
oneway=[[] for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        if i!=j and graph[i][j]!=graph[j][i]:
            if graph[i][j]=='Y':
                oneway[i].append(j)
            elif graph[j][i]=='Y':
                oneway[j].append(i)
visit=[0]*N
cycle=0
for i in range(N):
    if visit[i]==1:
        continue
    visitstack=[0]*N
    cycle=dfs(N, oneway, visit, visitstack, i)
    if cycle==1:
        break
if cycle==1:
    print("NO")
else:
    flag=0
    for i in range(N):
        if graph[i][i]=='Y':
            print("NO")
            flag=1
    if flag==0:
        print("YES")
