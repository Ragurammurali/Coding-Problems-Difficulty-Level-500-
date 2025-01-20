- Link: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BOBBANK 
- Difficulty:481

Code:
T=int(input())
for i in range(T):
    W,X,Y,Z=map(int,input().split())
    total_amount_deposited=(X*Z)+W
    total_bank_charges=Y*Z 
    final_balance=total_amount_deposited-total_bank_charges
    print(final_balance)
