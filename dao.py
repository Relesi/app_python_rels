#!/usr/bin/python3
# coding:utf-8
import MySQLdb as mdb
import sys
import os
from models import *

class DAO(models):
	"""Classe responsável pelo banco de dados"""
	def abre_conexao(self):
		try:
			con = mdb.connect('localhost', 'root', '123', 'crud');
			print("Conexão aberta")
			return con
		except Exception as e:
			sys.exit("Não foi possível abrir comunicação com o banco")

	def fecha_conexao(self):
		try:
			con = mdb.connect('localhost', 'root', '123', 'crud');
			con.close()
			print("Conexão encerrada")
		except Exception as e:
			sys.exit("Não foi possível encerrar comunicação com o banco de dados")

	def cadastrar(self, tmp_models):
		tmp_nome = tmp_models.get_nome()
		tmp_idade = tmp_models.get_idade()
		print(tmp_nome)
		print(tmp_idade)
		try:
			con = DAO.abre_conexao(self)
			cur = con.cursor()
			with con :
				cur.execute("INSERT INTO Pessoa(nome, idade) VALUES(%s , %s)",(tmp_nome, tmp_idade))
				con.commit()
			
			DAO.fecha_conexao(self)
			print("cadastro feito com sucesso !!")
		except Exception as e:
			sys.exit("Não foi possível efetuar cadastro")
			con.rollback()
			DAO.fecha_conexao(self)
	
	def selecionar(self, tmp_seleciona, tmp_models):
		tmp_ID = tmp_models.get_ID()
		try:
			con = DAO.abre_conexao(self)
			with con:
				cur = con.cursor()
				if tmp_seleciona == '1':
					cur.execute("SELECT * FROM Pessoa")
					con.commit()
					desc = cur.description
					print("======================================================")
					print("%s %s %s " % (desc[0][0], desc[1][0], desc[2][0]))
					print("======================================================")
					for i in range(cur.rowcount):
						row = cur.fetchone()
						print("%s %s %s " % (row[0], row[1], row[2]))
					print("======================================================")
				else :
					sql = "SELECT ID, nome, idade FROM Pessoa WHERE ID = "+tmp_ID
					print(sql)
					cur.execute(sql)
					con.commit()
					desc = cur.description
					print("======================================================")
					print("%s  %s  %s" %(desc[0][0], desc[1][0], desc[2][0]))
					print("======================================================")
					for i in range(cur.rowcount):
						row = cur.fetchone()
						print("%s  %s  %s  " % (row[0], row[1], row[2]))
					print("======================================================")

			DAO.fecha_conexao(self)
		except Exception as e:
			sys.exit("Não foi possível selecionar os itens do banco")
			DAO.fecha_conexao(self)
		
	def alterar(self, tmp_altera, tmp_models):
		tmp_nome = tmp_models.get_nome()
		tmp_idade = tmp_models.get_idade()
		tmp_ID = tmp_models.get_ID()
		con = DAO.abre_conexao(self)
		with con :
			cur = con.cursor()
			if tmp_altera == '1':
				cur.execute("UPDATE Pessoa set nome = %s where ID = %s",(tmp_nome, tmp_ID))
				con.commit()

			elif tmp_altera == '2':
				cur.execute("UPDATE Pessoa set idade = %s where ID = %s",(tmp_idade, tmp_ID))
				con.commit()

			elif tmp_altera == '3':
				cur.execute("UPDATE Pessoa set nome = %s, idade = %s where ID = %s",(tmp_nome, tmp_idade, tmp_ID))
				con.commit()

			else:
				print("erro de parâmetro no método alterar ")
		DAO.fecha_conexao(self)

	def excluir(self, escolha, tmp_models):
		tmp_ID =tmp_models.get_ID()
		try:
			con = DAO.abre_conexao(self)
			with con :
				cur = con.cursor()
				if escolha == '1':
					cur.execute("DELETE FROM Pessoa")
					con.commit()

				else:
					sql = "DELETE FROM Pessoa where ID = "+tmp_ID
					cur.execute(sql)
					con.commit()


			DAO.fecha_conexao(self)
		except Exception as e:
			sys.exit("erro ao excluir ")
	



		