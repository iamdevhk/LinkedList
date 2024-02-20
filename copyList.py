class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapp={None:None}
        temp=head
        while(temp):
            newNode=Node(temp.val)
            mapp[temp]=newNode
            temp=temp.next
        temp=head
        while(temp):
            copy=mapp[temp]
            copy.next=mapp[temp.next]
            copy.random=mapp[temp.random]
            temp=temp.next
        return mapp[head]
        