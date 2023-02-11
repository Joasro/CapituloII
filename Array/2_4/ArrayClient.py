from Array import Array

def main():
    arr = Array([1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9, 9])
    print("Array antes de eliminar duplicados: ", arr.arr)
    arr.removeDupes()
    print("Array después de eliminar duplicados: ", arr.arr)

if __name__ == "__main__":
    main()