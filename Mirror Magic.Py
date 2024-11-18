m=int(input())
n=[]
for _ in range(m):
    p=list(map(int,input().split()))
    n.append(p)
q=[p[::-1]for p in n]
for p in q:
    print(" ".join(map(str,p)))
