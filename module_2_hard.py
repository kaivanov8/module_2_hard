# Дополнительное практическое задание
# по модулю "Основные операторы"

#                   СЛИШКОМ ДРЕВНИЙ ШРИФТ
q = True
while q :
    v = int ( input('Введите число из первой вставки (3-20) '))
    if v < 3 or v > 20:
        print('Число должно быть от 3 до 20')
    else:
        q = False
result =[]
for i in range( 1, v):
    for j in range( i+1, v+1):
        if v % (i+j) == 0:
            result.append(i)
            result.append(j)

print (*result)