class SolutionDP:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak3(self, s, dict):
        # write your code here

        if not s or not dict:
            return 0
        n = len(s)
        dict = [x.lower() for x in dict]
        s = s.lower()

        f = [0] * (n + 1)
        f[0] = 1
        # dp 存前边所有点到current point有多少种方法
        # 最后一位存答案
        maxLength = max([len(w) for w in dict])
        for i in range(n + 1):
            for j in range(1, min(i, maxLength) + 1):
                # 一个单词，插板最多情况为自身长度
                # maxLength是dict的限制可以最大插板数量
                # C/at Ca/t Cat/
                if f[i - j] == 0:
                    # 插板情况不存在，Example : Ca/t, i = 2 j = 2
                    continue
                if s[i - j:i] in dict:
                    f[i] += f[i - j]

        return f[-1]

class SolutionMemo:
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

class SolutionDFS:
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
    S = SolutionDP().wordBreak3("Catmat",["Cat","mat","Ca","tm","at","C","Dog","og","Do"])
    print(S)