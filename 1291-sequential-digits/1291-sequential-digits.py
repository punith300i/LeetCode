class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def solve(low, high, number, last_digit, answer):
            if low <= number <= high: answer.append(number)
            if number > high or last_digit == 9: return
            new_number, new_digit = number * 10 + last_digit + 1, last_digit + 1
            solve(low, high, new_number, new_digit, answer)
        answer = []
        for i in range(1, 10): solve(low, high, i, i, answer)
        answer.sort()
        return answer
        
    