class Array:
    def __init__(self, initialSize):        # constructor for our own Array class
        self.__a = [None] * initialSize     # __a is our Array variable instance declaration
        self.__nItems = 0                   # __nItems is out number of items in the array instance declaration
        
    def __len__(self):                      # use dunder __len__ so we can call it as a method
        return self.__nItems
    
    def get(self, n):                       # def get method
        if 0 <= n and n < self.__nItems:    # if n is > 0 and n less than nItems i.e. within the range of the array
            return self.__a[n]              # return __a[n]
        
    def set(self, n, value):                # def set method
        if 0 <= n and n < self.__nItems:    # if n is > 0 and n less than nItems i.e. within the range of the array
            self.__a[n] = value             # set __a[n] = value
            
    def insert(self, item):                 # insert item @ __nItems index
        self.__a[self.__nItems] = item      # increment __nItems
        self.__nItems += 1
        
    def find(self, item):                   # loop over array looking for item match
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return j
        return -1
    
    def search(self, item):                 # 
        return self.get(self.find(item))
    
    def delete(self, item):
        for j in range(self.__nItems):
            if self .__a[j] == item:
                self.__nItems -= 1
                for k in range(j, self.__nItems):
                    self.__a[k] = self.__a[k + 1]
                return True
        return False
    
    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])
        
        
    