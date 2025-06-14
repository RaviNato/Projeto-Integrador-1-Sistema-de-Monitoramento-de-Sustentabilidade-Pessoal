﻿'''
 Criar tabela no banco dados

CREATE TABLE BD240225234.projeto(
	codigo int not null auto_increment,
    nome varchar(50) not null,
	data_checagem date not null,
    agua_litros decimal(10,2) not null,
    energia_KWh decimal(10,2) not null,
    residuos_nao_resiclaveis_Kg decimal(10,2) not null,
    residuos_reciclados decimal(10,2) not null,
    transporte varchar(50) not null,
    classificacao_agua varchar(25) not null,
    classificacao_energia varchar(25) not null,
    classificacao_lixo varchar(25) not null,
    classificacao_transporte varchar(25) not null,
    PRIMARY KEY (codigo)
) DEFAULT CHARSET = utf8mb4;
'''









# Fazendo a conexao com o MySQL
import pprint
from mysql.connector import connect, Error

# Conectando com o baco de dados
def obterConxao ():
    if obterConxao.conexao==None:
        obterConxao.conexao = connect(
            host="172.16.12.14", # Deve ser preenchido com o hostname da conexao MySQL onde esta o banco de dados
            user="BD240225234", # Deve ser preenchido com o username da conexao MySQL onde esta o banco de dados
            password="Kexms4", # Deve ser preenchido com o username da conexao MySQL onde esta o banco de dados
            database="BD240225234" # Deve ser preenchido com o nome do banco de dados
            )
    return obterConxao.conexao
obterConxao.conexao=None

# Codigo para inserir uma novo registro no banco de dados
def entradBD(nome, ano, mes, dia, litros, kwh, kg, porcentagem, transporte_banco, consumAgua, consumEnergia, consumLixo, consumTransporte):
    comando = ("INSERT INTO BD240225234.projeto"
           "(nome, data_checagem, agua_litros, energia_KWh, residuos_nao_resiclaveis_Kg, residuos_reciclados, transporte, classificacao_agua, classificacao_energia, classificacao_lixo, classificacao_transporte)"
           "VALUES"
           f"('{nome}', '{ano}.{mes}.{dia}', '{litros}', '{kwh}', '{kg}', '{porcentagem}', '{transporte_banco}', '{consumAgua}', '{consumEnergia}', '{consumLixo}', '{consumTransporte}') ")
    
    conexao=obterConxao()
    cursor=conexao.cursor()
    cursor.execute(comando)
    conexao.commit()

# Codigo para chamar entradas da lista de checagem
def listaDeDados():
    comando = f"SELECT codigo, nome, DATE_FORMAT(data_checagem,'%d/%m/%Y'), agua_litros, energia_KWh, residuos_nao_resiclaveis_Kg, residuos_reciclados, transporte, classificacao_agua, classificacao_energia, classificacao_lixo, classificacao_transporte FROM BD240225234.projeto;"
    conexao=obterConxao()
    cursor=conexao.cursor()
    cursor.execute(comando)


    linhas = cursor.fetchall()
    return linhas

# Codigo para criar uma lista com os dados guardados no banco de dados
def listar():
    try:
        linha=listaDeDados() #Chamando o sub programa para pega os dados
    except Error:
        print("Problema de conexão com o BD!")
    else:
        atual=0
        while atual<len(linha):
            print()
            print("CODIGO......................: ", linha[atual][0])
            print("NOME........................: ", linha[atual][1])
            print("DATA........................: ", linha[atual][2])
            print("ÁGUA(LITROS)................: ", linha[atual][3])
            print("ENERGIA(KWh)................: ", linha[atual][4])
            print("RESÍDUOS NÃO RECICLÁVEIS(Kg): ", linha[atual][5])
            print("RESÍDUOS RECICLADOS(%)......: ", linha[atual][6])
            print("TRANSPORTE..................: ", linha[atual][7])
            print("CONSUMO DE ÁGUA.............: ", linha[atual][8])
            print("CONSUMO DE ENERGIA ELÉTRICA.: ", linha[atual][9])
            print("GERAÇÃO LIXO NÃO RECICLÁVEL.: ", linha[atual][10])
            print("USO DE TRANSPORTES..........: ", linha[atual][11])
            atual+=1

        print()

