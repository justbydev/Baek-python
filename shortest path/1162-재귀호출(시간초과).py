import sys
sys.setrecursionlimit(10**8)
def dfs(N, M, K, graph, res, nw, weight, visit):
    if nw==N-1:
        weight.sort(reverse=True)
        sm=index=0
        while index<len(weight):
            if index==K:
                break
            sm+=weight[index]
            index+=1
        if res[0]==-1:
            res[0]=sum(weight)-sm
        else:
            res[0]=min(res[0], sum(weight)-sm)
    else:
        for i in range(len(graph[nw])):
            if visit[graph[nw][i][0]]==0:
                visit[graph[nw][i][0]]=1
                weight.append(graph[nw][i][1])
                dfs(N, M, K, graph, res, graph[nw][i][0], weight, visit)
                weight.pop()
                visit[graph[nw][i][0]]=0
            
N,M,K=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(N)]
for i in range(M):
    st,ed,w=map(int, sys.stdin.readline().split())
    graph[st-1].append([ed-1, w])
    graph[ed-1].append([st-1, w])
res=[-1]
weight=[]
visit=[0]*N
visit[0]=1
dfs(N, M, K, graph, res, 0, weight, visit)
print(res[0])

                  
