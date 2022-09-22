s = 'HANGMAN'
li = []
for i in range(len(s)):
    li.append('X')
user_input = input("Enter the letter or write full word: ")
if s == "".join(li) or s == user_input:
    print(s)
    print('Congratulations. You win!!!')

while True:
    if (len(user_input) != 1 or len(user_input) > len(s)) and user_input != '':
        user_input = input("Incorrect input. Enter the letter or write full word: ")
    if user_input in s:
        if s.count(user_input) == 1:
            li[s.find(user_input)] = user_input
        else:
            input_count = [i for i in range(len(s)) if s[i] == user_input]
            for i in range(len(input_count)):
                li[input_count[i]] = user_input
        if s == "".join(li) or s == user_input:
            print(s)
            print('Congratulations. You win!!!')
            break
        print(''.join(li))
        user_input = input("Excellent, continue. Enter the letter or write full word: ")
    else:
        user_input = input("Try again. Enter the letter or write full word: ")


