#two sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        """
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return None
        
#group anagrams

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
    
        dict = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in dict:
                dict[key].append(word)
            else:
                dict[key] = [word]
        output = []
        
        for item in dict:
            output.append(dict[item])
            
        return output
            