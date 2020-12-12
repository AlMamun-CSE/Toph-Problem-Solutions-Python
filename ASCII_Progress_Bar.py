input_string_int = int(float(input()))

n = input_string_int // 10

plus_sign = '+' * n
dot_sign = '.' * (10 - n)
percent = input_string_int

print('[{}{}] {}%'.format(plus_sign, dot_sign, percent))
