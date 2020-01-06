class Solution(object):
    def helper(self, n, mapper):
        if n in mapper:
            return mapper[n]
        res = 0
        for i in range(n):
            left = self.helper(n-1-i, mapper)
            right = self.helper(i, mapper)
            res += left * right 
        mapper[n] = res
        return res
    
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        mapper = {0: 1, 1: 1, 2: 2, 3: 5 }
        return self.helper(n, mapper)


if __name__ == '__main__':
	sol = Solution()
	print(sol.numTrees(13))