- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PARTY2 
- Difficulty: 363

Code:
T=int(input())
for i in range(T):
    N,X,K=map(int,input().split())
    A=N*X 
    if(A<K):
        print("YES")
    elif(A>K):
        print("NO")
    elif(A==K):
        print("YES")
