def tagurpidi(järjend):
    if len(järjend) == 0:
        return ''
    else:
        päis = järjend[0]
        saba = järjend[1:]
        elementid_sabas = tagurpidi(saba)
        return elementid_sabas + päis 


print(tagurpidi("stressed"))
