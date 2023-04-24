# twoSum

# Q. 정수가 저장된 배열 nums가 주어졌을 때, nums의 원소 중 두 숫자를 더해서 target 이 될 수 있으면 True, 불가능하면 False를 반환한다.
# 같은 원소를 두 번 사용할 수 없다.

# 직관적으로 생각하기로의 풀이

# 완전 탐색으로 시작 -> 문제 상황을 단순화 하기 -> 문제 상황을 극한으로 만들기
# 전부 다 더해보면 되지 않을까? -> 더해보니 14가 되는게 있다 -> 숫자가 무한대로 늘어난다면 어떻게 비교 할 것인가?

def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return True
    return False


print(twoSum(nums=[4, 1, 9, 7, 5], target=14))
