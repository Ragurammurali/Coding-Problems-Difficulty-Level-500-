- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CS2023_GIFT
- Difficulty: 390

Code:
X,N,M=map(int,input().split())
total_funds_om_has=X+M
if(total_funds_om_has>=N):
    print("YES")
elif(total_funds_om_has<N):
    print("NO")
