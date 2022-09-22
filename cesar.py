# Разделение функции на шифрование и дешифорование
# Шифрование:
#   - Определение функции
#   - Определение текста
#   - Определение количество шагов вперед
#   - Если строчные буквы, то использовать алфавит строных букв
#   - Если прописные буквы, то использовать алфавит прописных букв.
#   - Все что в тексте не является буквой добавлять сразу в результат не проверяю.
# rus_lower_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# rus_upper_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
def close_cesar_en(text, step):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    res = ''
    for i in text:
        if i.isalpha():
            if i == i.lower():
                for j in range(len(eng_lower_alphabet)):
                    if i == eng_lower_alphabet[j]:
                        if j + step > len(eng_lower_alphabet) - 1:
                            step_ex = step - (len(eng_lower_alphabet) - (j + 1))
                            res += eng_lower_alphabet[step_ex - 1]
                        else:
                            res += eng_lower_alphabet[j + step]
            elif i == i.upper():
                for j in range(len(eng_upper_alphabet)):
                    if i == eng_upper_alphabet[j]:
                        if j + step > len(eng_upper_alphabet) - 1:
                            step_ex = step - (len(eng_upper_alphabet) - (j + 1))
                            res += eng_upper_alphabet[step_ex - 1]
                        else:
                            res += eng_upper_alphabet[j + step]
        else:
            res += i
    return res

def open_cesar_en(text, step):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    for i in text:
        if i.isalpha():
            if i == i.lower():
                for j in range(len(eng_lower_alphabet)):
                    if i == eng_lower_alphabet[j]:
                        if j - step < 0:
                            step_ex = step - j
                            res += eng_lower_alphabet[len(eng_lower_alphabet) - step_ex]
                        else:
                            res += eng_lower_alphabet[j - step]
            elif i == i.upper():
                for j in range(len(eng_upper_alphabet)):
                    if i == eng_upper_alphabet[j]:
                        if j - step < 0:
                            step_ex = step - j
                            res += eng_upper_alphabet[len(eng_upper_alphabet) - step_ex]
                        else:
                            res += eng_upper_alphabet[j - step]
        else:
            res += i
    return res

def close_cesar_ru(text, step):
    rus_lower_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    rus_upper_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    res = ''
    for i in text:
        if i.isalpha():
            if i == i.lower():
                for j in range(len(rus_lower_alphabet)):
                    if i == rus_lower_alphabet[j]:
                        if j + step > len(rus_lower_alphabet) - 1:
                            step_ex = step - (len(rus_lower_alphabet) - (j + 1))
                            res += rus_lower_alphabet[step_ex - 1]
                        else:
                            res += rus_lower_alphabet[j + step]
            elif i == i.upper():
                for j in range(len(rus_upper_alphabet)):
                    if i == rus_upper_alphabet[j]:
                        if j + step > len(rus_upper_alphabet) - 1:
                            step_ex = step - (len(rus_upper_alphabet) - (j + 1))
                            res += rus_upper_alphabet[step_ex - 1]
                        else:
                            res += rus_upper_alphabet[j + step]
        else:
            res += i
    return res

def open_cesar_ru(text, step):
    rus_lower_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    rus_upper_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    res = ''
    for i in text:
        if i.isalpha():
            if i == i.lower():
                for j in range(len(rus_lower_alphabet)):
                    if i == rus_lower_alphabet[j]:
                        if j - step < 0:
                            step_ex = step - j
                            res += rus_lower_alphabet[len(rus_lower_alphabet) - step_ex]
                        else:
                            res += rus_lower_alphabet[j - step]
            elif i == i.upper():
                for j in range(len(rus_upper_alphabet)):
                    if i == rus_upper_alphabet[j]:
                        if j - step < 0:
                            step_ex = step - j
                            res += rus_upper_alphabet[len(rus_upper_alphabet) - step_ex]
                        else:
                            res += rus_upper_alphabet[j - step]
        else:
            res += i
    return res


cesar = input('Do you want to open or close cesar code: ')
lang = input('Select language: ')
while True:
    if cesar == 'open' or cesar == 'close':
        break
    cesar = input('Incorrect input, try again. Do you want to open or close cesar code: ')
while True:
    if lang == "en" or lang == "ru":
        break
    lang = input('Incorrect input, try again.Select language "en" or "ru": ')

text = input('Enter your text: ')
step = int(input("Select count of step: "))
if cesar == 'open':
    if lang == 'en':
        print(open_cesar_en(text, step))
    else:
        print(open_cesar_ru(text, step))
elif cesar == 'close':
    if lang == 'en':
        print(close_cesar_en(text, step))
    else:
        print(close_cesar_ru(text, step))
