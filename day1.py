#Linked list cycle
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        cur = head
        track = {}
        while cur != None:
            if cur.next in track:
                return cur.next
            track[cur] = True
        
            cur = cur.next
        return None
            

#contains duplicates

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        tracking = {}
        
        for num in nums:
            if num in tracking:
                return True
            tracking[num] = True
        
        return False


#add two numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        
       
        
        node1 = l1
        node2 = l2
        
        output = None
        
        carry = 0
        
        while node1.val != None or node2.val != None:
            
            #add
            if node1.val == None:
                val1 = 0
            else:
                val1 = node1.val
            
            if node2.val == None:
                val2 = 0
            else:
                val2 = node2.val
            
            sum_val = val1 + val2 + carry
            remainder = sum_val % 10
            
            carry = (sum_val - remainder) / 10
            
            #add to linked list and carry
            new_node = ListNode(remainder, None)
            if output == None:
                output = new_node
                cur = new_node
            else:
                cur.next = new_node
                cur = new_node
            
            #keep going
            if node1.next == None:
                node1 = ListNode(None, None)
            else:
                node1 = node1.next
                
            if node2.next == None:
                node2 = ListNode(None, None)
            else:
                node2 = node2.next
        if carry != 0:
            new_node = ListNode(carry, None)
            cur.next = new_node
        return output
            
            
