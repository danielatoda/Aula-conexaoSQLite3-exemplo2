import sqlite3
from sqlite3 import Error

#criar conexao
arquivo = "banco.db"
def conexao_banco(arquivo):
  conexao = None
  try:
    conexao=sqlite3.connect(arquivo)
    print("Conexão realizada!")
  except Error as e:
    print("Erro ao conectar ao banco!", e)
  return conexao

var_conexao = conexao_banco(arquivo)

#criar tabela
create_sql = """ CREATE TABLE IF NOT EXISTS aluno(
  id integer not null primary key autoincrement,
  nome varchar(45),
  email varchar(45)
);"""

def criar_tabela(conexao,sql):
  try:
    cursor = conexao.cursor()
    cursor.execute(sql)
    print("Tabela criada com sucesso!")
  except Error as e:
    print("Erro ao criar a tabela", e)
    

criar_tabela (var_conexao, create_sql)

#inserir dados
nome = input("Insira seu nome: ")
email = input("Insira seu e-mail: ")
insert_sql = """INSERT INTO aluno (nome, email) VALUES ('++nome++', '++email++');"""

def inserir(conexao,sql):
  try:
    cursor=conexao.cursor()
    cursor.execute(sql)
    conexao.commit()
    print("Insert realizado com sucesso!")
  except Error as e:
    print("Erro ao inserir dados na tabela aluno!", e)

inserir(var_conexao, insert_sql)

var_conexao.close()