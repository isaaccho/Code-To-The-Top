class node:
    def __init__(self,value = None):
        self.value = value
        self.next = None



class linked_list:
    def __init__(self):
        self.head = node()

#this append will append this node to the end
    def append(self,value):
        new_node = node(value)
        cur = self.head
        while cur.next!=None:
            cur = cur.next

        cur.next = new_node

    def display(self):
        llist = []
        elems = []
        rnn = self.head
        while rnn.next !=None:
            rnn = rnn.next
           # llist = llist + rnn.value
            elems.append(rnn.value)
        #print (llist)
        print (elems)

    def delete(self,index):
        cur_index = 0
        del_node = self.head
        while del_node.next !=None:
            last_node = del_node
            del_node = del_node.next
            if cur_index ==index:
                
                last_node.next = del_node.next
                return
            cur_index = cur_index +1
        

new_n =  linked_list();
new_n.display()
new_n.append(1)
new_n.append(2)
new_n.append(3)
new_n.append(8)
new_n.display()
new_n.delete(2)
new_n.display()
new_n.delete(2)
new_n.display()
