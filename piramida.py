def stroika(q):
    for w in range(q // 2):
        print('*' * (w+1))
    for w in range((q // 2) + 1, 0, -1):
        print('*' * (w))
def my_input():
    return int(input('Введите число'))
def main():
    number = my_input()
    if number % 2 == 0:
        print('Введите нечетное число')
    else:
        stroika(number)

main()