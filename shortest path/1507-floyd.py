import sys

N=int(sys.stdin.readline())
graph=[]

real=[[1]*N for _ in range(N)]
def floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i==j or i==k or k==j:
                    continue
                if (graph[i][k]+graph[k][j])==graph[i][j] and real[i][j]==1 and real[i][k]==1 and real[k][j]==1:
                    real[i][j]=0
                    graph[i][j]=float('inf')
                    real[j][i]=0
                    graph[j][i]=float('inf')
                elif graph[i][k]+graph[k][j]<graph[i][j] and real[i][j]==1 and real[i][k]==1 and real[k][j]==1:
                    return -1
    return 1
                    
for _ in range(N):
    tmp=list(map(int, sys.stdin.readline().split()))
    graph.append(tmp)
    
r=floyd()
if r==-1:
    print(-1)
else:
    sm=0
    for i in range(N-1):
        for j in range(i+1, N):
            if graph[i][j]==float('inf'):
                continue
            sm+=graph[i][j]
    print(sm)


