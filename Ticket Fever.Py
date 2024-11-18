a=int(input())
for _ in range(a):
    b,c=map(int,input().split())
    if b>c:
        print(b-c)
    else:
        print(0)
