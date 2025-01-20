- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FLOW002 
- Difficulty: 421

Code:
T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    remainder=A%B
    print(remainder)
