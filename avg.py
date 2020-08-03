l=int(input())
n = list(map(int,input().strip().split()))[:l]
sum=n[0]
print(sum)
for i in range(0,len(n)-1):
    sum=sum+n[i+1]
    avg=sum/(i+2)
    print(avg)


