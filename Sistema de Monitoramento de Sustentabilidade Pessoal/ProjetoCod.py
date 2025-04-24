# Fazendo a conexao com o MySQL
import mysql.connector

# Conectando com o baco de dados
conexao = mysql.connector.connect(
    host="localhost", # Deve ser preenchido com o hostname da conexao MySQL onde esta o banco de dados
    user="root", # Deve ser preenchido com o username da conexao MySQL onde esta o banco de dados
    password="12345", # Deve ser preenchido com o username da conexao MySQL onde esta o banco de dados
    database="projeto" # Deve ser preenchido com o nome do banco de dados
    )

cursor = conexao.cursor()


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


# entrada das informaçoes no banco de dados

transporte_banco = None
if transporte == 1:
    transporte_banco = "Transporte público (ônibus, metrô, trem)"
elif transporte == 2:
    transporte_banco = "Bicicleta"
elif transporte == 3:
    transporte_banco = "Caminhada"
elif transporte == 4:
    transporte_banco = "Carro (combustível fósseis)"
elif transporte == 5:
    transporte_banco = "Carro elétrico"
else:
    transporte_banco = "Carona compartilhada"


comando = ("INSERT INTO sustentabilidade"
           "(nome, data_checagem, agua_litros, energia_KWh, residuos_nao_resiclaveis_Kg, residuos_reciclados, transporte)"
           "VALUES"
           f"('{nome}', '{ano}.{mes}.{dia}', '{litros}', '{kwh}', '{kg}', '{porcentagem}', '{transporte_banco}') ")
cursor.execute(comando)
conexao.commit()


# Menu para acessar o banco de dados

