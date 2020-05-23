alfavit = 'qwertyuiopasdfghjklzxcvbnm'
def schet_capital(q):
    schet = 0 
    for w in q:
        for e in alfavit.upper():
            if w == e:
                schet += 1 
    return schet 

 
def schet_small(q):
    schet = 0 
    for w in q:
        for e in alfavit.lower():
            if w == e:
                schet += 1 
    return schet

proposal = 'Privet Mir, i ect" Grut.'

print(f'Itog big in proposal: {schet_capital(proposal)}')
print(f'Itog malenkie in proposal: {schet_small(proposal)}')