# Codigo para alterar as informações do banco de dados
def alterarBD(coluna, codigo, novoBD, novoBD2, novoBD3):
    if coluna == "data_checagem":
        comando = f"UPDATE BD240225234.projeto SET data_checagem = '{novoBD3}.{novoBD2}.{novoBD}' WHERE codigo = '{codigo}';"
    else:
        comando = f"UPDATE BD240225234.projeto SET {coluna} = '{novoBD}' WHERE codigo = '{codigo}';"

    registroatual = f"SELECT codigo, nome, DATE_FORMAT(data_checagem,'%d/%m/%Y'), agua_litros, energia_KWh, residuos_nao_resiclaveis_Kg, residuos_reciclados, transporte, classificacao_agua, classificacao_energia, classificacao_lixo, classificacao_transporte FROM BD240225234.projeto WHERE codigo = '{codigo}' ;"
    conexao=obterConxao()
    cursor=conexao.cursor()
    cursor.execute(comando)
    cursor.execute(registroatual)

    linha = cursor.fetchall()

    consumAgua, consumEnergia, consumLixo, consumTransporte = ProcessamentoClassificações(linha[0][3], linha[0][4], linha[0][6], linha[0][7])
    atualizarClassificações = f"UPDATE BD240225234.projeto SET classificacao_agua = '{consumAgua}', classificacao_energia = '{consumEnergia}', classificacao_lixo = '{consumLixo}', classificacao_transporte = '{consumTransporte}' WHERE codigo = '{codigo}';"
    cursor.execute(atualizarClassificações)
    conexao.commit()

# Codigo para checar se codigo informado esta cadastrado no banco de dados
def checagemNao(codigo):
    comando = f"SELECT * FROM BD240225234.projeto WHERE codigo = '{codigo}';"
    conexao=obterConxao()
    cursor=conexao.cursor()
    cursor.execute(comando)

    linhas=cursor.fetchall()
    return linhas==[]

# Codigo para deletar infirmações do banco de dados
def deletar(codigo):
    try:
        codigoN=checagemNao(codigo) #Chamndo o sub programa para ver se codigo esta cadestrado
    except Error:
        print("Problema de conexão com o BD!")
    else:
        if codigoN:
            print("Esse codigo não esta registrado!")
        else:
            comando = f"DELETE FROM BD240225234.projeto WHERE codigo = {codigo};"
            conexao=obterConxao()
            cursor=conexao.cursor()
            cursor.execute(comando)
            conexao.commit()

# Codigo para fechar a conexão com o banco de dados
def fechaConexa():
    conexao=obterConxao()
    cursor=conexao.cursor()
    cursor.close()
    conexao.close()

# Registro
def inserir():
    datavalida = True
    while datavalida:
        try: # Tentando obter um número inteiro
            print()
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

    digitoBem = True
    litrosBem = True
    kwhBem = True
    kgBem = True
    porcentagemBem = True
    transporteBem = True


    print()
    while digitoBem:
        while litrosBem:
            try: # tentando obter um número inteiro em todas as entradas
                litros = float((input("Quantos litros de água você consumiu hoje? (Aprox. em litros): ")).replace(",", "."))
            except ValueError:
                print(f"{nome}, os valores deverão ser um número! Tente novamente.")
            else:
                if litros < 0:
                    print(f"{nome}, o valor deverá ser um valor positivo! Tente novamente.")
                else:
                    litrosBem = False

        while kwhBem:
            try:
                kwh = float((input("Quantos kWh de energia elétrica você consumiu hoje?: ")).replace(",", "."))
            except ValueError:
                print(f"{nome}, os valor deverá ser um número! Tente novamente.")
            else:
                if kwh < 0:
                    print(f"{nome}, o valor deverá ser um valor positivo! Tente novamente.")
                else:
                    kwhBem = False

        while kgBem:
            try:
                kg = float((input("Quantos kg de resíduos não recicláveis você gerou hoje?: ")).replace(",", "."))
            except ValueError:
                print(f"{nome}, os valor deverá ser um número! Tente novamente.")
            else:
                if kg < 0:
                    print(f"{nome}, o valor deverá ser um valor positivo! Tente novamente.")
                else:
                    kgBem = False

        while porcentagemBem:
            try:
                porcentagem = float((((input("Qual a porcentagem de resíduos reciclados no total (em %)?: ")).replace("%", "")).replace(",", ".")).strip())
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
                    "Qual o meio de transporte você usou hoje?: \n",\
                    "[1] Transporte público (ônibus, metrô, trem)\n",\
                    "[2] Bicicleta\n",\
                    "[3] Caminhada\n",\
                    "[4] Carro (combustível fósseis)\n",\
                    "[5] Carro elétrico\n",\
                    "[6] Carona compartilhada")
                transporte = int(input(""))
            except ValueError:
                print(f"{nome}, o valor deverá ser um número! Tente novamente.")
            else:
                if transporte > 6 or transporte < 1:
                    print(f"{nome}, não há correspondência para esse transporte! Tente novamente.")
                    print()
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
        f"##############        {nome}, aqui está o resultado de suas classificações!         #############\n",\
        "\n",\
        f"  Consumo de água:                        {consumAgua}\n",\
        f"  Consumo de Energia Elétrica:            {consumEnergia}\n",\
        f"  Geração de Resíduos Não Recicláveis:    {consumLixo}\n",\
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

    try:
        entradBD(nome, ano, mes, dia, litros, kwh, kg, porcentagem, transporte_banco, consumAgua, consumLixo, consumEnergia, consumTransporte)# Chama o sub programa para inserir as imformções
    except Error:
        print("Erro nos dados digitados!")
    else:
        print("Dados cadastrados com sucesso\n")

