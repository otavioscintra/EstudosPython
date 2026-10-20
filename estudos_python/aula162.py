
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
from pytz import timezone

data = datetime.now()
print(data.timestamp())
print(datetime.fromtimestamp(1791994946))
# data_str_data = "2026/10/14 11:46:00"
# data_str_data = "14/10/2026"
# data_str_fmr = "%d/%m/%Y"

data = datetime(2010, 11, 13, 3, 6, 22, tzinfo=timezone("Asia/Tokyo"))
# data = datetime.strptime(data_str_data, data_str_fmr)
