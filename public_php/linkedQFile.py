
class Node:
    def __init__(self):
        self.value=None
        self.next=None

class LinkedQ:
    def __init__(self):
        self.__first=None #privata attribut mha __
        self.__last=None

    def enqueue(self,input): #lägg till ny nod
        nod=Node() #skapa en ny nod
        nod.value=input #ansätt värde
        if self.isEmpty(): #om tom
            self.__first=nod
            self.__last=nod
        else:
            self.__last.next=nod #skapa pil mellan sista noden och den nya
            self.__last=nod #ansätt den nya till den sista

    def dequeue(self): #ta bort första noden. Value ges som output
        if self.isEmpty(): #om tom
            return None
        if self.__first==self.__last:
            out=self.__first.value
            self.__first=None
            self.__last=None
            return out
        else:
            out=self.__first.value
            self.__first=self.__first.next
            return out

    def isEmpty(self): #kolla om tom
        if self.__first==None:
            return True
        else:
            return False

    def remove(self,input): #ta bort nod med value=input
        if not self.isEmpty(): #om ej tom
            if self.__first.value==input: #om den första ska tas bort
                self.__first=self.__first.next #första = nod 2
            else:
                nod=self.__first #startvärde för iteration
                while nod.next.next!=None:
                    if nod.next.value==input: #om vi vill ta bort nästa nod
                        nod.next=nod.next.next #peka om så att nästa blir nästnästa
                    else: #om vi ej vill ta bort den
                        nod=nod.next #iterera till nästa nod
                if self.__last.value==input: #om vi vill ta bort sista noden
                    self.__last=nod #peka om sista till näst sista
                    nod.next=None

    def visa(self): #printar hela listan (ingår inte i uppgiften)
        if not self.isEmpty():
            nod=self.__first
            while nod!=None:
                print(nod.value)
                nod=nod.next
        else:
            print('There are no nodes')

