class Node :
    
    def __init__(self, value) :
        self.value = value
        self.child = self.left = self.right = self.parent = None

class LinkedList :
    
    def __init__(self) :
        self.tail = None
        self.head = None

class FibonacciHeap(Heap):

    def __init__ (self, min) :
        self.min = None
        root_list = LinkedList()


    def insert(self, value) :
        node = Node(value)

        if self.min  > node.value :
            return   
        
        if LinkedList.head = None :
            LinkedList.head = node
            node.left = None
            return

        if not self.root_list :    
            node.left = LinkedList.tail
            LinkedList.tail.right = LinkedList.tail = self.min = node
            return


    def find_min(self) -> int:
        return self.min


    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: Heap) -> None:
        """
        Fusionne deux arbres
        """
        pass