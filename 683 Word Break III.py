class SolutionOptimized:
    """
    With Memo optimize
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dict):
        # Write your code here
        if not dict:
            return 0

        maxLength = len(max(dict, key=lambda item: len(item)))
        low_dict = list(map(lambda x: x.lower(), dict))
        memo = {}
        return self.dfs(s.lower(), low_dict, 0, maxLength,memo)

    def dfs(self, s, dict, start, maxLength,memo):
        if start in memo:
            return memo[start]
        if start == len(s):
            return 1
        ans = 0
        for i in range(start, len(s)):
            if i + 1 - start > maxLength:
                break
            word = s[start:i + 1]
            if word not in dict:
                continue
            ans += self.dfs(s, dict, i + 1, maxLength,memo)
        memo[start] = ans
        return ans

class Solution:
    """
    Without Memo optimize
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here
        if not dict:
            return 0

        maxLength = len(max(dict, key=lambda item: len(item)))
        low_dict = list(map(lambda x: x.lower(), dict))

        return self.dfs(s.lower(), low_dict, 0, maxLength)

    def dfs(self, s, dict, start, maxLength):
        if start == len(s):
            return 1
        ans = 0
        for i in range(start, len(s)):
            if i + 1 - start > maxLength:
                break
            word = s[start:i + 1]
            if word not in dict:
                continue
            ans += self.dfs(s, dict, i + 1, maxLength)

        return ans


class MySolution:
    """
    Without memo Optimize
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here
        if not dict:
            return 0
        result = []
        maxLength = len(max(dict, key=lambda item: len(item)))
        low_dict = list(map(lambda x: x.lower(), dict))

        self.dfs(s.lower(), low_dict, 0, maxLength, [], result)
        return len(result)

    def dfs(self, s, dict, start, maxLength, path, result):

        if start == len(s):
            result.append("".join(path))

        for i in range(start, len(s)):

            if i + 1 - start > maxLength:
                break
            word = s[start:i + 1]
            if word not in dict:
                continue
            path.append(word)
            self.dfs(s, dict, i + 1, maxLength, path, result)
            path.pop()
if __name__ == '__main__':
    S = SolutionOptimized().wordBreak3("Catmat",["Cat","mat","Ca","tm","at","C","Dog","og","Do"])
    print(S)