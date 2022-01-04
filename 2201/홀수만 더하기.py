# 10개 수를 받아 홀수만 더한 값 출력
t = int(input())   # 테스트 케이스 개수 
 
for test_case in range(1,t+1):
    li = map(int, input().split())
    answer = 0
    for i in li:
        if i%2!=0:     # 2로 나누었을 떄 나머지가 0이 아니면 홀수 
            answer += i
    print("#"+str(test_case),str(answer))