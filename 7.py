import cmath
R = [22, 3, 9, 0, 111, 4]
R.sort()
print(R)
C = [6+5j, 1+5j, 4+2j, -4+1j, 8-4j]
C.sort(key=lambda x: abs(x))
print(C)
C.sort(key=lambda x: x.real, reverse=True)
print(C)
S = ['abvg', 'bimbimbambam', 'abvgeezh', 'bim', 'bam', 'qwerty']
S.sort(key=len)
print(S)

