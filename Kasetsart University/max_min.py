i   = 0
MIN = 0
MAX = 0
total = 0
result = 0
while True:
    a = str(input())
    if(a==''): break
    a = float(a)
    if i == 0: MIN= a
    if a < MIN:
        MIN = a
    if a > MAX:
        MAX = a
    total = total + a
    result+=1
    i+=1
print(f"{MAX:.2f} {MIN:.2f}")
print(f"{total:.2f} {total/result:.2f}")