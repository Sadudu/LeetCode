        
        
        
        
        re = ListNode(0)
        r = re
        c = 0
        while(l1 or l2):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            s = val1 + val2 + c
            c = s//10
            r.next = ListNode(s%10)
            r = r.next
            if(l1 != None): l1 = l1.next
            if(l2 != None): l2 = l2.next
            
        if(c):r.next = ListNode(1)
        return re.next
        
        
        
        
        
        
        class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = l1
        c = 0
        over = True
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            while(True):
                s = l1.val+l2.val + c
                l1.val = s%10
                c = s//10
                if(l1.next == None):
                    l1.next = l2.next
                    break
                if(l2.next == None):
                    break
                l1 = l1.next
                l2 = l2.next
            while(c!=0):
                if(l1.next == None):
                    l1.next = ListNode(1)
                    break
                else:
                    l1 = l1.next
                    s = l1.val + c
                    l1.val = s%10
                    c = s//10                   
            return re
        
        
        
