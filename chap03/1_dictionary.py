# dictionary: 내부 동작이 해시 테이블로 되어있는 자료구조.

# ex)
# 리스트로 저장 할 경우, 각 숫자가 어떤 key인지 확인할 수 없다.
score = [97, 49, 89]

new_score = { 'math': 97, 'eng': 49, 'kor': 89 }
print(new_score['math'])
new_score['math'] = 45
print(new_score['math'])

if 'math' in new_score:
    print(new_score['math'])
else:
    print('false')

# Dictionary in Two Sum

# Q. 정수가 저장된 배열 nums가 주어졌을 때, nums의 원소 중 두 숫자를 더해서 target 이 될 수 있으면 True, 불가능하면 False를 반환한다.
# 같은 원소를 두 번 사용할 수 없다.

def dict(value, answer):
    new_dict = {}
    for v in value:
        new_dict[v] = True

    for d in new_dict:
        need = answer - d
        if need in new_dict and need != d:
            return True
    return False

print(dict([4, 1, 9, 7, 8, 2], 14))

# Longest Consecutive Sequence

# 정렬되어 있지 않은 정수형 배열 nums가 주어졌다. nums 원소를 가지고 만들 수 있는 가장 긴 연속된 수의 갯수는 몇 개인지 반환하시오

def longest_nums(nums):

    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1
    else:
        new_nums = {}
        answer = 0

        for n in nums:
            new_nums[n] = 0

        for n in nums:
            if n-1 not in new_nums:
                cnt = 1
                target = n + 1
                while target in new_nums:
                    cnt += 1
                    target += 1
                    print(cnt)
                answer = max(answer, cnt)
        return answer

print(longest_nums([6, 3, 100, 5, 4, 4]))

