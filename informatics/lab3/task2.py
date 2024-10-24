# ISU 467353
# Вариант 1

# Довольно распространённая ошибка ошибка – это повтор слова. Вот в предыдущем
# предложении такая допущена. Необходимо исправить каждый такой повтор.
# Повтор это – слово, один или несколько пробельных символов, и снова то же слово.

import re


def task2(str):
    words = re.findall(r'\w+', str)
    for word in words:
        str = re.sub(f'\\b{word}\\b(\s+{word}\\b)+', word, str, flags=re.IGNORECASE)

    return str


def test(str, answer):
    result = task2(str)
    print(f'Test: '
          f'string = "{str}"\nAnswer: {answer}\n'
          f'Result: {result}\n'
          f'Right: {answer == result}\n')


test('Lorem lorem ipsum dolor sit   sit amet amet, consectetur adipiscing elitelit elit. unc nunc varius bibendum accumsan.',
     'Lorem ipsum dolor sit amet, consectetur adipiscing elitelit elit. unc nunc varius bibendum accumsan.')

test("Практический опыт опытный показывает, что повышение повышение   повышение уровня гражданского сознания требует от от, нас    нас анализа новых предложений.",
     'Практический опыт опытный показывает, что повышение уровня гражданского сознания требует от, нас анализа новых предложений.')

test("Дорогие друзья, друзья дальнейшее развитие различных форм форм  деятельности обеспечивает широкому кругу кругуспециалистов участие",
     'Дорогие друзья, друзья дальнейшее развитие различных форм  деятельности обеспечивает широкому кругу кругуспециалистов участие')

test("один один два два два привет привет ккк е е е еее", 'один два привет ккк е еее')

test("Hello world Hello world world wor ld", 'Hello world Hello world wor ld')
