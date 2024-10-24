# ISU 467353
# Смайлик: ;<)

import re

def task1(str):
    return len(re.findall(r';<\)', str))


def test(str, answer):
    result = task1(str)
    print(f'Test: '
          f'string = "{str}"\nAnswer: {answer}\n'
          f'Result: {result}\n'
          f'Right: {answer == result}\n')


test(";<)331;<\ 1):1)<>'", 1)
test(";<) ;<) ;<);<)", 4)
test("Hello world", 0)
test(";-) ;>) ;<] ;<(", 0)
test("", 0)
