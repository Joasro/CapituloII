class Array:
    def __init__(self, arr=[]):
        self.arr = arr

    def removeDupes(self):
        new_list = []
        for item in self.arr:
            if item not in new_list:
                new_list.append(item)
        self.arr = new_list


