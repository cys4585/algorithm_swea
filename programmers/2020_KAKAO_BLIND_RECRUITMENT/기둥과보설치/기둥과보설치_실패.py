# 기둥과 보 설치

# 빙하가 깨지면서 스노우타운에 떠내려 온 죠르디는 인생 2막을 위해 주택 건축사업에 뛰어들기로 결심했다.
# 죠르디는 기둥과 보를 이용하여 벽면 구조물을 자동으로 세우는 로봇을 개발할 계획인데,
# 그에 앞서 로봇의 동작을 시뮬레이션 할 수 있는 프로그램을 만들고 있다.

# 프로그램은 2차원 가상 벽면에 기둥과 보를 이용한 구조물을 설치할 수 있는데,
# 기둥과 보는 길이가 1인 선분으로 표현되며 다음과 같은 규칙을 가지고 있다.
#   - 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 한다.
#   - 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 한다.
# 단, 바닥은 벽면의 맨 아래 지면을 말한다.

# 2차원 벽면은 n*n 크기 정사각 격자 형태이며, 각 격자는 1*1 크기이다.
# 맨 처음 벽면은 비어있는 상태이다. 기둥과 보는 격자선의 교차점에 걸치지 않고,
# 격자 칸의 각 변에 정확히 일치하도록 설치할 수 있다.

#만약 (4, 2)에서 오른쪽으로 보를 먼저 설치하지 않고,
# (3, 2)에서 오른쪽으로 보를 설치하려 한다면 2번 규칙에 맞지 않으므로 설치가 되지 않습니다.
# 기둥과 보를 삭제하는 기능도 있는데 기둥과 보를 삭제한 후에 남은 기둥과 보들 또한 위 규칙을 만족해야 합니다.
# 만약, 작업을 수행한 결과가 조건을 만족하지 않는다면 해당 작업은 무시됩니다.

# 벽면의 크기 n, 기둥과 보를 설치하거나 삭제하는 작업이 순서대로 담긴 2차원 배열 build_frame이 매개변수로 주어질 때,
# 모든 명령어를 수행한 후 구조물의 상태를 return 하도록 solution 함수를 완성해주세요.

# 5 <= n <= 100
# 1 <= build_frame의 세로 <= 1000
# build_frame의 가로 = 4
# build_frame의 원소 = [x, y, a, b]
#   - x, y,는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태이다.
#   - a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타낸다.
#   - b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타낸다.
#   - 벽면을 벗어나게 기둥, 보를 설치하는 경우는 없다.
#   - 바닥에 보를 설치하는 경우는 없다.
# 구조물은 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽방향으로 설치 또는 삭제한다.
# 구조물이 겹치도록 설치하는 경우와, 없는 구조물을 삭제하는 경우는 입력으로 주어지지 않는다.
# 최종 구조물의 상태는 아래 규칙에 맞춰 return
#   - return 하는 배열은 가로 길이가 3인 2차원 배열로, 각 구조물의 좌표를 담고있어야 한다.
#   - return 하는 배열의 원소는 [x, y, a]
#   - x, y는 기둥, 보의 교차점 좌표이며, [가로좌표, 세로좌표] 형태이다.
#   - 기둥, 보는 교차점 좌표를 기준으로 오른쪽, 또는 위쪽 방향으로 설치되어 있음을 나타낸다.
#   - a는 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타낸다.
#   - return 하는 배열은 x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우, y 좌표 기준으로 오름차순 정렬
#   - x, y 좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 된다.

#     [1,0,0,1],
#     [1,1,1,1],
#     [2,1,0,1],
#     [2,2,1,1],
#     [5,0,0,1],
#     [5,1,0,1],
#     [4,2,1,1],
#     [3,2,1,1]
#   - 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 한다.
#   - 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 한다.

def solution(n, build_frame):
    answer = [[]]
    matrix = [['허공 '] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        matrix[0][i] = '바닥 '
    for x, y, a, b in build_frame:
        # 기둥
        if a == 0:
            # 설치
            if b == 1:
                if '바닥' in matrix[y][x] or '보 왼쪽' in matrix[y][x] or '보 오른쪽' in matrix[y][x] or '기둥 위' in matrix[y][x]:
                    matrix[y][x] += '기둥 아래 '
                    matrix[y+1][x] += '기둥 위 '
            # 삭제
            else:
                if matrix[y+1][x] == '보 중간':
                    matrix[y][x] = '허공 '
        # 보
        else:
            # 설치
            if b == 1:
                if '기둥 위' in matrix[y][x] or '기둥 위' in matrix[y][x+1]:
                    matrix[y][x] += '보 왼쪽 '
                    matrix[y][x+1] += '보 오른쪽 '
                elif '보 오른쪽' in matrix[y][x] and '보 왼쪽' in matrix[y][x+1]:
                    matrix[y][x] += '보 중간 '
                    matrix[y][x+1] += '보 중간 '
            # 삭제
            else:
                pass
    return matrix

# [가로좌표, 세로좌표, 구조물종류(기둥or보), (설치or삭제)]
#   [x,y,a,b]
#   a : 0 => 기둥
#     : 1 => 보
#   b : 0 => 삭제
#     : 1 => 설치
# arr = [
#     [1,0,0,1],
#     [1,1,1,1],
#     [2,1,0,1],
#     [2,2,1,1],
#     [5,0,0,1],
#     [5,1,0,1],
#     [4,2,1,1],
#     [3,2,1,1]
# ]
# print(solution(5, arr))
arr = [
    [0,0,0,1],
    [2,0,0,1],
    [4,0,0,1],
    [0,1,1,1],
    [1,1,1,1],
    [2,1,1,1],
    [3,1,1,1],
    [2,0,0,0],
    [1,1,1,0],
    [2,2,0,1]
]
solution(5, arr)