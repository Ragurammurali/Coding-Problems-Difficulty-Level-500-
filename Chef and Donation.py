- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DNATION 
- Difficulty: 305

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if(Y>X):
        difference=Y-X
        print(difference)

