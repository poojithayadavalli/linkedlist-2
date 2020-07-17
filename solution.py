class Node:
  def __init__(self,val):
    self.data=val
    self.next=None
    
def linkedList(llist):
  head=Node(llist(0))
  temp=head
  for i in range(1,len(llist)):
    temp.next=Node(llist[i])
    temp=temp.next
  return head

def solution(head):
  if head==None:
    return
  pre=cur=head
  temp=head.next
  while cur and cur.next:
    while pre and temp:
      if pre.data+temp.data<=0:
        if head==head:
          head=temp.next
          pre=head
          tem=head.next
        else:
          temp1.next=temp.next
          pre=temp.next
          temp=pre.next
      else:
        temp1=pre
        pre=pre.next
        temp=temp.next
    cur=cur.next
def display(head):
  l=[]
  while head:
    l.append(str(head.data))
  print(" ".join(l))
llist=list(map(int,input().split()))
head=linkedList(llist)
display(solution(head))
