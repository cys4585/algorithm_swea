# 숨바꼭질

# 수빈 : N / 동생 : K (0<=N, K <= 500,000)
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간 구하기
# 수빈이의 가능한 이동 : 1초 후 (X -> 2X, X+1, X-1) 중 하나
# 동생의 이동 K -> K+1 -> K+1+2 -> K+1+2+3 -> ...
# 0보다 작은 좌표, 50보다 큰 좌표로 이동 불가능, 정수 좌표에서만 찾을 수 있음
# N=5, K=17 => 2초
# N=17, K=5 => 4초
# N=1, K=10 => 6초

n, k = input().split()

result = 0
if n == k:
    pass
else:
    queue = list()
# 홀수초, 짝수초일때로 나눠서 각각 가장 빠른 시간 계산...?
#

print(result)