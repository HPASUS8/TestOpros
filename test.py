
name = input ('Привет! Как тебя зовут? ')
age = int(input('А сколько тебе лет? '))
year = int(int(input('Напомнишь, какой сейчас год? ')))
hyear = (100 - age) + year
hyear1 = (100 - age) + (year - 1)
hby = year - age
hby1 = year - age - 1
print (f'Привет, {name}! Сейчас тебе {age}, ты родился(ась) в {hby}! Или в {hby1}? В любом случае, в {hyear}/{hyear1} году тебе исполнится 100 лет!')
print (f'А сейчас я скажу твоё имя наоборот:')
print (name[::-1])
print (f'Ну что, я удивил тебя? Надеюсь, да!')
