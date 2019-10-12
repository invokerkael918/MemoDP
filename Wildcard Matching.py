class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    def isMatch(self, source, pattern):
        # write your code here
        return self.is_match_helper(source, 0, pattern, 0, {})

    def is_match_helper(self, source, i, pattern, j, memo):

        if (i, j) in memo:
            return memo[(i, j)]
        # source is empty, pattern must be all *

        if len(source) == i:
            for index in range(j, len(pattern)):
                if pattern[index] != "*":
                    return False
            return True

        # not found
        if j == len(pattern):
            return False

        if pattern[j] != "*":
            matched = self.is_match_char(source[i], pattern[j]) and self.is_match_helper(source, i + 1, pattern, j + 1,
                                                                                         memo)
        # pattern[j] = *
        else:
            matched = self.is_match_helper(source, i + 1, pattern, j, memo) or self.is_match_helper(source, i, pattern,
                                                                                                    j + 1, memo)

        memo[(i, j)] = matched

        return matched

    def is_match_char(self, s, p):
        return s == p or p == "?"
