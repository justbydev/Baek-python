import sys
import heapq

def dijkstra(N, M, st, ed, dist, graph):
    check=[0]*N
    check[st]=1
    heap=[]
    heapq.heappush(heap, [0, st])
    while heap:
        weight, now=heapq.heappop(heap)
        check[now]=1
        for nx, nw in graph[now]:
            if check[nx]==0:
                if dist[nx]>weight+nw:
                    dist[nx]=weight+nw
                    heapq.heappush(heap, [weight+nw, nx])
N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
graph=[[] for _ in range(N)]
for _ in range(M):
    st,ed,w=map(int, sys.stdin.readline().split())
    graph[st-1].append([ed-1, w])
st,ed=map(int, sys.stdin.readline().split())
dist=[float('inf')]*N
dist[st-1]=0
dijkstra(N, M, st-1, ed-1, dist, graph)
print(dist[ed-1])


                  
