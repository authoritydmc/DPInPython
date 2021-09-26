# dict to store key-val
# Python program to implement fibbonaci number generator using DP
d={}
d[0]=1
d[1]=1

def fib(n):
    if d.get(n,-1)!=-1:
        return d[n]
    d[n]=fib(n-1)+fib(n-2)
    return d[n]


print(fib(30))

for k,v in d.items():
    print(k,v)

