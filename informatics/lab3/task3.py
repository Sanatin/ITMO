# ISU 467353
# Вариант: 1

import re


def task3(str):
    glas = ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']
    words = []
    for w in glas:
        temp = glas.copy()
        temp.remove(w)
        other = ''.join(temp)
        words.extend(re.findall(r'\b[^'+ other +r'\W]*' + w + r'[^'+ other + r'\W]*\b', str, flags=re.IGNORECASE))

    return ' '.join(sorted(words, key=lambda w: (len(w), w.lower())))


def test(str, answer):
    result = task3(str)
    print(f'Test: '
          f'string = "{str}"\nAnswer: {answer}\n'
          f'Result: {result}\n'
          f'Right: {answer == result}\n')


test('где же душа? люди все время спешат, вовсе не жаль', 'же не все где жаль')
test('дай джим на счастье лапу мне, такую лапу не видал я сроду', 'я на не дай мне джим')
test('давай с тобой полаем при луне, на тихую бесшумную погоду', 'на при давай тобой')
test('жизнь животные гол полый полость нога ногой', 'гол жизнь ногой полость')
test('а аа оо оао ее ппп пп рн ёёё ё', 'а ё аа ее оо ёёё')