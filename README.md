# Домашнее задание к лекции 4.«Tests»

##Solution:
- made pytests and unittests for each function
- made input mocking and data mocking
- all functions are clean and doesn't use global variables 

### Задача №1 unit-tests
Из курса «Python: программирование на каждый день и сверхбыстрое прототипирование» необходимо протестировать программу по работе с бухгалтерией [Лекции 2.1](https://github.com/netology-code/py-homework-basic/tree/master/2.1.functions).
При наличии своего решения данной задачи можно использовать его или использовать предложенный код в директории scr текущего задания.

* Следует протестировать основные функции по получению информации о документах, добавлении и удалении элементов из словаря.
  
Рекомендации по тестам.
1. Если у вас в функциях информация выводилась(print), то теперь её лучше возвращать(return) чтобы можно было протестировать.
2. input можно "замокать" с помощью ```unittest.mock.patch```, если с этим будут проблемы, то лучше переписать функции так, чтобы данные приходили через параметры.
