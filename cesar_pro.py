# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными.
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


text = input()
li = text.split()
res = ''

count = 0
count_str = ''
for i in li:
    for j in i:
        if j.isalpha():
            count += 1
    count_str += str(count)
    count = 0
for i in range(len(li)):
    test = close_cesar_en(li[i], int(count_str[i]))
    res += test + ' '
print(res)