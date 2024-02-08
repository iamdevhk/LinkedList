#143. Reorder List 
#leetcode 143

#You are given the head of a singly linked-list. The list can be represented as:

#L0 → L1 → … → Ln - 1 → Ln
#Reorder the list to be on the following form:
#L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle of the list using two pointer approach
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #reverse the second of the list
        prev=None
        curr=slow.next
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        #remove connection between first half and second half
        slow.next=None

        #merge the first half and revsered second half
        sHalf=prev
        fHalf=head
        while sHalf:
            #save the next nodes
            temp1=fHalf.next
            temp2=sHalf.next

            #reorder the nodes
            fHalf.next=sHalf
            sHalf.next=temp1

            #move the pointers to next whcih is saved in the temp
            fHalf=temp1
            sHalf=temp2