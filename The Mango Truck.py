- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MANGOES
- Difficulty: 482

Code:
T=int(input())
for i in range(T):
    X,Y,Z=map(int,input().split())
    unutilised_weight=Z-Y 
    maximum_mangoes=(Z-Y)/X  
    print(int(maximum_mangoes))
