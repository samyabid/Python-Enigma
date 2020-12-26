import class_fonctions as f
import class_enigma0 as e0

class bombe():
	def __init__(self,MESSAGE_SUPPOSE,MESSAGE_INTERCEPTE,configuration):
		self.MESSAGE_SUPPOSE = MESSAGE_SUPPOSE
		self.MESSAGE_INTERCEPTE = MESSAGE_INTERCEPTE
		self.menu = [] # c'est le menu sous forme [position,lettre,lettre]
		self.R1,self.R1_,self.R2,self.R2_,self.R3,self.R3_,self.REF = configuration

	def creer_menu(self):
		for i in range (0,len(self.MESSAGE_SUPPOSE)):
			self.menu += [[i,self.MESSAGE_SUPPOSE[i],self.MESSAGE_INTERCEPTE[i]]]