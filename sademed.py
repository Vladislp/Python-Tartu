def count():
    _max = {'name': '', 'sal': 0}
    with open("palgad.txt", "r") as f:
        for line in f.readlines():
            our_line = line.strip().split(";")
            if int(our_line[-1]) > _max['sal']:
                _max['sal'] = int(our_line[-1])
                _max['name'] = our_line[0]
    print(_max['name'], _max['sal'])