# Seleciona as médias
def media():
    comando = f"SELECT ROUND(AVG(agua_litros), 2) AS MediaAgua, ROUND(AVG(energia_KWh), 2) AS MediaEnergia, ROUND(AVG(residuos_nao_resiclaveis_Kg), 2) AS ResiduosLixo, ROUND(AVG(residuos_reciclados), 2) AS PorcentagemLixoReciclado, ( SELECT transporte FROM BD240225234.projeto GROUP BY transporte ORDER BY COUNT(*) DESC LIMIT 1 ) AS TransporteMaisFrequente FROM BD240225234.projeto;;"
    conexao=obterConxao()
    cursor=conexao.cursor()
    cursor.execute(comando)


    linhas = cursor.fetchall()
    return linhas

# Processando as classificações gerais
def ProcessamentoClassificações (agua, energia, lixo, transporte):   
    AltaSustentabilidade = "Alta Sustentabilidade"
    ModeradaSustentabilidade = "Moderada Sustentabilidade"
    BaixaSustentabilidade = "Baixa Sustentabilidade"

    if agua < 150:
        consumAgua = AltaSustentabilidade
    elif agua > 151 and agua < 201:
        consumAgua = ModeradaSustentabilidade
    else:
        consumAgua = BaixaSustentabilidade

    if energia < 5:
        consumEnergia = AltaSustentabilidade
    elif energia > 4 and energia < 11:
        consumEnergia = ModeradaSustentabilidade
    else:
        consumEnergia = BaixaSustentabilidade

    if lixo > 50:
        consumLixo = AltaSustentabilidade
    elif lixo > 19 and lixo < 51:
        consumLixo = ModeradaSustentabilidade
    else:
        consumLixo = BaixaSustentabilidade

    if transporte in [1, 2, 3, 5]:
        consumTransporte = AltaSustentabilidade
    elif transporte == 4:
        consumTransporte = BaixaSustentabilidade
    else:
        consumTransporte = ModeradaSustentabilidade

    return consumAgua, consumEnergia, consumLixo, consumTransporte

# Lista as médias gerais do BD
def listarMedias():
    try:
        linha=media() #Chamando o sub programa para pega os dados
    except Error:
        print("Problema de conexão com o BD!")
    else:
        atual=0
        while atual<len(linha):

            consumAgua, consumEnergia, consumLixo, consumTransporte = ProcessamentoClassificações(linha[atual][0], linha[atual][2], linha[atual][3], linha[atual][4])

            print()
            print(f"##############        {nome}, aqui está a média de todos os registros!          ###############")
            print()
            print("MÉDIA DO CONSUMO DE ÁGUA....: ", linha[atual][0])
            print("MÉDIA DO CONSUMO DE ENERGIA.: ", linha[atual][1])
            print("MÉDIA DO CONSUMO DE LIXO....: ", linha[atual][2])
            print("MÉDIA DA % DE LIXO RECICLADO: ", linha[atual][3])
            print("TRANSPORTE MAIS UTILIZADO...: ", linha[atual][4])
            print("CONSUMO DE ÁGUA.............: ", consumAgua)
            print("CONSUMO DE ENERGIA ELÉTRICA.: ", consumEnergia)
            print("GERAÇÃO LIXO NÃO RECICLÁVEL.: ", consumLixo)
            print("USO DE TRANSPORTES..........: ", consumTransporte)

            atual+=1
        print()


print("################        PROGRAMA DE MONITORAMENTO DE SUSTENTABILIDADE PESSOAL     #######################")

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


