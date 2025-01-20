- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FBC
- Difficulty: 419

Code:
T=int(input())
for i in range(T):
    K,X=map(int,input().split())
    extra_water_that_can_be_filled=K-X
    print(extra_water_that_can_be_filled)
