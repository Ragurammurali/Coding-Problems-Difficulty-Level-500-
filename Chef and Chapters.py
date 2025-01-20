- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SEMCOURSES
- Difficulty: 350

Code:
T=int(input())
for i in range(T):
    X,Y,Z=map(int,input().split())
    total_chapters=X*Y*Z 
    print(total_chapters)
