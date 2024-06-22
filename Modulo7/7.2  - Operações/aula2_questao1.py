def imprimir_data_por_extenso():
    data = input('Digite uma data de nascimento (dd/mm/aaaa): ')
    dia, mes, ano = data.split("/")
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    mes_por_extenso = meses[int(mes) - 1]
    print('Você nasceu em {} de {} de {}.'.format(dia, mes_por_extenso, ano))

imprimir_data_por_extenso()
