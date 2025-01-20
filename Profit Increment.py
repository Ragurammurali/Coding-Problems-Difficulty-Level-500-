- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PROINC 
- Difficulty: 414

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    discount=(10/100)*X
    total_profit_made=discount+Y  
    print(int(total_profit_made))
