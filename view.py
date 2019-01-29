#!/usr/bin/python3
# coding:utf-8
from models import *
from dao import *
import os
import sys
class view(models):
	"""Classe responsável pela interface com o usuário"""
	def __init__(self):
		tmp_models = super(view, self).__new__(models)
		def cadastrar(self):
			self.nome = str(input("Digite o nome\n>>> : "))
			self.idade = str(input("Digite a idade\n>>> : "))

			tmp_models.set_nome(self.nome)
			tmp_models.set_idade(self.idade)
			print("Seus dados foram recebidos com sucesso !!")
			DAO.cadastrar(self, tmp_models)
		def selecionar(self):
			escolha = str(input("Digite 1 selecionar tudos os itens cadastrados\ndigite 2 para selecionar um item por ID\n>>> : "))

			if escolha == '1':
				tmp_models.set_ID(0)
				DAO.selecionar(self,escolha,tmp_models)

			elif escolha =='2':
				ID = str(input("Digite o ID\n>>> : "))
				tmp_models.set_ID(ID)
				DAO.selecionar(self,escolha,tmp_models)
			else : 
				print("escolha inválida")
				
			

		def alterar(self):
			escolha = str(input("Digite 1 para alterar o nome\nDigite 2 para alterar idade\nDigite 3 para alterar nome e idade\n>>> : "))
			if escolha == '1' :
				idade = False
				tmp_models.set_idade(idade)
				
				ID = str(input("Digite o ID do cadastro que deseja alterar"))
				tmp_models.set_ID(ID)
				
				nome = str(input("Digite para qual nome deseja alterar : "))
				tmp_models.set_nome(nome)
				
				DAO.alterar(self, escolha, tmp_models)

			elif escolha == '2' :
				nome = False
				ID = str(input("Digite o ID do cadastro que deseja alterar"))
				tmp_models.set_ID(ID)

				idade = str(input("Digite para qual idade  deseja alterar : "))
				tmp_models.set_idade(idade)

				DAO.alterar(self, escolha, tmp_models)

			elif escolha == '3' :
				ID = str(input("Digite o ID do cadastro que deseja alterar : "))
				tmp_models.set_ID(ID)

				nome = str(input("Digite para qual  nome que deseja alterar : "))
				tmp_models.set_nome(nome)

				idade = str(input("Digite para qual idade  deseja alterar : "))
				tmp_models.set_idade(idade)

				DAO.alterar(self, escolha, tmp_models )
			else:
				print("opção inválida")
		
		def excluir(self):
			escolha = str(input("Digite 1 para excluir todos\nDigite 2 para excluir por ID\n>>> : "))
			if escolha == '1':
				tmp_models.set_ID(0)
				DAO.excluir(self,escolha,tmp_models)
			elif escolha == '2':
				self.id = str(input("Digite o ID do cadastro que deseja excluir\n>>> : "))
				tmp_models.set_ID(self.id)
				print(type(self.id))
				DAO.excluir(self,escolha,tmp_models)

			else :
				print("Opção inválida")
				view()


			



		n = 1
		while n != 0 :
			os.system("clear")
			print("Bem vindo ao sistema de gerenciamento de dados crud !!")
			print("======================================================")
			print("""Digite 1 para cadastrar\nDigite 2 para buscar\nDigite 3 para modificar\nDigite 4 para excluir\nDigite 5 para sair""")
			print("======================================================")
			escolha = str( input(">>> : "))

			if escolha == '1':
				cadastrar(self)
				
			elif escolha == '2':
				
				selecionar(self)
			elif escolha == '3':
				
				alterar(self)
			elif escolha == '4':
				
				excluir(self)
			elif escolha == '5':
		
				n = 1
				exit()
			else : 
				print("opção inválida")
					