class Solution:

    @staticmethod
    def getStringDict(s):
        s_dict = dict()
        for char in s:
            if char in s_dict.keys():
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        return s_dict

    @staticmethod
    def isAnagram(s1, s2):
        s1_dict = Solution.getStringDict(s1)
        s2_dict = Solution.getStringDict(s2)
        for key in s1_dict.keys():
            if s1_dict[key] != s1_dict[key]:
                return False
        for key in s2_dict.keys():
            if not s1_dict[key] == s1_dict[key]:
                return False
        return True

    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        anagrams = list()
        for i, string1 in enumerate(strs):
            localAnagrams = list()
            for string2 in strs[i+1:]:
                if Solution.isAnagram(string1, string2):
                    localAnagrams.append(string2)
            if localAnagrams:
                localAnagrams.append(string1)
                anagrams.append(localAnagrams)
        return anagrams


print(Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
