n=[]
l=int(input())
n = list(map(int,input().strip().split()))[:l]
if 1<=l<=100:
    k=0
    for i in range(0,l):
        k=int(k+i)
        if n[0]==0 and n[k]==1:
            print("Change needed")
        else:
            print("No change needed")  
    
