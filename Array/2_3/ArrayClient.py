from Array import Array

def sortArray(arr):
  """Ordenados de forma númerica"""
  sorted_array = Array(arr.size())
  for i in range(arr.size()):
    max_num = arr.getMaxNum()
    sorted_array.append(max_num)
    arr.deleteMaxNum()
  return sorted_array

array = Array(5)
array.append(1)
array.append(3)
array.append(2)
array.append(5)
array.append(4)

sorted_array = sortArray(array)
print("Arreglo ordenado: ", end="")
for i in range(sorted_array.size()):
  print(sorted_array.get(i), end=" ")

