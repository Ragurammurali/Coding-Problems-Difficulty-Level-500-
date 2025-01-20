- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SUMM 
- Difficulty: 308 

Code:
T=int(input())
for i in range(T):
    A,B,C=map(int,input().split())
    if(C==A+B):
        print("YES")
    elif(C!=A+B):
        print("NO")
