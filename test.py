name = input ('Привет! Как тебя зовут? ')
age = int(input('А сколько тебе лет? '))
year = int(int(input('Напомнишь, какой сейчас год? ')))

one_hundred_year = (100 - age) + year
one_hundred_year_1 = (100 - age) + (year - 1)
happy_bday = year - age
happy_bday_1 = year - age - 1

print(f'Привет, {name}! Сейчас тебе {age}, ты родился(ась) в {hby}! Или в {hby1}? В любом случае, в {hyear}/{hyear1} году тебе исполнится 100 лет!')
print(f'А сейчас я скажу твоё имя наоборот:')
print(name[::-1])
print(f'Ну что, я удивил тебя? Надеюсь, да!')
