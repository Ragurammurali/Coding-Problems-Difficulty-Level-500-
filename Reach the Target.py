- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/REACHTARGET 
- Difficulty: 281 

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    win=X-Y
    print(win)
