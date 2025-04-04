print("################        PROGRAMA DE MONITORAMENTO DE SUSTENTABILIDADE PESSOAL     #######################")

# Entradas

nome = input("Qual seu nome? ")
print()

datavalida = False
while not datavalida:
    try: # tentando obter um número inteiro
        dia=int(input(f"Olá, {nome}, digite o dia do monitoramento: "))
    except ValueError:
        print("O dia deverá ser um valor inteiro!")
    else:
        if dia<1 or dia>31:
            print("Não há esse dia!")
        else:
            try: # tentando obter um número inteiro
                mes=int(input("Agora o digite o mes: "))
            except ValueError:
                print("O mês deverá ser um valor inteiro! Tente novamente.")
            else:
                if mes<1 or mes>12: # mês invalido
                    print("Não há esse mês! Tente novamente.")
                elif dia>30 and (mes==4 or mes==6 or mes==9 or mes==11): # dia maior que 30 em meses de 30 dias
                    print("Valor de dia e de mês incompatíveis um com o outro! Tente novamente.")
                elif dia>29 and mes==2:
                    print("Valor de dia e de mês incompatíveis um com o outro! Tente novamente.")
                else:
                    try: # tentando obter um número inteiro
                        ano=int(input("E por fim, digite o ano: "))
                    except ValueError:
                        print("O ano deve ser um valor inteiro! Tente novamente.")
                    else:
                        if ano<1950:
                            print("Este programa não valida datas com anos anteriores a 1950! Tente novamente.")
                        elif ano==0: # ano que nunca existiu
                            print("Não existe ano 0!")
                        elif ano%400==0 or (ano%4==0 and ano%100!=0): # ano bissexto
                            print("Data válida!")
                            datavalida = True
                        elif dia>28 and mes==2: # fevereio não pode ser mais de 28
                            print("Valor de dia, mês e ano incompatíveis um com o outro! Tente novamente.")
                        else:
                            print("Data válida!")
                            datavalida = True

print()

digitoBem = False
while not digitoBem:
    try: # tentando obter um número inteiro em todas as entradas
        litros = float(input("Quantos litros de água você consumiu hoje? (Aprox. em litros): "))
        kwh = float(input("Quantos kWh de energia elétrica você consumiu hoje?: "))
        kg = float(input("Quantos kg de resíduos não recicláveis você gerou hoje?: "))
        porcentagem = float((input("Qual a porcentagem de resíduos reciclados no total (em %)?: ")).replace("%", "").strip())
        print(
        " [1] Transporte público (ônibus, metrô, trem)\n",\
        "[2] Bicicleta\n",\
        "[3] Caminhada\n",\
        "[4] Carro (combustível fósseis)\n",\
        "[5] Carro elétrico\n",\
        "[6] Carona compartilhada")
        transporte = int(input("Qual o meio de transporte você usou hoje?: "))
    except ValueError:
        print(f"{nome}, os valores deverão ser um número! Tente novamente.")
    else:
        if litros < 0 or kwh < 0 or kg < 0 or porcentagem < 0:
            print(f"{nome}, o valores deverão ser um valor positivo! Tente novamente.")
        elif porcentagem > 100:
            print(f"{nome}, a porcentagem de resíduos reciclados não deve ultrapassar 100%! Tente novamente.")
        elif transporte > 6 or transporte < 1:
            print(f"{nome}, não há correspondência para esse transporte! Tente novamente.")
        else:
            digitoBem = True


# Processamento

AltaSustentabilidade = "Alta Sustentabilidade"
ModeradaSustentabilidade = "Moderada Sustentabilidade"
BaixaSustentabilidade = "Baixa Sustentabilidade"

consumAgua = None
if litros < 150:
    consumAgua = AltaSustentabilidade
elif litros > 151 and litros < 201:
    consumAgua = ModeradaSustentabilidade
else:
    consumAgua = BaixaSustentabilidade

consumEnergia = None
if kwh < 5:
    consumEnergia = AltaSustentabilidade
elif kwh > 4 and kwh < 11:
    consumEnergia = ModeradaSustentabilidade
else:
    consumEnergia = BaixaSustentabilidade

consumLixo = None
if porcentagem > 50:
    consumLixo = AltaSustentabilidade
elif porcentagem > 19 and porcentagem < 51:
    consumLixo = ModeradaSustentabilidade
else:
    consumLixo = BaixaSustentabilidade

consumTransporte = None
if transporte in [1, 2, 3, 5]:
    consumTransporte = AltaSustentabilidade
elif transporte == 4:
    consumTransporte = BaixaSustentabilidade
else:
    consumTransporte = ModeradaSustentabilidade





# Classificação

print(
    "\n",\
    f"#########      Chegamos ao fim, {nome}. Aqui está o resultado de suas classificações!       #########\n",\
    "\n",\
    f"  Consumo de água:                        {consumAgua}\n",\
    f"  Geração de Resíduos Não Recicláveis:    {consumLixo}\n",\
    f"  Consumo de Energia Elétrica:            {consumEnergia}\n",\
    f"  Uso de Transporte:                      {consumTransporte}\n",\
    "")




print("################                         PROGRAMA ENCERRADO                      #######################")