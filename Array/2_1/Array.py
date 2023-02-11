class Array:
    def __init__(self, n):
        self._array = [None] * n

    def __getitem__(self, index):
        return self._array[index]

    def __setitem__(self, index, value):
        self._array[index] = value

    def getMaxNum(self):
        numero_mayor = None
        for item in self._array:
            if isinstance(item, (int, float)):
                if numero_mayor is None or item > numero_mayor:
                    numero_mayor = item
        return  numero_mayor
