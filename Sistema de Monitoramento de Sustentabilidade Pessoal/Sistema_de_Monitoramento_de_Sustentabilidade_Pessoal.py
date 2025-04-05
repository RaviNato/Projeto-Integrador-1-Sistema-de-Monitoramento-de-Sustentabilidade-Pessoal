print("################        PROGRAMA DE MONITORAMENTO DE SUSTENTABILIDADE PESSOAL     #######################")

# Entradas
nomeBom = True
while nomeBom:
    nome = input("Qual seu nome? ")
    if nome.strip() == "":  # Verifica se o nome está vazio ou contém apenas espaços
        print("O nome não poderá ser vazio! Tente novamente.")
    elif any(char.isdigit() for char in nome):  # Verifica se algum caractere é número
        print("O nome não poderá conter números! Tente novamente.")
    elif not all(char.isalpha() or char.isspace() for char in nome):  # Verifica se o nome contém caracteres especiais
        print("O nome não poderá conter caracteres especiais! Tente novamente.")
    else:
        nomeBom = False
print()

datavalida = True
while datavalida:
    try: # Tentando obter um número inteiro
        dia = int(input(f"Olá, {nome}, digite o dia do monitoramento: "))
    except ValueError:
        print("O dia deverá ser um valor inteiro!")
    else:
        if dia < 1 or dia > 31:
            print("Não há esse dia!")
        else:
            try: # Tentando obter um número inteiro
                mes = int(input("Agora o digite o mes: "))
            except ValueError:
                print("O mês deverá ser um valor inteiro! Tente novamente.")
            else:
                if mes < 1 or mes > 12: # Mês invalido
                    print("Não há esse mês! Tente novamente.")
                elif dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11): # Dia maior que 30 em meses de 30 dias
                    print("Valor de dia e de mês incompatíveis um com o outro! Tente novamente.")
                elif dia > 29 and mes == 2:
                    print("Valor de dia e de mês incompatíveis um com o outro! Tente novamente.")
                else:
                    try: # Tentando obter um número inteiro
                        ano = int(input("E por fim, digite o ano: "))
                    except ValueError:
                        print("O ano deve ser um valor inteiro! Tente novamente.")
                    else:
                        if ano < 1950:
                            print("Este programa não valida datas com anos anteriores a 1950! Tente novamente.")
                        elif ano > 2025:
                            print("Este programa não valida datas com anos superiores a 2025! Tente novamente.")
                        elif ano%400 == 0 or (ano%4 == 0 and ano%100 != 0): # Ano bissexto
                            print("Data válida!")
                            datavalida = False
                        elif dia > 28 and mes == 2: # Fevereio não pode ser mais de 28
                            print("Valor de dia, mês e ano incompatíveis um com o outro! Tente novamente.")
                        else:
                            print("Data válida!")
                            datavalida = False

print()

digitoBem = True
litrosBem = True
kwhBem = True
kgBem = True
porcentagemBem = True
transporteBem = True

while digitoBem:
    while litrosBem:
        try: # tentando obter um número inteiro em todas as entradas
            litros = float(input("Quantos litros de água você consumiu hoje? (Aprox. em litros): "))
        except ValueError:
            print(f"{nome}, os valores deverão ser um número! Tente novamente.")
        else:
            if litros < 0:
                print(f"{nome}, o valor deverá ser um valor positivo! Tente novamente.")
            else:
                litrosBem = False

    while kwhBem:
        try:
            kwh = float(input("Quantos kWh de energia elétrica você consumiu hoje?: "))
        except ValueError:
            print(f"{nome}, os valor deverá ser um número! Tente novamente.")
        else:
            if kwh < 0:
                print(f"{nome}, o valor deverá ser um valor positivo! Tente novamente.")
            else:
                kwhBem = False

    while kgBem:
        try:
            kg = float(input("Quantos kg de resíduos não recicláveis você gerou hoje?: "))
        except ValueError:
            print(f"{nome}, os valor deverá ser um número! Tente novamente.")
        else:
            if kg < 0:
                print(f"{nome}, o valor deverá ser um valor positivo! Tente novamente.")
            else:
                kgBem = False

    while porcentagemBem:
        try:
            porcentagem = float((input("Qual a porcentagem de resíduos reciclados no total (em %)?: ")).replace("%", "").strip())
        except ValueError:
            print(f"{nome}, os valor deverá ser um número! Tente novamente.")
        else:
            if porcentagem < 0:
                print(f"{nome}, o valor deverá ser um valor positivo! Tente novamente.")
            elif porcentagem < 0:
                print(f"{nome}, o valor deverá ser um valor positivo! Tente novamente.")
            elif porcentagem > 100:
                print(f"{nome}, a porcentagem de resíduos reciclados não deve ultrapassar 100%! Tente novamente.")
            else:
                porcentagemBem = False

    while transporteBem:
        try:
            print(
            " [1] Transporte público (ônibus, metrô, trem)\n",\
            "[2] Bicicleta\n",\
            "[3] Caminhada\n",\
            "[4] Carro (combustível fósseis)\n",\
            "[5] Carro elétrico\n",\
            "[6] Carona compartilhada")
            transporte = int(input("Qual o meio de transporte você usou hoje?: "))
        except ValueError:
            print(f"{nome}, o valor deverá ser um número! Tente novamente.")
        else:
            if transporte > 6 or transporte < 1:
                print(f"{nome}, não há correspondência para esse transporte! Tente novamente.")
            else:
                transporteBem = False
                digitoBem = False


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