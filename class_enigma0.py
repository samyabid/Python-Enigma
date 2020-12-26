"""
ICI LA MACHINE N EST PAS MUNI DE TABLEAU DES CONNEXIONS
"""

import class_rotors as r
import class_fonctions as f

class enigma0:
	def __init__(self,configuration,reglage,MESSAGE): # attention ici reglage ne comprend pas le tableau des connexions !!!
		self.R1,self.R1_,self.R2,self.R2_,self.R3,self.R3_,self.REF = configuration
		self.RR1,self.RR2,self.RR3 = reglage
		self.MESSAGE = MESSAGE
		self.MESSAGE_= []
	
	def coder_une_lettre(self,lettre):
		lettre = r.passage_rotor(self.R1,self.RR1,lettre)
		lettre = r.passage_rotor(self.R2,self.RR2,lettre)
		lettre = r.passage_rotor(self.R3,self.RR3,lettre)
		lettre = self.REF[lettre]
		lettre = r.passage_rotor(self.R3_,self.RR3,lettre)
		lettre = r.passage_rotor(self.R2_,self.RR2,lettre)
		lettre = r.passage_rotor(self.R1_,self.RR1,lettre)
		return lettre

	def coder_MESSAGE (self):
		for i in self.MESSAGE:
			self.MESSAGE_ += [self.coder_une_lettre(i)]
			self.RR1,self.RR2,self.RR3 = f.actualisation_des_reglages(self.RR1,self.RR2,self.RR3)

