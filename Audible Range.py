- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/AUDIBLE 
- Difficulty: 279 

Code:
T=int(input())
for i in range(T):
    X=int(input())
    if(X>=67 and X<=45000):
        print("YES")
    else:
        print("NO")
