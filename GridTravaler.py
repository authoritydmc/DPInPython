# travel in m*n matrix only down or right allowed

# find the number of ways one can reach start to end for example
# [S x x]
# [x x x]
# [x x E]
# has 3 unique ways to reach start to end 

"""
To Solve these Kind of Problem ,try to divide problem in subproblem so suppose what if there is only 1,1 grid present ,you can reach start to end in 1 unit of time,
similary what if one of m or n is 0 , obviously grid cant exist hence no ways is 0 ..these two forms your base cases.

Now as said you can only travel right or down,so suppose if you go down then total no of rows size decrease by 1 i.e m-1 .
similary what if you go right then total no of coloumn decreases by 1 i.e n-1 so you can see that your problem is sum of sub problem and
i.e grid(m,n)=grid(m-1,n)+grid(m,n-1)
"""


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