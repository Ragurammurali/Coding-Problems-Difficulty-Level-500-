- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CHEFCHOCO
- Difficulty: 492

Code:
T=int(input())
for i in range(T):
    C,X,Y=map(int,input().split())
    remaining_chocolates=C-X 
    total_cost=remaining_chocolates*Y  
    print(total_cost)
