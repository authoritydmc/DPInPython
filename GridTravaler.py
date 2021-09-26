# travel in m*n matrix only down or right allowed




def gridT(m,n,d={}):
    if d.get(f"{m},{n}",-1)!=-1:
        return d[f"{m},{n}"]
    if m==0 or n==0:
        return 0
    if m==1 and n==1:
        return 1
    


    d[f"{m},{n}"]=gridT(m-1,n,d)+gridT(m,n-1,d)
    return d[f"{m},{n}"]


    




print(gridT(20,20))