def partition(matriz, nb, na):

    # choose the rightmost element as pivot
    pivot = matriz [na]

    # pointer for greater element
    i = nb - 1
    for j in range(nb, na):
        if matriz [j] <= pivot:
            i = i + 1
            (matriz[i], matriz[j]) = (matriz[j], matriz[i])

    (matriz[i + 1], matriz[na]) = (matriz[na], matriz[i + 1])
    return i + 1


def quickSort(matriz, nb, na):
    if nb < na:
        pi = partition(matriz, nb, na)
        quickSort(matriz, nb, pi - 1)
        quickSort(matriz, pi + 1, na)


data = [[20,23,25,27],[10,11,12,13],[2,3,4,5]]
print("MATRIZ")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('MATRIZ ORDENADA:')
print(data)