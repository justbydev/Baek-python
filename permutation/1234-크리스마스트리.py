import sys
sys.setrecursionlimit(10**8)
fac=[0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
def recur_tree(N, R, G, B, level, res, now):
    if level>N:
        res[0]+=now
        return
    if level%2==1:
        if R>=level:
            recur_tree(N, R-level, G, B, level+1, res, now)
        if G>=level:
            recur_tree(N, R, G-level, B, level+1, res, now)
        if B>=level:
            recur_tree(N, R, G, B-level, level+1, res, now)
        if level%3==0:
            div=level//3
            if R>=div and G>=div and B>=div:
                recur_tree(N, R-div, G-div, B-div, level+1, res, now*(fac[level]//(fac[div]*fac[div]*fac[div])))
    elif level%2==0:
        if R>=level:
            recur_tree(N, R-level, G, B, level+1, res, now)
        if G>=level:
            recur_tree(N, R, G-level, B, level+1, res, now)
        if B>=level:
            recur_tree(N, R, G, B-level, level+1, res, now)
        div=level//2
        temp=fac[level]//(fac[div]*fac[div])
        if R>=div and G>=div:
            recur_tree(N, R-div, G-div, B, level+1, res, now*temp)
        if R>=div and B>=div:
            recur_tree(N, R-div, G, B-div, level+1, res, now*temp)
        if G>=div and B>=div:
            recur_tree(N, R, G-div, B-div, level+1, res, now*temp)
        if level%3==0:
            div=level//3
            if R>=div and G>=div and B>=div:
                recur_tree(N, R-div, G-div, B-div, level+1, res, now*(fac[level]//(fac[div]*fac[div]*fac[div])))
                
N,R,G,B=map(int, sys.stdin.readline().split())
res=[0]

if N==1:
    if R!=0:
        res[0]+=1
    if G!=0:
        res[0]+=1
    if B!=0:
        res[0]+=1
else:
    if R!=0:
        recur_tree(N, R-1, G, B, 2, res, 1)
    if G!=0:
        recur_tree(N, R, G-1, B, 2, res, 1)
    if B!=0:
        recur_tree(N, R, G, B-1, 2, res, 1)
print(res[0])
