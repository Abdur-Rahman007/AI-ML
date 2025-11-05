s = input()

a = s.count('A')
b = s.count('B')

n = a + b

x = a/n
y = b/n

if x>0.7 or y>0.7:
    print("Biased Model")
else:
    print("Fair Model")