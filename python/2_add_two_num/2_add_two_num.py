# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carryBit = ListNode(0)
        addBit = ListNode(0)
        p1, p2 = l1, l2
        # addBit, carryBit = self.bit_add(p1.val, p2.val, carryBit)
        addBit.val, carryBit.val = self.add(p1, p2, carryBit)
        head = ListNode(addBit.val)
        tmp = head
    
        while(1):
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            if p1 or p2:
                addBit.val, carryBit.val = self.add(p1, p2, carryBit)
                tmp.next = ListNode(addBit.val)
                tmp = tmp.next
            elif carryBit.val:
                addBit.val, carryBit.val = self.add(p1, p2, carryBit)
                tmp.next = ListNode(addBit.val)
                tmp = tmp.next
            else:
                break
        return head

    # def bit_add(self, x, y, carryBit) -> tuple:
    #     sum = x + y + carryBit
    #     lowBit = sum % 10
    #     highBit = sum // 10
    #     return (lowBit, highBit)

    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     lowBit = 0
    #     highBit = 0
        
    
    def add(self, *args: ListNode) -> tuple:
        tmp = []
        [tmp.append(i.val) for i in args if i != None]
        result = sum(tmp)
        lowBit = result % 10
        highBit = result // 10
        return (lowBit, highBit)
            

    
    def LinkList(self, l: list) -> ListNode:
        head = ListNode(l.pop())
        tmp = head
        while(l):
            tmp.next = ListNode(l.pop())
            tmp = tmp.next
        return head
    def Output_Link(self, l:ListNode) -> None:
        while(1):
            print(l.val)
            if l.next == None:
                break
            l = l.next
sol = Solution()
a = [0]
b = [0]
l1 = sol.LinkList(a)
l2 = sol.LinkList(b)
result = sol.addTwoNumbers(l1,l2)
sol.Output_Link(result)