def range(start, stop):
    current = start
    while current < stop:
        yield current
        current +=1
g = range(0, 3)
for e in g:
    print(e)
