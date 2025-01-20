- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DETSCORE
- Difficulty: 267 

Code:
T=int(input())
for i in range(T):
    X,N=map(int,input().split())
    total_test_cases=10
    point_per_test_case=X/total_test_cases 
    points_scored_by_chef=point_per_test_case*N 
    print(int(points_scored_by_chef))
