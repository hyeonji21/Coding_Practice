def solution(n, k):
    answer = 0
    count = 0
    
    count = n // 10

    k = k - count
        
    answer = (n * 12000) + (k * 2000)
    
    return answer