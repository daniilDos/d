dr = {'Cristiano Ronaldo': '05/02/1985',
'Leonel Messi': '24/06/1987',
'kilian mbappe': '20/12/1998'}
print('Welcome to the birthday dictionary. We know birdth dates of:')
for name in dr:
    print(name)
print('What birth date you want to know?')
name = input('Enter a name:')
if name in dr:
    print(f'{name} s birhday is {dr[name]}')
else:
    print(f'{name} s такого имени нет словаре')    

