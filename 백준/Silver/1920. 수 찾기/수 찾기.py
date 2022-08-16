import sys

#이분 탐색
#입력: 정렬된 리스트 a, 찾는 값 x
#출력: 찾으면 그 값의 위치, 찾지 못하면 -1

def binary_search(a, x):
    start=0
    end = len(a)-1  #끝 값의 인덱스
    while start<=end: #끝 값까지 반복
        mid=(start+end)//2 #나눌 값은 중간 값
        if x==a[mid]:       #같으면 인덱스 반환
            return 1
        elif x>a[mid]:      #찾는 값이 더 크면 큰 범위서 찾음
            start=mid+1
        else:               #찾는 값이 더 작으면 작은 범위서 찾음
            end = mid-1
    return 0


input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()

for i in range(m):
    aa = b.pop(0)
    print(binary_search(a, aa))
