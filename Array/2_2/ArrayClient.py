from Array import Array

def main():
    array1 = Array(1, 2, 3, 4, 5)
    print("Array 1:", array1._array)
    max_num = array1.deleteMaxNum()
    print("El número más grande eliminado es :", max_num)
    print("Array 1:", array1._array)

    array2 = Array(1, 2, 3, "a", 5.0)
    print("Array 2:", array2._array)
    max_num = array2.deleteMaxNum()
    print("El número más grande eliminado es :", max_num)
    print("Array 2:", array2._array)

    array3 = Array("a", 2, "c")
    print("Array 3:", array3._array)
    max_num = array3.deleteMaxNum()
    print("El número más grande eliminado es :", max_num)
    print("Array 3:", array3._array)

if __name__ == "__main__":
    main()