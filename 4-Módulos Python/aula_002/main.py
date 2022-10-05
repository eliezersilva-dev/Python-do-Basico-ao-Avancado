# https://docs.python.org/2/library/datetime.html
# https://docs.python.org/2/library/calendar.html#module-calendar
# https://docs.python.org/2/library/locale.html?highlight=locale#module-locale

from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, 'pt_BR.utf-8')  # para pegar config do dispositivo usar: setlocale(LC_ALL, '')

data = datetime(2022, 10, 4, 22, 58, 17)
print(data)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

data = datetime.strptime('10/04/2022', '%d/%m/%Y')
print(data)

print(data.timestamp())
data = datetime.fromtimestamp(1649559600.0)
print(data)

data1 = datetime.strptime('20/01/1981 20:00:00', '%d/%m/%Y %H:%M:%S')
print(data1)
data1 = data1 + timedelta(days=5)
print(data1.strftime('%d/%m/%Y %H:%M:%S'))

d1 = datetime.strptime('20/01/1981 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/01/1981 20:30:00', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1
print(dif)

print(d1.time())

# Quarta-feira, 04 de outubro de 2022.
dt = datetime.now()
print(dt)
formatacao1 = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao1)
print(formatacao2)

mes_atual = int(dt.strftime('%m'))
print(mes_atual, mdays[mes_atual])
