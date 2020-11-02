
input_num = int(input('Enter a positive integer : '))

digits = 0

while input_num != 0:
    input_num = int(input_num / 10)
    digits = digits + 1

print(f'Number of digits:{input_num}')


