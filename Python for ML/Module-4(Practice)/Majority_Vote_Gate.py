n = int(input())

Y = 0; N = 0

for i in range(n):
    x = input()
    if x == "YES":
        Y += 1
    else:
        N += 1
        
if Y>=N:
    print("ACCEPT")
else:
    print("REJECT")