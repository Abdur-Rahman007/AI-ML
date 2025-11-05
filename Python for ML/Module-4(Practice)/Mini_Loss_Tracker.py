n = int(input())

target = float(input())

loss = 0

for i in range(n):
    x = float(input())
    loss += x
    
loss = loss/n

if loss <= target:
    print("PASS")
else:
    print("RETRY")