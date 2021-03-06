def build_field(n):
    tmp = []
    field = []
    for i in range(n):
        tmp.append('_')
    for j in range(n):
        field.append(tmp[:])
    return field

def set_start_location(f):
    f[0][0] = 'x'
    return f 

def show_field(f):
    for i in f:
        print(' '.join(i))

def move_up(f):
    field_size = range(len(f))
    modified = f[:]
    for i in field_size:
        for j in field_size:
            if f[i][j] == 'x':
                modified[i], modified[i-1], modified[i]
                break

def move_left(f):
    field_size = range(len(f))
    modified = f[:]
    for i in field_size:
        for j in field_size:
            if f[i][j] == 'x':
                modified[i][j] = '_'
                modified[i][j-1] = 'x'
                break
    return modified

def move_right(f):
    field_size = range(len(f))
    modified = f[:]
    for i in field_size:
        for j in field_size:
            if f[i][j] == 'x':
                modified[i][j] = '_'
                if j == len(f) - 1:
                    modified[i][0] = 'x'
                else:
                        modified[i][j+1] = 'x'
                break
    return modified

def move_down(f):
    field_size = range(len(f))
    modified = f[:]
    for i in field_size:
        for j in field_size:
            if f[i][j] == 'x':
                if i == len(f) - 1:
                    modified[0], modified[i-1] = modified[i-1], modified[0]
                else:
                    modified[i], modified[i+1] = modified[i+1], modified[i]
                break
        return modified

def user_input():
    return input('Выберите одно из направлений: up right down left или exit для выхода')

def user_input_fields():
    return int(input('Укажите размер поля:'))

def main():
    game = True
    fields = user_input_fields()
    field = set_start_location(build_field(fields))
    show_field(field)

    while game:
        user_direction = user_input()

        if user_direction == 'up':
            field = move_up(field)
       
       
        if user_direction == 'down':
            field = move_down(field)
        
        
        if user_direction == 'right':
            field = move_right(field)
       
       
        if user_direction == 'left':
            field = move_left(field)
       
       
        if user_direction == 'exit':
            game = False

        if game:
            show_field(field)
main()