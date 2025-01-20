- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MAXIMUMSUBS
- Difficulty: 435

Code:
T=int(input())
for i in range(T):
    X=int(input())
    Time=X*60
    submissions=Time/30
    print(int(submissions))
