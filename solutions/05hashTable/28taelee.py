
class MyHashMap:

    hashMap = {}
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hashMap[int] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.hashMap:
            return self.hashMap[key]
        else:
            return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.hashMap:
            self.hashMap.pop(key)


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,2)
print(obj)
param_2 = obj.get(1)
print(param_2)
obj.remove(1)
print(obj)
