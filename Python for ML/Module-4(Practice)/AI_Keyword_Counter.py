s = input()

a = s.split()
cnt = 0

for x in a:
    if "ai" == x:
        cnt += 1
    if "data" == x:
        cnt += 1
    if "model"== x:
        cnt += 1
    if "learn" == x:
        cnt += 1
    if "train" == x:
        cnt += 1
    if "neural" == x:
        cnt += 1

if cnt>=2:
    print("AI Detected")
else:
    print("Not AI Related")