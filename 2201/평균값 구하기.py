# 10개 수 평균값 출력

t = int(input())
for i in range(t) :
    nums = map(int,input().split())
    res = sum(n for n in nums)
    print( f"#{i+1} {round(res/10)}" )