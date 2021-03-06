# 연산자 끼워넣기

# N개의 수로 이루어진 수열 A1, A2, ..., An이 주어진다.
# 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다.
# 연산자는 덧셈, 뺄셈, 곱셈, 나눗셈으로만 이루어져 있다.

# 우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다.
# 이 때, 주어진 수의 순서를 바꾸면 안된다.

# 예를 들어, 6개의 수로 이루어진 수열이 1,2,3,4,5,6 이고,
# 주어진 연산자가 덧셈 2개, 뺄셈 1개, 곱셈 1개, 나눗셈 1개인 경우에는
# 총 60가지의 식을 만들 수 있다.
# 1+2+3-4*5/6
# 1/2+3+4-5*6
# 1+2/3*4-5+6
# 1/2*3-4+5+6
# ...

# 식의 계산은 연산자 우선순위를 무시하고 앞에서부터 진행해야 한다.
# 또, 나눗셈은 정수 나눗셈으로 몫만 취한다.

# 음수를 양수로 나눌 때는 C++14의 기준을 따른다.
# 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
# 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.
# 1+2+3-4*5/6 = 1
# 1/2+3+4-5*6 = 12
# 1+2/3*4-5+6 = 5
# 1/2*3-4+5+6 = 7

# N개의 수와 N-1개의 연산자가 주어졌을 때,
# 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

# cal_v : 계산된 값
# idx : 수열의 인덱스 (cal_v에 계산할 값을 구할 인덱스)
# p : 남은 + 연산자의 개수
# s : 남은 - 연산자의 개수
# m : 남은 * 연산자의 개수
# d : 남은 / 연산자의 개수
def dfs(cal_v, idx, p, s, m, d):
    global max_v
    global min_v
    if idx == N:
        if max_v is None or max_v < cal_v:
            max_v = cal_v
        if min_v is None or min_v > cal_v:
            min_v = cal_v
        return
    n = A[idx]
    if p:
        dfs(cal_v + n, idx + 1, p - 1, s, m, d)
    if s:
        dfs(cal_v - n, idx + 1, p, s - 1, m, d)
    if m:
        dfs(cal_v * n, idx + 1, p, s, m - 1, d)
    if d:
        dfs(-(-cal_v // n) if cal_v < 0 else cal_v // n, idx + 1, p, s, m, d - 1)


N = int(input())    # 2 <= N <= 11
A = list(map(int, input().split()))     # 1 <= A[i] <= 100
op = list(map(int, input().split()))  # (+, -, *, /)의 갯수 (sum(in_arr) == N-1)

max_v = min_v = None
dfs(A[0], 1, op[0], op[1], op[2], op[3])
print(max_v)
print(min_v)