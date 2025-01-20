- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/ASSIGNMNT
- Difficulty: 468

Code:
T=int(input())
for i in range(T):
    X,Y,Z=map(int,input().split())
    totaltimetakentocompleteassignments=X*Y  
    totaltime=Z*24*60
    if(totaltimetakentocompleteassignments<totaltime):
        print("YES")
    elif(totaltimetakentocompleteassignments>totaltime):
        print("NO")
    elif(totaltimetakentocompleteassignments==totaltime):
        print("YES")
