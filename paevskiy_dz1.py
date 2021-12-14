#1

duration = int(input('Введите время в секундах'))
days = duration // (60 * 60 * 24)
hours = (duration - days * ( 60 * 60 * 24)) // ( 60 * 60 )
minutes = (duration - days * ( 60 * 60 * 24) - hours * ( 60 * 60) // 60
HELP_Here_my_paucharm_for_some_reason_knocks_out_an_error = duration - days * (60 * 60 * 24) - hours * (60 * 60) - minutes * 60
print( days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')


#2

sum = 0
sum_2 = 0
my_list = []
for number in range (1, 1001, 2):
    sum_zero = 0
    sum_zero_2 = 0
    cubed = number ** 3
    my_list.append(cubed)
    cubed_zero = cubed
    while cubed > 0:
        a = cubed % 10
        sum_zero = sum_zero + a
        cubed = cubed // 10
    if sum_zero % 7 == 0:
        sum = sum + cubed_zero
    cubed_2 = number ** 3 + 17
    cubed_zero_2 = cubed_2
    while cubed_2 > 0:
        a2 = cubed_2 % 10
        sum_zero_2 = sum_zero_2 + a2
        cubed_2 = cubed_2 // 10
    if sum_zero_2 % 7 == 0:
        sum_2 = sum_2 + cubed_zero_2
print(sum)
print(sum_2)


#3

percent = int(input('Введите число процента: '))
if percent == 1:
    word = 'процент'
elif percent <= 4:
    word = 'процента'
else:
    word = 'процентов'
print(percent, word)