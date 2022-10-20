from datetime import date
hj = date.today()
sexo = int(input('\n[1] seu sexo for femenino\n[2] seu sexo fo masculino\n digite seu sexo: '))
if sexo == 1:
    print('como voce é do sexo femenino voce nao precisa se alistar')
else:
    n = int(input('digite ano de nascimento:'))
    if hj.year - n > 18:
        print('voce qua nasceu em {} voce esta {} anos e esta atrasado\nvoce deverie ter se alistado em {}'.format(n, hj.year - n, n +18))
    elif hj.year - n < 18:
        print('voce nasceu em {} e tem {} anos\nvoce so podera se alistar em {}'.format(n, hj.year - n , n + 18))
    elif hj.year - n == 18:
        print('parabens voce completa 18 anos ete ano \npode se alistar:')