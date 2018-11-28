def list_sort(lista):

    even = []
    odd = []
    characters = []
    mydict = dict()

    for i in lista:

        if isinstance(i, int):
            if i % 2 == 0:
                even.append(i)

            else:
                odd.append(i)

        elif isinstance(i, str):
            characters.append(i)

    mydict['evens'] = sorted(even)
    mydict['odds'] = sorted(odd)
    mydict['chars'] = sorted(characters)
    return mydict


print(list_sort([1, 2, 3, 4, 5, 'a', 'b']))