CREATE DATABASE projeto;
USE projeto;

# Criação da tabela 
CREATE TABLE projeto.sustentabilidade(
	codigo int not null auto_increment,
    nome varchar(50) not null,
	data_checagem date not null,
    agua_litros decimal(10,2) not null,
    energia_KWh decimal(10,2) not null,
    residuos_nao_resiclaveis_Kg decimal(10,2) not null,
    residuos_reciclados decimal(10,2) not null,
    transporte varchar(50) not null,
    PRIMARY KEY (codigo)
);

