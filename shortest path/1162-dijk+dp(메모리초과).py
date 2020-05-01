import sys
import heapq

def dijkstra_dp(N, M, K, graph, dp):
    heap=[]
    heapq.heappush(heap, [0, 0, 0])
    check=[0]*N
    check[0]=1
    while heap:
        now=heapq.heappop(heap)
        check[now[1]]=1
        cnt=now[2]
        for i in range(len(graph[now[1]])):
            if check[graph[now[1]][i][0]]==0:
                dp[graph[now[1]][i][0]][cnt]=min(dp[graph[now[1]][i][0]][cnt], graph[now[1]][i][1]+dp[now[1]][cnt])
                heapq.heappush(heap, [dp[graph[now[1]][i][0]][cnt], graph[now[1]][i][0], cnt])
                if cnt+1<=K:
                    dp[graph[now[1]][i][0]][cnt+1]=min(dp[graph[now[1]][i][0]][cnt+1], dp[now[1]][cnt])
                    heapq.heappush(heap, [dp[graph[now[1]][i][0]][cnt+1], graph[now[1]][i][0], cnt+1])
N,M,K=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(N)]
for i in range(M):
    st,ed,w=map(int, sys.stdin.readline().split())
    graph[st-1].append([ed-1, w])
    graph[ed-1].append([st-1, w])
dp=[[float('inf')]*(K+1) for _ in range(N)]
dp[0][0]=0
dijkstra_dp(N, M, K, graph, dp)
print(min(*dp[N-1]))


                  
