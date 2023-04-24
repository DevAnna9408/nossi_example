# sortAndTwoPointer
# 배열의 다양한 활용

# 1. 반복문
# 2. Sort & Two Pointer

# Sort: 정렬이 안된 리스트를 정렬할 때 걸리는 시간 복잡도는 O(n Log n)이다.
# twoPointer : 배열 중 두 개의 포인터를 왔다갔다 하면서 답을 찾아가는 과정(정렬이 된 배열에서 사용)

# Q. 정수가 저장된 배열 nums가 주어졌을 때, nums의 원소 중 두 숫자를 더해서 target 이 될 수 있으면 True, 불가능하면 False를 반환한다.
# 같은 원소를 두 번 사용할 수 없다.

# 접근방법으로의 풀이

# 정렬을 했다고 가정, 양 끝의 숫자를 더했을 때 target보다 크면 오른쪽 끝 숫자를 한 칸 왼쪽으로 이동
# target보다 작으면 왼쪽 끝 숫자를 오른쪽으로 한 칸 이동
# 왼쪽, 오른쪽이 같은 숫자를 가리킬 때 까지 반복함

def sortAndTwoPointer(nums, target):
    nums.sort()
    l, r = 0, len(nums)-1
    while l<r:
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] == target:
            return True

    return False

print(sortAndTwoPointer([4, 1, 9, 7, 5, 3, 16], 14))





