

while True:
    x=input('key in 5 chars or b:')
    if x=='b':
        break
    if len(x)< 5:
        print('more charectars please')
        continue
    else:
        print('long enough')
input('press enter to exit')
