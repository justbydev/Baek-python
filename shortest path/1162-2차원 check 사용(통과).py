import sys
import heapq

def dijkstra_dp(N, M, K, graph, dp):
    heap=[]
    heapq.heappush(heap, [0, 0, 0])
    check=[[0]*(K+1) for _ in range(N)]
    check[0][0]=1
    while heap:
        weight, now, cnt=heapq.heappop(heap)
        check[now][cnt]=1
        for nx, nxw in graph[now]:
            if check[nx][cnt]==0 and dp[nx][cnt]>weight+nxw:
                dp[nx][cnt]=weight+nxw
                heapq.heappush(heap, [weight+nxw, nx, cnt])
            if cnt+1<=K and dp[nx][cnt+1]>weight and check[nx][cnt+1]==0:
                dp[nx][cnt+1]=weight
                heapq.heappush(heap, [weight, nx, cnt+1])
            
N,M,K=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(N)]
for i in range(M):
    st,ed,w=map(int, sys.stdin.readline().split())
    graph[st-1].append([ed-1, w])
    graph[ed-1].append([st-1, w])
dp=[[float('inf')]*(K+1) for _ in range(N)]
dp[0][0]=0
dijkstra_dp(N, M, K, graph, dp)
print(min(dp[N-1]))


                  
