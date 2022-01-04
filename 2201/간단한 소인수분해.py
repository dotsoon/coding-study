# 숫자 N이 주어질 때 a,b,c,d,e 출력
# N=2a x 3b x 5c x 7d x 11e

num = int(input())

for i in range(1,num+1):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    
    n = int(input())
    
    while n!=1:
        if n%11 == 0:
            e += 1
            n = n//11
        elif n%7 == 0:
            d += 1
            n = n//7
        elif n%5 == 0:
            c += 1
            n = n//5
        elif n%3 == 0:
            b += 1
            n = n//3
        elif n%2 == 0:
            a += 1
            n = n//2

    print('#%d' %i,a,b,c,d,e)