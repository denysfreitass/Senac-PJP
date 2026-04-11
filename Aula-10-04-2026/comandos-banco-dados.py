'''
SQL - Structured Query Language é uma linguagem de programação usada para gerenciar e manipular bancos de dados relacionais. Com o SQL, você pode executar várias operaçãoes, como criar, modificar e consultar bancos de dados. 
                                          SQL
                         /-----|-----------|---------|-------\            
                       /       |           |         |        \ 
                    DQL       DML         DDL        DCL       DTL
                  /            |           |          |         \       
            select          insert       create     grant      begin
                            update       alter      revoke     commit
                            delet        drop                  rollback

Tipos de charset
character set é o nome que se dá a um conjunto de caracteres especificos utilizado no banco de dados.

existe um tipo sugerido na maioria das instalações que é o UTF-8. ele é considerado como charset universal por suportar a maioria dos idiomas do mundo.

exemplo de código para denifir o charset

CREATE DATABASE meu_banco
CHARACTER SET WE8ISO88591

'''

## FUNÇÃO CREATE
##  CREATE TABLE table_name (COLUMN_NAME DATATYPES[,.....]);
## exemplo
## CREATE TABLE employ(Name VARCHAR2(20), Email VARCHAR2(100), DO@ DATE)

'''
INT - NUMERO INTEIRO

INSERT INTO exemplo (idade) VALUES (25);
SELECT idade FROM exemplo;
---------------------------------------------------
BIGINT - NUMEROS GRANDES
INSERT INTO exemplo (codigos) VALUES (999999999);
SELECT codigo FROM exemplo;
---------------------------------------------------
DECIMAL(p, s) - NUMEROS COM CASAS DECIMAIS
usado para valores monetários ou exatos
*p = total de dígitos
*s = digitos após o ponto decimal

INSERT INTO exemplo (preco) VALUES (99.99);
SELECT preco FROM exemplo;
----------------------------------------------------
FLOAT - NUMEROS DECIMAL DE PRECISÃO SIMPLES
usado para numeros com casas decimais

-----------------------------------------------------
VARCHAR(n) - TEXTO COM TAMANHO VARIÁVEL
usado para nomes, emails, endereços 
exemplo: nome VARCHAR(100)

INSERT INTO exemplo(nome) VALUES ('Maria Silva')
SELECT nome FROM exemplo;
-----------------------------------------------------
CHAR(n) - TEXTO COM TAMANHO FIXO
usado para campos com numeros fixos - exemplo CPF OU CEP
exemplo: estado CHAR(2)

INSERT INTO exemplo (estado) VALUES ('SP');
SELECT estado FROM exemplo;
-----------------------------------------------------
TEXT - TEXTO LONGO
usado para observações 
INSET INTO exemplo ()
------------------------------------------------------

DATA - apenas DATA
INSERT INTO exemplo (data) VALUES ('2025-05-25');
SELECT data FROM exemplo;
------------------------------------------------------
TIME - APENAS HORA
INSERT INTO exemplo (horario) VALUES ('14:30:00')
SELECT horario FROM exemplo;
------------------------------------------------------
DATETIME - DATA E HORA JUNTOS

INSERT INTO exemplo (registro) VALUES ('2025-05-25 14:30:00');
SELECT registro FROM exemplo;
------------------------------------------------------
BOOLEAN OU TINYINT(1) - verdadeiro ou falso
USADO PARA INDICAR SE ALGO ESTÁ ATIVO, VÁLIDO, ETC..
exemplo: ativo = 1 (sim), 0 (não)

INSERT INTO exemplo (ativo) VALUES (1);
SELECT ativo FROM exemplo;
------------------------------------------------------
TIMESTAMP - data e hora com fuso horário automatico ( UTC)
usado para registrar automaticamente data e hora de criação ou atualização de um registro
exemplo : log de sistema

INSERT INTO exemplo (ultimo_acesso) VALUES(CURRENT_TIMESTAMP);
SELECT ultimo_acesso FROM exemplo;

-------------------------------------------------------
ENUM - lista de valores permitidos
usado para opções fixas
exemplo: status do usuário

INSERT INTO exemplo (status) VALUES ('ativo');
SELECT status FROM exemplo;

** valores possíveis
ativo | inativo | bloqueado

-------------------------------------------------------

CRIAÇÃO DE TABELAS
exemplo - tabela com nome 'alunos' dentro dela tenho ( matricula, nome, idade, curso)

CREATE TABLE alunos (
matricula INT,
nome VARCHAR(100),
idade INT,
curso VARCHAR(50)
);

exemplo 2

CREATE TABLE curso (
id INT NOT NULL AUTO_INCREMENT,
PRIMARY KEY ('id'),
qtde_vaga INT,
nome VARCHAR(100),
data_criacao DATE,
status ENUM('ativo', 'inativo') DEFAULT 'ativo',
);

INSERINDO VALORES
exemplo

INSERT INTO curso (nome,qtde_vaga,status) VALUES ('Curso Python', 20,'ativo')
'''