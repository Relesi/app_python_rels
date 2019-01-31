#C:\Program Files (x86)\Python37-32

class models(object):
	def __init__(self,ID="", nome="", idade=""):
		self.ID = ID
		self.nome = nome
		self.idade = idade
	
	
	def set_ID(self, ID):
		self.ID = ID
		print("ID OK")

	def get_ID(self):
		return self.ID
	

	def set_nome(self, nome):
		self.nome = nome
		print("nome OK!!")

	def get_nome(self):
		return self.nome 
	
	

	def set_idade(self, idade):
		self.idade = idade
		print("idade OK!!")

	def get_idade(self):
		return self.idade

