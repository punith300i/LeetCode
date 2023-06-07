class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.value_array = []
    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val]=len(self.value_array)
        self.value_array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        remove_index = self.d[val]
        #move top element to the index where item needs to be removed
        self.value_array[remove_index] = self.value_array[-1]
        # pop the top element from the stack
        top_element = self.value_array.pop()
        
        #update the new position of the top element with id of val that needs to be removed
        self.d[top_element] = remove_index
        
        # delete the val element from the dict
        del self.d[val]
        
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.value_array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()