def eemalda_sõned(array):
    farray = []
    for element in array:
        if isinstance(element, list) == False:
            farray.append('')
        elif isinstance(element, list) == True:
            farray.append(eemalda_sõned(element))
    return farray
print(eemalda_sõned(['a','b',['c']]))
