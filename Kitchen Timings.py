- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/KITCHENTIME
- Difficulty: 273

Code:
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    hours_chef_works=Y-X
    print(hours_chef_works)
