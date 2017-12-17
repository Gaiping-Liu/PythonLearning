#!/usr/bin/env pathon3
# _*_ coding: utf-8 _*_

def MergeTwoSortedList(lista, listb):
    if not isinstance(lista, list):
        raise TypeError("%s is not list", lista)
    if not isinstance(listb, list):
        raise TypeError("%s is not list", listb)
    aindex = 0

    for bindex in range(len(listb)):
        while aindex < len(lista):
            if (listb[bindex] < lista[aindex]):
                lista.insert(aindex, listb[bindex])
                break
            aindex = aindex + 1
        if (aindex == len(lista)):
            lista.extend(listb[bindex::])  # why return this is none?
            return lista
    return lista


lista = [0, 0, 3, 4, 5, 6]
listb = [2, 4, 5, 7, 8]
print(MergeTwoSortedList(lista, listb))  # This has changed lista
listc = MergeTwoSortedList(lista, listb)
print(listc)
