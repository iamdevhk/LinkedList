class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            count=0
            temp=head
            while temp:
                count+=1
                temp=temp.next
            print(count)
            remove=count-n
            temp1=head
            if count==1:
                return None
            if remove==0:
                return head.next
            for i in range(remove-1):
                temp1=temp1.next
            
        
            
            temp1.next=temp1.next.next
            return head