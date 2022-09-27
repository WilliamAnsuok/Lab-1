import csv
import random

flag = 0
search = input('Search for: ')

count_row = -1                                                   #счётчик строк в таблице
count_symb = 0                                                   #счётчик книг с названием длинее 30 символов

max_pop = 0 #счетчик максимальной популярности
popularity = [] #массив, в котором содержаться самые популярные книги
tags = [] #список уникальных тегов

id_s = [] #айди всех книг
with open('books.csv', 'r', encoding='cp1251') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in table:

        count_row += 1              #подсчёт всех записей в таблице исключая шапку

        lower_case = row[3].lower()

        index = lower_case.find(search.lower())

        if index != -1:             #вывод всех книг по запрошенному автору с учётом условий варианта
            if row[7] != 'Цена поступления':
                if '.' in row[7]:
                    if float(row[7][:-3]) >= 200:
                        print(row[1])
                else:
                    if int(row[7]) >= 200:
                        print(row[1])
            flag = 1

        if len(row[1]) > 30:         #подсчёт кол-ва записей с длинной названия более 30 символов
            count_symb += 1

        if row[8] != 'Кол-во выдач':    #определение наибольшего значения выдачи книг
            if int(row[8]) > max_pop:
                max_pop = int(row[8])

        check = list(row[12].split('#')[1:]) #список тегов для каждой книги

        for i in check:                      #список уникальных тегов для всех книг
            if i not in tags:
                tags.append(i)

        id_s.append(row[0])                  #добавление айди книги в общий список

    if flag == 0:
        print('Not found')


with open('books.csv', 'r', encoding='cp1251') as csvfile:  #поиск 20 самых популярных книг
    table = csv.reader(csvfile, delimiter=';')
    if len(popularity) < 20:
        while max_pop >= 0:
            for row in table:
                if row[8] == str(max_pop):
                    popularity.append(row[1])
            max_pop -= 1

require = []                #формирование запроса на 20 рандомных айди книг
while len(require) != 20:
    ran = random.randrange(0, count_row)
    if id_s[ran] not in require:
        require.append(id_s[ran])
require.sort()              #сортировка айди по возрастанию
result = []                 #лист с подготовленными данными для файла result.txt

with open('books.csv', 'r', encoding='cp1251') as csvfile:      #формирование списка из 20 рандомных книг, подготовка к записи их в резалт тхт
    table = csv.reader(csvfile, delimiter=';')
    for row in table:
        for i in require:
            if row[0] == i:
                temp = [row[3], row[1], row[6][6:11]]
                result.append(temp)

print('Amount of rows in full table:', count_row)
print('Amount of books with name longer that 30 symbols:', count_symb)
print('All tags: ', *tags)
print('The list of most popular books: ')
for i in range(20):
    print(popularity[i])

f = open('result.txt', 'w')         #запись 20 рандомных книг в фаул резалт тхт
for i in range(20):
    ax = str(i + 1) + '. ' + result[i][0] + '. ' + result[i][1] + ' - ' + result[i][2] + '\n'
    f.write(ax)
f.close()