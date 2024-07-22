def calcular_idade_em_anos_meses_dias(dias):
    anos = dias // 365
    dias_restantes = dias % 365
    meses = dias_restantes // 30
    dias_finais = dias_restantes % 30

    print(f'{anos} ano(s)')
    print(f'{meses} mes(es)')
    print(f'{dias_finais} dia(s)')


valor_em_dias = int(input())

calcular_idade_em_anos_meses_dias(valor_em_dias)
