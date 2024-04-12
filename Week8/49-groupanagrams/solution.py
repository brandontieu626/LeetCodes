class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=collections.defaultdict(list)

        for word in strs:
            char=[0]*26

            for c in word:
                char[ord(c)-ord('a')]+=1
            
            res[tuple(char)].append(word)
        
        return res.values()