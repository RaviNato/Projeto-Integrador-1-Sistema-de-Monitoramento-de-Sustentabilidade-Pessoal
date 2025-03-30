print("################        PROGRAMA DE MONITORAMENTO DE SUSTENTABILIDADE PESSOAL     #######################")


nome = input("Qual seu nome? ")
data = input(f"Olá, {nome}, qual a data do dia referente (00-00-0000)? ")

digitoBem = False
while not digitoBem:
    try:
        litros = float(input("Quantos litros de água você consumiu hoje (Aprox. em litros)? "))
        kwh = float(input("Quantos kWh de energia elétrica você consumiu hoje? "))
        kg = float(input("Quantos kg de resíduos não recicláveis você gerou hoje? "))
        porcentagem = float((input("Qual a porcentagem de resíduos reciclados no total? ")).replace("%", "").strip())
        print(
        " [1] Transporte público (ônibus, metrô, trem)\n",\
        "[2] Bicicleta\n",\
        "[3] Caminhada\n",\
        "[4] Carro (combustível fósseis)\n",\
        "[5] Carro elétrico\n",\
        "[6] Carona compartilhada")
        transporte = int(input("Qual o meio de transporte você usou hoje? "))
    except ValueError:
        print(f"{nome}, o valor deverá ser um número! Tente novamente.")
    else:
        if litros < 0 or kwh < 0 or kg < 0 or porcentagem < 0:
            print(f"{nome}, o valor deverá ser um valor positivo! Tente novamente.")
        elif porcentagem > 100:
            print(f"{nome}, a porcentagem de resíduos reciclados não deve ultrapassar 100%! Tente novamente.")
        elif transporte > 6 or transporte < 1:
            print(f"{nome}, não há correspondência para esse transporte! Tente novamente.")
        else:
            digitoBem = True




consumAgua = None
if litros < 150:
    consumAgua = "Alta Sustentabilidade"
elif litros > 151 and litros < 201:
    consumAgua = "Moderada Sustentabilidade"
else:
    consumAgua = "Baixa Sustentabilidade"

consumEnergia = None
if kwh < 5:
    consumEnergia = "Alta Sustentabilidade"
elif kwh > 4 and kwh < 11:
    consumEnergia = "Moderada Sustentabilidade"
else:
    consumEnergia = "Baixa Sustentabilidade"


consumLixo = None
if porcentagem > 50:
    consumLixo = "Alta Sustentabilidade"
elif porcentagem > 19 and porcentagem < 51:
    consumLixo = "Moderada Sustentabilidade"
else:
    consumLixo = "Baixa Sustentabilidade"

consumTransporte = None
if transporte == 1 or transporte == 2 or transporte == 3 or transporte == 5:
    consumTransporte = "Alta Sustentabilidade"
elif transporte == 4:
    consumTransporte = "Baixa Sustentabilidade"
else:
    consumTransporte = "Moderada Sustentabilidade"






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