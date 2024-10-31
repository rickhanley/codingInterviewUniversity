class Array:
    
    def __init__(self, initialSize):    # constructor
        self.__a = [None] * initialSize # the array stored as a list
        self.nItems = 0                 # No items in array initially
        
    def insert(self, item):             # Insert item at end
        self.__a[self.nItems] = item    # item goes at current end
        self.nItems += 1                # Incremement number of items
        
    def search(self, item):
        for j in range(self.nItems):
            if self.__a[j] == item:
                return self.__a[j]
            
        return None
    
    def delete(self, item):
        for j in range(self.nItems):
            if self.__a[j] == item:
                for k in range(j, self.nItems):
                    self.__a[k] = self.__a[k + 1]
                self.nItems -= 1
                return True
    
        return False

    def traverse(self, function = print):
        for j in range(self.nItems):
            function(self.__a[j])