print('B.M.I calculater ')



wk=int(input('enter to convert your weight : '))
w=(wk * 0.45 ) 

hi=int(input('enter your  feet : '))
hic=(hi * 12)

inc=int(input('enter your inches : '))

h=(hic + inc)

hit=(h*0.025)



d=(w/(hit*hit))
print('B.M.I  is : ',d)
if d<18.5:
    print('you are underweight')
if d==19:
    print('you are normal ')

if d==20:
    print('you are normal ')
if d==21:
    print('you are normal ')
if d==22:
    print('you are normal ')
if d==23:
    print('you are normal ')
if d==24.9:
    print('you are normal ')
if d>25 :
    print('you are over-weight & keep in dait')
    
input('please press enter to exit')
