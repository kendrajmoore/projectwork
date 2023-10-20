

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.get_mid(head)
        left, right = self.sortList(head), self.sortList(mid)
        return self.merge(left, right)

    def get_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            if list1:
                tail.next = list1
            if list2:
                tail.next = list2

        return dummy.next

    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def swapNode(self, head, k):
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        if 2 * k - 1 == length:
            return head

        first_node = head
        for i in range(k -1):
            first_node = first_node.next

        second_node = head
        for j in range(length - k):
            second_node = second_node.next

        first_node.val, second_node.val = second_node.val, first_node.val
        return head
    
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

    def mergeTwoLists(self, list1, list2):
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
        node.next = list1 or list2
        return dummy.next




head = [4,2,1,3]

