import numpy as np
# a = np.array([0, 1])
# print(a)
#
# a = np.arange(3)
# print(a)
#
# print(type(a))
# print(a.dtype)
# a = np.arange(3,dtype='int64')
# print(a)
# print(a.dtype)
#
# b = a.astype('float')
# print(b)
# print(b.dtype)
#
# print(b.shape)
# print(b.ndim)
#
# a = np.array([np.arange(2), np.arange(2)])
# print(a)
# print(a.shape)
# print(a.ndim)

# zera = np.zeros((5,5))
# print(zera)
# jedynki = np.ones((4,4))
# print(jedynki)
# print(zera.dtype)
# print(jedynki.dtype)
#
# pusta = np.empty((2,2))
# print(pusta)
# poz_1 = pusta[1,1]
# poz_2 = pusta[0,1]
# print(poz_1)
# print(poz_2)
#
# wlasna = np.array([[1,2], [3,4]])
# print(wlasna)
#
# liczby = np.arange(1, 2, 0.1)
# print(liczby)
#
# przedzial = np.linspace(1, 2, 5) #przedzial = np.linspace(1, 2, 5, endpoint=False)
# print(przedzial)
#
# z = np.indices((5,3))
# print(z)
#
# x, y = np.mgrid[0:5, 0:5]
# print(x)
# print(y)
#
# mat_diag = np.diag([a for a in range(5)], -1)
# print(mat_diag)
#
# z = np.fromiter(range(5), dtype='int32')
# print(z)

# marcin = b'Marcin'
# mar_1 = np.frombuffer(marcin,dtype="S1")
# print(mar_1)
# print("")
# mar_2 = np.frombuffer(marcin,dtype="S2")
# print(mar_2)
# marcin = "Marcin"
# mar_3 = np.array(list(marcin))
# print(mar_3)
# print("")
# mar_4 = np.array(list(marcin), dtype="S1")
# print(mar_4)
# print("")
# mar_5 = np.array(list(b"Marcin"))
# print(mar_5)
# print("")
# mar_6 = np.fromiter(marcin, dtype="S1")
# print(mar_6)
# print("")
# mar_7 = np.fromiter(marcin, dtype="U1")
# print(mar_7)
#
# mat = np.ones((2,2))
# mat_1 = np.ones((2,2))
# mat = mat + mat_1
# print(mat)
# mat = mat - mat_1
# print(mat)
# print(mat * mat_1)
# print(mat / mat_1)
#
# mat2 = np.array([[4,6], [8,10]])
# mat3 = np.array([[2,2], [2, 2]])
#
# print(mat2 * mat3)
# print(mat2 / mat3)

# a = np.arange(10)
# print(a)
#
# s = slice(2, 7, 2)
# print(a[s])
#
# s = range(2, 7, 2)
# print(a[s])
#
# print(a[2:7:2])
#
# print(a[1:])
#
# print(a[2:5])

# mat = np.arange(25)
#
# mat = mat.reshape((5,5))
# print(mat)
# print(mat[1:])
# print(mat[:,1])
# print(mat[:,1:2])
# print(mat[:,-1:])
# print(mat[2:5, 1:3])
# print(mat[:, range(2, 5, 2)])
#
# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# print(x)
#
# rows = np.array([[0, 0], [3, 3]])
# cols = np.array([[0, 2], [0, 2]])
#
# y = x[rows, cols]
# print(y)

#czesc2

# #inicjujemy dane
# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
# print(a)
# print(b)
# #wykonamy działanie odejmowania na tablicach i zapiszemy wynik do nowej zmiennej
# c = a - b
# print(c)
#
# #wykonujemy operacje kwadrat zawartosci danej tablicy
# print(b**2)
#
# #możemye również modyfikować obecne dane z tablicy
# a += b
# print(a)
# a -= b
# print(a)

# a = np.arange(12).reshape(3, 4)
# print(a)
#
# #suma całej macierzy, czyli suma wszystkich elementów z macierzy 3x4
# print(a.sum())
# #suma każdej z kolumn
# print(a.sum(axis=0))
# #minimum każdego z rzędów, inaczej mówiąc wartość min. z każdego wiersza
# print(a.min(axis=1))
# #skumulowana suma dla wierszy
# print(a.cumsum(axis=1))


# a = np.arange(3)
# b = np.arange(3)
# print(a)
# print(b)
# print(a.dot(b))
# print(np.dot(a, b))

# a = np.array([[2, 1, 3], [-1, 2, 4]])
# print(a)
# b = np.array([[1, 3], [2, -2], [-1, 4]])
# print(b)
# print(np.dot(a, b))

# a = np.ones(3, dtype='int32')
# print(a)
# print(a.dtype)
# b = np.linspace(0, np.pi, 3)
# print(b)
# print(b.dtype)
#
# #do zmiennej c zostanie zapisany wynik dodawania macierzy a i b
# c = a + b
# print(c)
# print(c.dtype)
#
# d = np.exp(c*1j)
# print(d)
# print(d.dtype)

# a = np.arange(3)
# print(a)
# print(np.exp(a))
# print(np.sqrt(a))
#
# b = np.array([2., -1., 4.])
# print(np.add(a, b))

# a = np.arange(6).reshape(3, 2)
# print(a)
#
# for b in a.flat:
#     print(b)
#     print("")

#generujemy macierz 1x6
a = np.arange(6)
print(a)
print(a.shape)
print('')
b = a.reshape(2, 3)
print(b)
print(b.shape)
print('')
# c = a.reshape(3, 2)
# print(c)
# print(c.shape)
#
# d = c.ravel()
# print(d)

e = b.T
print(e)