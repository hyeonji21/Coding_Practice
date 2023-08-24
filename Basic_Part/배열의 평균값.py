def solution(numbers):
    answer = 0
    sum_ = 0
    for i in numbers:
        sum_ += i
    answer = sum_ / len(numbers)
    return answer