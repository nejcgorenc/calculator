convert = True
while convert:
    km = float(raw_input('Vnesi kilometre:'))

    p = 1.609

    miles = km * p

    print ('{0} kilometrov je {1} milj') .format(km, miles)

    answer = raw_input(("Vtipkaj 'da' za novo pretvorbo ali 'ne' za konec:"))
    if answer == 'da':
        continue
    elif answer == 'ne':
        convert = False
    else:
        raise ValueError('Go fuck yourself you sick bastard!!!')

