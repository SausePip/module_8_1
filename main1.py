

def add_everything_up(a, b):
    try:
        if isinstance(a, str) or isinstance(b, str):
            return str(a) + str(b)
        return a + b
    except Exception as e:
        return f"Ошибка: {e}"


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))