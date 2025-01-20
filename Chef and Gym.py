- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CGYM
- Difficulty: 496

Code:
T=int(input())
for i in range(T):
    X,Y,Z=map(int,input().split())
    cost=X 
    training=Y  
    budget=Z  
    both=cost+training
    if(budget<cost):
        print(0)
    elif(budget<both):
        print(1)
    elif(budget==both):
        print(2)
    elif(budget>both):
        print(2)
