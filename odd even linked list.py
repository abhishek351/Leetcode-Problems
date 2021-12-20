class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        
        oddptr=current=head
        evenptr=evenstart=head.next
        i=1
        while current:
            if i >2   and i%2!=0:
                oddptr.next=current
                oddptr=oddptr.next
            elif i>2 and i%2==0:
                evenptr.next=current
                evenptr=evenptr.next
            current=current.next
            i+=1
        evenptr.next=None
        oddptr.next=evenstart
        
        return  head