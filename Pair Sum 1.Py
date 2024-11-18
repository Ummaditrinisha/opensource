def find_pair_with_sum():
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    complements=set()
    for num in arr:
        if k-num in complements:
            print("true")
            return 
        complements.add(num)
    print("false")
find_pair_with_sum()
