- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FAIRPASS 
- Difficulty: 342 

Code:
T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    if(K>N):
        print("YES")
    elif(K<N):
        print("NO")
    elif(K==N):
        print("NO")
