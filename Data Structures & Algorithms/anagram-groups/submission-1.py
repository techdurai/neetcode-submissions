class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for s in strs:
            key = ''.join(sorted(s))

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())

        return list(sdict.values())

sol = Solution()
strs = ["act","pots","tops","cat","stop","hat"]
print(sol.groupAnagrams(strs))
