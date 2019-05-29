def mediaan(a):
    a = sorted(a)
    if len(a) % 2 == 1:
        keskmine = a[int((len(a) + 1)/2) - 1]
        return keskmine
    elif len(a) % 2 == 0:
        keskmine1 = sum(a[int(len(a)/2)-1:int(len(a)/2)+1])/2
        return keskmine1
a = [1, 3, 7, 24, 12]

print(mediaan(a))

        