n = 1
i = 1
count = int(input())
while i<=count:
    j = 1
    while j<=i:
        print(chr(ord('A')+n-1),end='')
        n = n + 1
        j+=1
    n = 1
    print("\n",end='')
    i += 1