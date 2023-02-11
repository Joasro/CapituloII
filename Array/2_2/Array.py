class Array:
    def __init__(self, *args):
        self._array = list(args)

    def deleteMaxNum(self):
        max_num = None
        max_num_index = None
        for index, item in enumerate(self._array):
            if isinstance(item, (int, float)):
                if max_num is None or item > max_num:
                    max_num = item
                    max_num_index = index
        if max_num is not None:
            del self._array[max_num_index]
            return max_num
        return None