# Menu para acessar o banco de dados
bancodado = True
while bancodado:
    menubd = True
    while menubd:
        try:
            print()
            print(
                "O que você deseja fazer?\n",\
                "[1]Inserir registro.\n",\
                "[2]Ver todos os registros.\n",\
                "[3]Alterar registro.\n",\
                "[4]Deletar registro.\n",\
                "[5]Visualizar médias gerais.\n",\
                "[6]Encerrar programa.")
            menu_resposta=int(input(""))
        except ValueError:
            print(f"{nome}, o valor deverá ser um número! Tente novamente.")
        else:
            if menu_resposta > 6 or menu_resposta < 1:
                print(f"{nome}, não há correspondência para essa opção! Tente novamente.")
            else:
                menubd = False


    if menu_resposta == 1:
        inserir()# Chama o sub programa para fazer inserir um registro


    
    if menu_resposta == 2:
        listar()# Chama o sub programa para fazer lista das informações



    if menu_resposta == 3:
        
        print()
        cod_alt = int(input("Digite o codigo do registro que você desaja Alterar: "))
        try:
            codigoN=checagemNao(cod_alt) #Chamndo o sub programa para ver se codigo esta cadestrado
        except ValueError:
            print("Problema de conexão com o BD!")
        else:
            if codigoN:
                print("Esse codigo não esta registrado!")
            else:
                bd_alt = True
                while bd_alt:
                    menu_alt = True
                    while menu_alt:
                        try:
                            print()
                            print(
                                "O que você deseja alterar?\n",\
                                "[1]NOME.\n",\
                                "[2]DATA.\n",\
                                "[3]ÁGUA(LITROS).\n",\
                                "[4]ENERGIA(KWh).\n",\
                                "[5]RESÍDUOS NÃO RECICLÁVEIS(Kg).\n",\
                                "[6]RESÍDUOS RECICLADOS(%).\n",\
                                "[7]TRANSPORTE.")
                            menu_resposta_alt=int(input(""))
                        except ValueError:
                            print(f"{nome}, o valor deverá ser um número! Tente novamente.")
                        else:
                            if menu_resposta_alt > 7 or menu_resposta_alt < 1:
                                print(f"{nome}, não há correspondência para essa opção! Tente novamente.")
                            else:
                                
                                menu_alt = False

            
                    if menu_resposta_alt == 1:
                        print()
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

                        alterarBD("nome", cod_alt, nomeAlt, 0, 0)# Chama o sub programa para alterar a informação do banco de dados
                        bd_alt = False

                    elif menu_resposta_alt == 2:
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

                        alterarBD("data_checagem", cod_alt, dia, mes, ano)# Chama o sub programa para alterar a informação do banco de dados
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
                                print()
                                valor = float(input("Digite o novo valor: "))
                            except ValueError:
                                print(f"{nome}, os valores deverão ser um número! Tente novamente.")
                            else:
                                if valor < 0:
                                    print(f"{nome}, o valor deverá ser um valor positivo! Tente novamente.")
                                else:
                                    alt_aer = False

                        
                        alterarBD(coluna, cod_alt, valor, 0, 0)# Chama o sub programa para alterar a informação do banco de dados
                        bd_alt = False

                    elif menu_resposta_alt == 6:
                        alt_por = True
                        while alt_por:
                            try:
                                print()
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
                                    
                        alterarBD("residuos_reciclados", cod_alt, porcentagem, 0, 0)# Chama o sub programa para alterar a informação do banco de dados
                        bd_alt = False

                    else:
                        transporteAlt = True
                        while transporteAlt:
                            try:
                                print()
                                print(
                                    "Qual o meio de transporte você usou hoje?: \n",\
                                    "[1] Transporte público (ônibus, metrô, trem)\n",\
                                    "[2] Bicicleta\n",\
                                    "[3] Caminhada\n",\
                                    "[4] Carro (combustível fósseis)\n",\
                                    "[5] Carro elétrico\n",\
                                    "[6] Carona compartilhada")
                                transporte = int(input(""))
                                print()
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

                        alterarBD("transporte", cod_alt, transporte_bancoAlt, 0, 0)# Chama o sub programa para alterar a informação do banco de dados
                        bd_alt = False# Menu para escolher o que deseja mudar no banco de dados



    if menu_resposta == 4:
        print()
        cod_del = int(input("Digite o codigo do registro que você desaja deletar: "))
        deletar(cod_del)
        print()# Chama o sub programa deletar informações
        


    if menu_resposta == 5:
        listarMedias()# Chama o sub programa listar médias



    if menu_resposta == 6:
        fechaConexa()
        bancodado = False# Chama o sub programa para fechar a conexão
        
print()
print("######################                         PROGRAMA ENCERRADO                      #######################")