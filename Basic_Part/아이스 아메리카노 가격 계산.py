def solution(money):
    answer = []
    num1 = money // 5500
    num2 = money % 5500
    
    answer = [num1, num2]
    
    return answer