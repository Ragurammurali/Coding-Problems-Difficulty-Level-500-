- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/COUGAME 
- Difficulty: 347

Code:
T=int(input())
for i in range(T):
    G,B=map(int,input().split())
    if(B>G):
        print(B-G)