bancodado = True
while bancodado:
    menubd = True
    while menubd:
        try:
            print(
                "O que você deseja fazer?\n",\
                "[1]Ver checagem anteriores.\n",\
                "[2]Alterar uma checagem anterior.\n",\
                "[3]Deletar uma checagem anterior.\n",\
                "[4]Encerrar programa.")
            menu_resposta=int(input(""))
        except ValueError:
            print(f"{nome}, o valor deverá ser um número! Tente novamente.")
        else:
            if menu_resposta > 4 or menu_resposta < 1:
                print(f"{nome}, não há correspondência para essa opção! Tente novamente.")
            else:
                menubd = False

    if menu_resposta == 1:
        # Código para exiber a informações do banco de dados
        comando = f"SELECT * FROM sustentabilidade;"
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for linha in resultado:
            print("CODIGO: ", linha[0])
            print("NOME: ", linha[1])
            print("DATA: ", linha[2])
            print("ÁGUA(LITROS): ", linha[3])
            print("ENERGIA(KWh): ", linha[4])
            print("RESÍDUOS NÃO RECICLÁVEIS(Kg): ", linha[5])
            print("RESÍDUOS RECICLADOS(%): ", linha[6])
            print("TRANSPORTE: ", linha[7], "\n")

    if menu_resposta == 2:
        # Menu para escolher o que deseja mudar no banco de dados
        cod_alt = int(input("Digite o codigo da checagem que você desaja Alterar: "))
        bd_alt = True
        while bd_alt:
            menu_alt = True
            while menu_alt:
                try:
                    print(
                        "O que você deseja alterar?\n",\
                        "[1]NOME.\n",\
                        "[2]DATA.\n",\
                        "[3]ÁGUA(LITROS).\n",\
                        "[4]ENERGIA(KWh).\n",\
                        "[5]RESÍDUOS NÃO RECICLÁVEIS(Kg).\n",\
                        "[6]RESÍDUOS RECICLADOS(%).\n",\
                        "[7]TRANSPORTE).\n")
                    menu_resposta_alt=int(input(""))
                except ValueError:
                    print(f"{nome}, o valor deverá ser um número! Tente novamente.")
                else:
                    if menu_resposta_alt > 7 or menu_resposta < 1:
                        print(f"{nome}, não há correspondência para essa opção! Tente novamente.")
                    else:
                        
                        menu_alt = False

            
            if menu_resposta_alt == 1:
                nomeBomAlt = True
                while nomeBomAlt:
                    nomeAlt = input("Digite o novo nome? ")
                    if nomeAlt.strip() == "":
                        print("O nome não poderá ser vazio! Tente novamente.")
                    elif any(char.isdigit() for char in nomeAlt):
                        print("O nome não poderá conter números! Tente novamente.")
                    elif not all(char.isalpha() or char.isspace() for char in nomeAlt):
                        print("O nome não poderá conter caracteres especiais! Tente novamente.")
                    else:
                        nomeBomAlt = False

                #Codigo para alterar a informação do banco de dados
                comando = f"UPDATE sustentabilidade SET nome = '{nomeAlt}' WHERE codigo = '{cod_alt}';"
                cursor.execute(comando)
                conexao.commit()
                bd_alt = False

            elif menu_resposta_alt == 2:
                datavalida = True
                while datavalida:
                    try: 
                        dia = int(input(f"Digite o novo dia: "))
                    except ValueError:
                        print("O dia deverá ser um valor inteiro!")
                    else:
                        if dia < 1 or dia > 31:
                            print("Não há esse dia!")
                        else:
                            try:
                                mes = int(input("Agora o digite o mes: "))
                            except ValueError:
                                print("O mês deverá ser um valor inteiro! Tente novamente.")
                            else:
                                if mes < 1 or mes > 12:
                                    print("Não há esse mês! Tente novamente.")
                                elif dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
                                    print("Valor de dia e de mês incompatíveis um com o outro! Tente novamente.")
                                elif dia > 29 and mes == 2:
                                    print("Valor de dia e de mês incompatíveis um com o outro! Tente novamente.")
                                else:
                                    try:
                                        ano = int(input("E por fim, digite o ano: "))
                                    except ValueError:
                                        print("O ano deve ser um valor inteiro! Tente novamente.")
                                    else:
                                        if ano < 1950:
                                            print("Este programa não valida datas com anos anteriores a 1950! Tente novamente.")
                                        elif ano > 2025:
                                            print("Este programa não valida datas com anos superiores a 2025! Tente novamente.")
                                        elif ano%400 == 0 or (ano%4 == 0 and ano%100 != 0):
                                            print("Data válida!")
                                            datavalida = False
                                        elif dia > 28 and mes == 2:
                                            print("Valor de dia, mês e ano incompatíveis um com o outro! Tente novamente.")
                                        else:
                                            print("Data válida!")
                                            print();
                                            datavalida = False

                comando = f"UPDATE sustentabilidade SET data_checagem = '{ano}.{mes}.{dia}' WHERE codigo = '{cod_alt}';"
                cursor.execute(comando)
                conexao.commit()
                bd_alt = False

            elif menu_resposta_alt >= 3 and menu_resposta_alt <= 5:
                if menu_resposta_alt == 3:
                    coluna = "agua_litros"
                elif menu_resposta_alt == 4:
                    coluna = "energia_KWh"
                else:
                    coluna = "residuos_nao_resiclaveis_Kg"
                alt_aer = True
                while alt_aer:
                    try:
                        valor = float(input("Digite o novo valor: "))
                    except ValueError:
                        print(f"{nome}, os valores deverão ser um número! Tente novamente.")
                    else:
                        if valor < 0:
                            print(f"{nome}, o valor deverá ser um valor positivo! Tente novamente.")
                        else:
                            alt_aer = False

                
                comando = f"UPDATE sustentabilidade SET {coluna} = '{valor}' WHERE codigo = '{cod_alt}';"
                cursor.execute(comando)
                conexao.commit()
                bd_alt = False

            elif menu_resposta_alt == 6:
                alt_por = True
                while alt_por:
                    try:
                        porcentagem = float((input("Digite a nova porcentagem?: ")).replace("%", "").strip())
                    except ValueError:
                        print("Os valor deverá ser um número! Tente novamente.")
                    else:
                        if porcentagem < 0:
                            print("O valor deverá ser um valor positivo! Tente novamente.")
                        elif porcentagem < 0:
                            print("O valor deverá ser um valor positivo! Tente novamente.")
                        elif porcentagem > 100:
                            print("A porcentagem de resíduos reciclados não deve ultrapassar 100%! Tente novamente.")
                        else:
                            alt_por = False
                            
                comando = f"UPDATE sustentabilidade SET residuos_reciclados = '{porcentagem}' WHERE codigo = '{cod_alt}';"
                cursor.execute(comando)
                conexao.commit()
                bd_alt = False

            else:
                transporteAlt = True
                while transporteAlt:
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
                        print("O valor deverá ser um número! Tente novamente.")
                    else:
                        if transporte > 6 or transporte < 1:
                            print("Não há correspondência para esse transporte! Tente novamente.")
                        else:
                            transporteAlt = False

                transporte_bancoAlt = None
                if transporte == 1:
                    transporte_bancoAlt = "Transporte público (ônibus, metrô, trem)"
                elif transporte == 2:
                    transporte_bancoAlt = "Bicicleta"
                elif transporte == 3:
                    transporte_bancoAlt = "Caminhada"
                elif transporte == 4:
                    transporte_bancoAlt = "Carro (combustível fósseis)"
                elif transporte == 5:
                    transporte_bancoAlt = "Carro elétrico"
                else:
                    transporte_bancoAlt = "Carona compartilhada"

                comando = f"UPDATE sustentabilidade SET transporte = '{transporte_bancoAlt}' WHERE codigo = '{cod_alt}';"
                cursor.execute(comando)
                conexao.commit()
                bd_alt = False

        

    if menu_resposta == 3:
        # Código para deletar informações do banco de dados
        cod_del = int(input("Digite o codigo da checagem que você desaja deletar: "))
        comando = f"DELETE FROM sustentabilidade WHERE codigo = {cod_del};"
        cursor.execute(comando)
        conexao.commit()
        

    if menu_resposta == 4:
        bancodado = False
        
    
# Fechamneto conexão com o banco de dados
cursor.close()
conexao.close()

print("################                         PROGRAMA ENCERRADO                      #######################")
