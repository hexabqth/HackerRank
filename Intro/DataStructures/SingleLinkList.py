#Node class
class Node:
    def __init__(self,**kwargs):
        self.dataval=kwargs.get('dataval')
        self.nextval=None
        return

#Creating list class
class SingleLink:

    def __init__(self,**kwargs):
        self.startval=None
        self.head=None
        

        return

    def inserthead(self,**kwargs):

        node=kwargs.get('node')
        if self.startval == None :
            self.startval=node
            self.head=node
        else :
            temp=self.head
            self.head=node
            temp.nextval=node
        
        return
            

    
    def insertstart(self,**kwargs):

        node=kwargs.get('node')
        temp=self.startval
        self.startval=node
        node.nextval=temp

        return

    def insertmiddle(self,**kwargs):
        #e3 will be inserted between e1 and e2
        e1=kwargs.get('node1')
        e2=kwargs.get('node2')

        #node to be inserted
        e3=kwargs.get('node3')

        temp=e1.nextval
        e1.nextval=e3 
        e3.nextval=e2
        
        return
    
    def delete(self,**kwargs):
        
        #node to be deleted
        e1=kwargs.get('node')
        if self.startval is self.head:
            self.start=None
            self.head=None

        # if we want to delete start of ll
        elif self.startval is e1:
            self.startval=e1.nextval

        # delete middle element 
        elif e1 is not self.startval and e1 is not self.head:
            nv=self.startval
            while True:
                nv=self.nextval(startval=nv)
                if nv.nextval is e1:
                    break
            nv.nextval=e1.nextval


        #delete last element
        else:
            nv=self.startval
            while True:
                nv=self.nextval(startval=nv)
                if nv.nextval is e1:
                    break
            self.head=nv

        return


    def nextval(self,**kwargs):
        startval=kwargs.get('startval')
        return self.startval if startval.nextval is None else startval.nextval

     


    
e1=Node(dataval='Monday')
sl=SingleLink()
sl.inserthead(node=e1)
e2=Node(dataval='Tuesday')
sl.inserthead(node=e2)
e3=Node(dataval='Wednesday')
sl.insertmiddle(node1=e1,node2=e2,node3=e3)
print(sl.startval.dataval)

print(sl.nextval(startval=e1).dataval)
print(sl.head.dataval)
sl.delete(node=e1)
print(sl.startval.dataval,sl.head.dataval)
sl.delete(node=e2)
print(sl.startval.dataval,sl.head.dataval)
sl.delete(node=e3)
print(sl.startval,sl.head)