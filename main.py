m_arr = []

number = int(input('Введите количество элементов массива: '))

for i in range (number):
  element = int(input('Введите число: '))
  m_arr.append(element)

m_arr_part_k = []
m_arr_part_p = []

N = len(m_arr)
M = int(input('Введите длину M: '))
begin_first = int(input('Введите начало 1: '))
begin_two = int(input('Введите начало 2: '))

if begin_first < begin_two:
  K, P = begin_first, begin_two
else:
  K, P = begin_two, begin_first

for i in range (M):
  m_arr_part_k.append(m_arr[K - 1 + i])
  m_arr_part_p.append(m_arr[P + i - 1])

print('Исходный массив:', m_arr)

for i in range (M):
  m_arr.remove(m_arr_part_k[i])
  m_arr.remove(m_arr_part_p[i])
  m_arr.insert(K - 1 + i, m_arr_part_p[i])
  m_arr.insert(P - 1 + i, m_arr_part_k[i])

print('Новый массив:', m_arr)
