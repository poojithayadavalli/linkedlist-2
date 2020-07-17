class Node:
  def __init__(self,val):
    self.data=val
    self.next=None
    
def linkedList(llist):
  head=Node(llist[0])
  temp=head
  for i in range(1,len(llist)):
    temp.next=Node(llist[i])
    temp=temp.next
  return head

def display(head):
  l=[]
  while head:
    l.append(str(head.data))
    head=head.next
  return "".join(l)
def solution(head):
  if head==None:
    return False
  cur = head
  while cur and cur.next:
    pre=head
    temp=head.next
    while pre and temp:
      flag=True
      if pre.data + temp.data <=0:
        flag=False
        if head==pre:
          pre=temp.next
          temp=pre.next
          head=pre
        else:
          temp1.next=temp.next
          pre=temp1.next
          if pre:
            temp=pre.next
          else:
            break
      else:
        temp1=pre
        pre=pre.next
        temp=temp.next
    cur=cur.next
    if flag:break
  return head
 
llist=list(map(int,input().split()))
head=linkedList(llist)
head=solution(head)
print(display(head))
