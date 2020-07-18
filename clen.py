def create_field(n):
    """n - размер поля, return field"""

    field = []
    for _ in range(n):
        field.append(['_']*n)
    
    field[0][0] = 'X'
    return field

def move_player(direction, field):
    """direction - направление движения игрока
    field - поле"""
    length_field = len(field)
    for row in range(length_field):
        for col in range(length_field):
            if field[row][col] == 'X':
                field[row][col] = '_'
                field[row][col+1] = 'X'
                break
    return field

def display_field(f):
    """f - поле"""
    for row in f:
        print(' '.join(row))

field = create_field(5)
display_field(field)

for _ in range(2):
    field = move_player('direction', field)
    display_field(field)

