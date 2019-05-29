def rek_abs(array):
    farray = []
    for element in array:
        if isinstance(element, int) == True or isinstance(element, float) == True:
            if element < 0:
                element = abs(element)
            farray.append(element)
        elif isinstance(element, list) == True:
            farray.append(rek_abs(element))
        else:
            farray.append('NaN')
    return farray
print(rek_abs([2,-6, [8,-12,-12, [4, [-6], -3]], 7, [3.55, -3.55]]))
