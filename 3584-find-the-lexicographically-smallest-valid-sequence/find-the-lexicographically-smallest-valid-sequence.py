class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        # suf[i] = number of characters of word2
        # that can be matched using word1[i:]
        suf = [0] * (n + 1)
        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suf[i] = m - 1 - j

        ans = []
        j = 0
        changed = False

        for i in range(n):
            if j == m:
                break

            # Normal matching
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use the one allowed modification
            elif not changed:
                remaining = m - j - 1

                if suf[i + 1] >= remaining:
                    ans.append(i)
                    j += 1
                    changed = True

        if j == m:
            return ans

        return []