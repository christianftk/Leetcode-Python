#input is sorted already
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        size = len(numbers)
        for x in range(size):
            curr = target - numbers[x]
            for y in range(x+1,size):
                if numbers[y] > curr:
                    break
                elif numbers[y] == curr:
                    return [x+1, y+1]
        return []

numbers = [2, 7, 11, 15]
target = 9
print(Solution.twoSum(Solution,numbers,target))
