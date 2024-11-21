import time

import Task0.task0 as task0
import Task1.task1 as task1
import Task2.task2 as task2
import Task3.task3 as task3

print('Время основного задания:')
start = time.time()
for i in range(100):
   task0.xml_to_yaml('../schedule.xml', '../Task0/schedule.yaml')
end = time.time() - start
print(end)

print('Время доп задания 1:')
start = time.time()
for i in range(100):
   task1.xml_to_yaml('../schedule.xml', '../Task1/schedule.yaml')
end = time.time() - start
print(end)

print('Время доп задания 2:')
start = time.time()
for i in range(100):
   task2.xml_to_yaml('../schedule.xml', '../Task2/schedule.yaml')
end = time.time() - start
print(end)

print('Время доп задания 3:')
start = time.time()
for i in range(100):
   task3.xml_to_yaml('../schedule.xml', '../Task3/schedule.yaml')
end = time.time() - start
print(end)
