#
# @lc app=leetcode id=1931 lang=python3
#
# [1931] Painting a Grid With Three Different Colors
#

# @lc code=start
class Solution:
   
        # Approach 1: Column by column DP
        # Time Complexity: O(3^2m * m)
        # Space Complexity: O(3^2m * n)
    #     MOD = 10**9 + 7
    #     # generate all valid column patterns
    #     cols = []
    #     def dfs_build(col, last_color):
    #         i = len(col)
    #         if i == m:
    #             cols.append(tuple(col))
    #             return
    #         for c in (0, 1, 2): #0 = red, 1 = green, 2 = blue
    #             if c != last_color:
    #                 col.append(c)
    #                 dfs_build(col, c)
    #                 col.pop()
    #     dfs_build([], -1)
    #     S = len(cols)
        
    #     # precompute which patterns can follow which
    #     can_follow = [[False] * S for _ in range(S)]
    #     for i in range(S):
    #         for j in range(S):
    #             ok = True
    #             for row in range(m):
    #                 if cols[i][row] == cols[j][row]:
    #                     ok = False
    #                     break
    #             can_follow[i][j] = ok
       
    #    # dp over columns, rolling 1D
    #     prev = [1] * S # dp for column 0
    #     for _ in range(1, n):
    #         curr = [0] * S
    #         for j in range(S):
    #             total = 0
    #             for i in range(S):
    #                 if can_follow[i][j]:
    #                     total += prev[i]
    #             curr[j] = total % MOD
    #         prev = curr
    #     # sum of all possible ways to paint the last column
    #     return sum(prev) % MOD
    
    # Approach 2: Matrix Exponentiation
    # Time Complexity: O(3^m * log n)
    # Space Complexity: O(3^2m)
    MOD = 10**9 + 7
    @staticmethod
    def mat_mult(A, B):
        """
        Multiply two S×S matrices A and B modulo MOD.
        Returns C = A·B.
        Time: O(S^3)
        """
        S = len(A)
        # initialize result matrix with zeros
        C = [[0]*S for _ in range(S)]
        for i in range(S):
            for k in range(S):
                if A[i][k]:
                    aik = A[i][k]
                    # accumulate row i of A times column j of B
                    for j in range(S):
                        C[i][j] = (C[i][j] + aik * B[k][j]) % Solution.MOD
        return C

    @staticmethod
    def mat_pow(mat, exp):
        """
        Fast exponentiation of an S×S matrix 'mat' to power 'exp' modulo MOD.
        Uses binary exponentiation in O(S^3 · log exp).
        """
        S = len(mat)
        # start with identity matrix
        res = [[1 if i==j else 0 for j in range(S)] for i in range(S)]
        base = mat
        while exp > 0:
            if exp & 1:
                res = Solution.mat_mult(res, base)
            base = Solution.mat_mult(base, base)
            exp >>= 1
        return res

    def colorTheGrid(self, m: int, n: int) -> int:
        """
        Returns the number of ways to color an m×n grid with 3 colors
        so that no two adjacent cells share the same color, modulo 1e9+7.
        This uses:
        - State-compression: each column is one integer s in [0,3^m),
            encoding colors in base-3.
        - Precompute T[i][j]=1 if state valid[i] can be next to valid[j].
        - dp_j = T · dp_{j-1}  ⇒  dp_{n-1} = T^(n-1) · dp_0.
        Overall time: O(m·3^m + 3^(3m)·log n).
        """
        # 1) Enumerate all valid column-states (no vertical repeats)
        max_state = 3**m
        valid = []
        for s in range(max_state):
            x, ok = s, True
            prev = x % 3
            x //= 3
            for _ in range(1, m):
                cur = x % 3
                if cur == prev:
                    ok = False
                    break
                prev = cur
                x //= 3
            if ok:
                valid.append(s)

        S = len(valid)
        idx = {s:i for i,s in enumerate(valid)}  # map state→index

        # 2) Build transition matrix T of size S×S
        #    T[i][j] = 1 if valid[i] and valid[j] differ in every row
        T = [[0]*S for _ in range(S)]
        for i, s in enumerate(valid):
            for j, t in enumerate(valid):
                x, y = s, t
                good = True
                for _ in range(m):
                    if (x % 3) == (y % 3):
                        good = False
                        break
                    x //= 3
                    y //= 3
                if good:
                    T[i][j] = 1

        # 3) Exponentiate T to the (n-1)th power
        #    dp_0 is a vector of all 1's (any valid first-column state)
        if n == 1:
            # Special case: only one column, just count valid states
            return S

        Tn = Solution.mat_pow(T, n-1)

        # 4) Multiply Tn by dp_0 and sum entries
        #    dp_n[i] = sum_j Tn[i][j] * dp_0[j] = sum_j Tn[i][j]
        result = 0
        for i in range(S):
            result = (result + sum(Tn[i])) % Solution.MOD

        return result

       
# @lc code=end

