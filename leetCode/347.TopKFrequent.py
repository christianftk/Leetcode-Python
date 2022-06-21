class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        numset = set(nums)
        output = []
        defvalue = []
        for i in range(len(numset)):
            defvalue.append(0)

        countdic = dict(zip(numset,defvalue))
        print(countdic)
        for num in nums:
            countdic[num] += 1

        print(countdic)

        countdicord = sorted(countdic.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            output.append(countdicord.pop(0)[0])

        return output



nums = [1, 1, 1, 2, 2, 3, 1, 44, 4, 2, 3, 2, 2, 2, 5532]
k = 2
print(Solution.topKFrequent(Solution,nums,k))
