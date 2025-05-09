# -*- coding: utf-8 -*-
"""extra.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o00u-2f3gqXUs8XKUCAHeCix7X8984V8
"""

with open("extra.txt", "r") as file:
  lista_desorganizada = [linha.strip() for linha in file.readlines()]

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

lista_organizada = mergeSort(lista_desorganizada)
print("Lista desorganizada: ", lista_desorganizada)
print("Lista organizada: ", lista_organizada)