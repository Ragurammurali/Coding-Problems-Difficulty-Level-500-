- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PRACTICEPERF 
- Difficulty: 467

Code:
P1,P2,P3,P4=map(int,input().split())
count=0
if(P1>=10):
    count+=1
if(P2>=10):
    count+=1
if(P3>=10):
    count+=1
if(P4>=10):
    count+=1
print(count)
