# Valid Parentheses, 괄호 유효성 문제

# (){}[]를 포함하고 있는 문자열 string이 주어졌을 때, 괄호가 유효한지 아닌지 판별하시오.

def check_parentheses(value):
    new_stack = []

    for c in value:
        if c == "(":
            new_stack.append(")")
        elif c == "{":
            new_stack.append("}")
        elif c == "[":
            new_stack.append("]")
        elif not new_stack or new_stack.pop() != c:
            print("false")
            return False
    print("true")
    return True

check_parentheses("{(([]))[]}")

# Daily Temperature

# 매일 온도를 나타내는 int형 배열 temperatures가 주어진다. answer 배열의 원소 answer[i]는 i번째 날의 온도보다
# 더 따듯해지기까지 며칠을 기다려야 하는지 나타낸다.
# 만약 더 따듯해지는 날이 없다면 answer[i] == 0이다.
# answer 배열을 반환하는 함수를 구현하시오

# 1 <= tempatratures.length <= 10의5승
# 30 <= temperatures[i] <= 100

# 이중 포문, 시간 복잡도 O(n제곱이라서 시간복잡도는 탈락)
def answer(temperatures):
    new_answer = []
    for t in temperatures:
        for j in temperatures:
            pass

def nossi_answer(temperatures):
    new_answer = [0] * len(temperatures) # ans 배열을 모두 0으로 초기화
    new_stack = [] # 우리가 사용할 stack
    for cur_day, tem in enumerate(temperatures): #enumurate는 인자로 넘어온 목록을 기준으로 인덱스와 원소를 차례대로 접근하게 해 주는 객체이다.
        while new_stack and new_stack[-1][1] < tem:
            prev_day, _ = new_stack.pop()
            new_answer[prev_day] = cur_day = prev_day
        new_stack.append((cur_day, tem))
    return new_answer