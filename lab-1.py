import csv
import random

flag = 0
search = input('Search for: ')
f = open('result.txt', 'w')

count_row = -1                                                   #счётчик строк в таблице
count_symb = 0                                                   #счётчик книг с названием длинее 30 символов

help_count = 0

max_pop = 0
popularity = []
tags = []

books = []
authors = []
years = []

id_s = []
with open('books.csv', 'r', encoding='cp1251') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in table:

        lower_case = row[3].lower()

        index = lower_case.find(search.lower())

        if index != -1:
            if row[7] != 'Цена поступления':
                if float(row[7][:-3]) >= 200:
                    print(row[1])
            flag = 1

        if len(row[1]) > 30:
            count_symb += 1

        count_row += 1

        if row[8] != 'Кол-во выдач':
            if int(row[8]) > max_pop:
                max_pop = int(row[8])

        check = list(row[12].split('#')[1:])

        for i in check:
            if i not in tags:
                tags.append(i)

        id_s.append(row[0])

    if flag == 0:
        print('Not found')
    f.close()

with open('books.csv', 'r', encoding='cp1251') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    if len(popularity) < 20:
        while max_pop >= 0:
            for row in table:
                if row[8] == str(max_pop):
                    popularity.append(row[1])
            max_pop -= 1

require = []
while len(require) != 20:
    ran = random.randrange(0, count_row)
    if id_s[ran] not in require:
        require.append(id_s[ran])

with open('books.csv', 'r', encoding='cp1251') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in table:
        for i in require:
            if row[0] == i:
                axil = [row[3], row[1], int(row[6][6:11])]
                books.append(axil)
                authors.append(row[3])
                years.append(int(row[6][6:11]))

authors.sort()
#years.sort()

print('Amount of rows in full table:', count_row)
print('Amount of books with name longer that 30 symbols:', count_symb)
print('All tags: ', *tags)
print('The list of most popular books: ')
for i in range(20):
    print(popularity[i])
print(books)
print(authors)
print(years)