
a = input()
x = a.split()

sum = 0
size = 0

for i in x:
    sum += float(i)
    size += 1
    
ans = sum/size

if ans < 85:
    print("Dark Image")
elif 85<= ans and ans<= 170:
    print("Normal Image")
else:
    print("Bright Image")
