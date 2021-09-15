import datetime

# dir(datetime)

print(datetime.date.today()) #dia de hoje

print(datetime.date(2020, 7, 7)) #pegar dia específico 

print(datetime.datetime.now()) #pegar horário

date = datetime.date(2020, 7, 7) #pegar variáveis do dia
print(date.day)
print(date.month)
print(date.year)

time = datetime.datetime(2020, 7, 7, 7, 30) #pegar variáveis da hora
print(time.hour)
print(time.minute)
print(time.second)