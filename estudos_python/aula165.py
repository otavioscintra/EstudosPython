# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

data_emprestimo = datetime(2020, 12, 20)
data_final = data_emprestimo + relativedelta(years=5)
delta = relativedelta(data_final, data_emprestimo)
meses = delta.years * 12 + delta.months
valor_parcela = 1_000_000/meses
data_pagamento = data_emprestimo


while data_final > data_pagamento:
    print(data_pagamento.strftime("%d/%m/%Y"), f'R$ {valor_parcela:.2f}')
    data_pagamento += relativedelta(months=1)
