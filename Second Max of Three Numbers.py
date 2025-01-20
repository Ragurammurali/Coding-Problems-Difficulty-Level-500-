- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SNDMAX 
- Difficulty: 300 

Code:
T=int(input())
for i in range(T):
    A=list(map(int,input().split()))
    A.remove(max(A))
    print(max(A))
