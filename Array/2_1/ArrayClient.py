from Array import Array

def main():
    
    array = Array(10)

    array[0] = 'nosé'
    array[1] = [1, 2, 3]
    array[2] = 75
    array[3] = 54
    array[4] = True
    array[5] = 76
    array[6] = 98
    array[7] = 9.9
    array[8] = 'uwewewe'
    array[9] = 'Dalasreview'

    numero_mayor = array.getMaxNum()
    print('El número más grande del arreglo es : ', numero_mayor)

if __name__ == '__main__':
    main()
