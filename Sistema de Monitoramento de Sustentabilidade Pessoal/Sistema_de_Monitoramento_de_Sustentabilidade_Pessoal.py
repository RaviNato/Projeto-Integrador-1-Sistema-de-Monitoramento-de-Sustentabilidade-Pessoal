print("################        PROGRAMA DE MONITORAMENTO DE SUSTENTABILIDADE PESSOAL     #######################")

nome = input("Qual seu nome? ")
data = input(f"Olá, {nome}, qual a data do dia referente (00/00/0000)? ")

digitoBem = False
while not digitoBem:
    try:
        litros = float(input("Quantos litros de água você consumiu hoje (Aprox. em litros)? "))
        kwh = float(input("Quantos kWh de energia elétrica você consumiu hoje? "))
        kg = float(input("Quantos kg de resíduos não recicláveis você gerou hoje? "))
        porcentagem = float(input("Qual a porcentagem de resíduos reciclados no total? "))
        print(
        " [1] Transporte público (ônibus, metrô, trem)\n",\
        "[2] Bicicleta\n",\
        "[3] Caminhada\n",\
        "[4] Carro (combustível fósseis)\n",\
        "[5] Carro elétrico\n",\
        "[6] Carona compartilhada")
        transporte = float(input("Qual o meio de transporte você usou hoje? "))
    except ValueError:
        print(f"{nome}, o valor deverá ser um número!")
    else:
        if litros < 0 or kwh < 0 or kg < 0 or porcentagem < 0:
            print(f"{nome}, o valor deverá ser um valor positivo!")
        elif transporte > 6 or transporte < 1:
            print(f"{nome}, não há correspondência para esse transporte!")
        else:
            digitoBem = True



    












print("################                         PROGRAMA ENCERRADO                      #######################")