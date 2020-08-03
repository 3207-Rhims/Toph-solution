n = input()
n=int(n)
p1=n%1000
q=int(n/1000)
l=q%1000
m=int(q/1000)
p=m%1000
if p>0 :
    r=p  
if p1>0:
    t=p1
else:
    print("000")   
    
if l>0:
    k=l 
else:
    print("000")            
print(r, k, t, sep=",")   
        