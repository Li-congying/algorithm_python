class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        candidates.sort()
        def dfs(candidates, target, index, set_):

            if target < 0:
                return False

            set_.append(candidates[index])
            if target == candidates[index]:
                self.result.append(set_)
                return

            for i in range(index, len(candidates)):
                if candidates[i] > target:
                    break
                dfs(candidates, target - candidates[index], i, set_[:])

        for i in range(len(candidates)):
            set_ = []
            dfs(candidates, target, i, set_)

        return self.result

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return []
        self.result2 = []
        candidates.sort()

        def dfs(candidates, index, target, set_):
            if target < 0:
                return False

            set_.append(candidates[index])
            if target == candidates[index]:
                self.result2.append(set_)
                return
            for i in range(index+1, len(candidates)):
                if candidates[i] > target-candidates[index]:
                    break
                if i > index+1 and candidates[i] == candidates[i-1]:
                    continue
                dfs(candidates, i, target-candidates[index], set_[:])

        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue

            dfs(candidates, i, target, [])

        return self.result2

s = Solution()


#print s.combinationSum([1,2],3)
print s.combinationSum2([4,4,2,2,3,1], 11)




