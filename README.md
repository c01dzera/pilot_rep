# Курсовая работа "Структура и алгоритмы обработки данных"

#Требования:
#1. Полная объектная реализация с определением классов для всех элементов реализуемой структуры: 
#информационные объекты (обязательно!), объекты-элементы списка (динамическая реализация), объекты-списки,объект-контейнер
#2. Имена классов, свойств и методов должны носить содержательный смысл и соответствовать информационной задаче
#3. Соблюдение принципа инкапсуляции – использование в классах только закрытых свойств и реализация необходимого набора методов доступа
#4. Реализация в классах всех необходимых методов: конструкторы, методы доступа к свойствам, методы добавления и удаления на каждом из двух уровней, метод поиска (при необходимости)
#5. Возможность сохранения всей структуры во внешнем файле с обратной загрузкой
#6. Наличие модуля, демонстрирующего все возможности созданной библиотеки классов и обладающего удобным оконным пользовательским интерфейсом

#Варианты реализации контейнера:
#5. Объектная реализация контейнера на основе комбинированной структуры «Стек-массив динамических списков»
#Варианты информационного наполнения контейнера
#1.	Задача «Студенческие группы»
#	информационные объекты: студенты (свойства – Фамилия, Возраст)
#	студенты объединяются в рамках объекта Группа (свойство – Номер)
#	группы объединяются в рамках объекта-контейнера Факультет (свойство – НазваниеФакультета)