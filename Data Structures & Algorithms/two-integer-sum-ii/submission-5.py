class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        e = len(numbers) - 1
        while True:
            a = numbers[s]
            b = numbers[e]
            """
            given that a + b is greater than target, 
            any element > a will not be a part of solN with b
            """
            if a + b == target:
                return [s+1, e+1]
            if a + b > target:
                e -= 1
            elif a + b < target:
                """
                same story opposite logic
                """
                s += 1   
