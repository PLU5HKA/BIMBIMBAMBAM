import cmath
R = [22, 3, 9, 0, 111, 4]
C = [6+5j, 1+5j, 4+2j, -4+1j, 8-4j]
S = ['abvg', 'bimbimbambam', 'abvgeezh', 'bim', 'bam', 'qwerty']
A = [[1, 2, 3], [1, 2], [1, 2, 3, 4, 5], [1, 2, 3, 4]]
print(f'{R}\n{C}\n{S}\n{A} ')
R.sort()
print('Сортировка по возрастанию',R)
C.sort(key=lambda x: abs(x))
print('массив комплексных чисел по модулю',C)
C.sort(key=lambda x: x.real, reverse=True)
print('массив комплексных чисел по убыванию действительной части',C)
S.sort(key=len)
print('список строк по длине',S)
print('кортеж строк в лексикографическом порядке',tuple(sorted(S)))
print('кортеж списков по возрастанию длины',tuple(sorted(A, key=len)))
