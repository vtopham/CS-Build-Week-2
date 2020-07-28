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
            

#stack queue

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = []
        
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        
        """
        self.storage.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.storage.pop(0)
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.storage[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.storage) > 0:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()