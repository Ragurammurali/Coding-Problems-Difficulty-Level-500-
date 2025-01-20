- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CMASKS 
- Difficulty: 432

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    cost1=X*100
    cost2=Y*10
    if(cost1==cost2):
        print("Cloth")
    elif(cost1<cost2):
        print("Disposable")
    elif(cost2<cost1):
        print("Cloth")
    
