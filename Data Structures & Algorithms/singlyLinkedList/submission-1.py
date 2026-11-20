class LinkedListNode:

    def __init__(self, val, next_node=None):
        self.value =val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = self.head

    
    def get(self, index: int) -> int:
        if not self.head:
            return -1
        current1= self.head
        current = self.head
        count = 1
        while current1.next != None:
            current1= current1.next
            count +=1
        

        
        if index >0 and index< count:
            for x in range(0, index):
                current = current.next

            return current.value
        elif index ==0:
            return self.head.value
        else:
            return -1        
        

    def insertHead(self, val: int) -> None:
        if self.head is None:
            k = LinkedListNode(val)
            self.head = k
            self.tail =k 
        else:
            old_head = self.head
            new_node = LinkedListNode(val, old_head)
            self.head = new_node
        
        

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = LinkedListNode(val, None)
            self.tail = self.head
        else:
            current = self.head
            new = LinkedListNode(val, None)
            while current.next !=None:
                current = current.next
            current.next = new
            self.tail = new

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        current1= self.head
        current = self.head
        count = 1
        while current1.next != None:
            current1= current1.next
            count +=1
        

        
        if index >0 and index< count:
            for x in range(0,index-1):
                current= current.next
                

            
            current.next = current.next.next

            return True
        elif index==0:
            self.head=self.head.next

            return True
        else:
            return False


        

    def getValues(self) -> List[int]:
        if self.head is None:
            return []
        else:
            current =self.head

            list1 = []
            list1.append(self.head.value)

            while current.next!=None:
                current=current.next
                list1.append(current.value)

            return list1

        
