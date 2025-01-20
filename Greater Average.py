- Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/AVGPROBLEM
- Difficulty: 500

Code:
T=int(input())
for i in range(T):
    A,B,C=map(int,input().split())
    D=(A+B)/2
    if(D>C):
        print("YES")
    else:
        print("NO")
