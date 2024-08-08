def add_everything_up(a, b):
    try:
        print(a + b)

    except TypeError:
        print(str(a) + str(b))

add_everything_up(5, 'ПРИВЕТ')
add_everything_up('Сергей, ', 1963)
add_everything_up(50.125, 24)
add_everything_up(1.987654, 0.1)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))