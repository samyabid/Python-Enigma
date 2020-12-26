import class_rotors as r
import class_fonctions as f

class enigma: # ici on bosse avec des listes (pas des chaines)
	def __init__(self,configuration,reglage,MESSAGE):
		self.R1,self.R1_,self.R2,self.R2_,self.R3,self.R3_,self.REF = configuration
		self.RR1,self.RR2,self.RR3,self.TC = reglage
		self.MESSAGE = MESSAGE
		self.MESSAGE_= []
	
	def coder_une_lettre(self,lettre):
		lettre = self.TC[lettre]
		lettre = r.passage_rotor(self.R1,self.RR1,lettre)
		lettre = r.passage_rotor(self.R2,self.RR2,lettre)
		lettre = r.passage_rotor(self.R3,self.RR3,lettre)
		lettre = self.REF[lettre]
		lettre = r.passage_rotor(self.R3_,self.RR3,lettre)
		lettre = r.passage_rotor(self.R2_,self.RR2,lettre)
		lettre = r.passage_rotor(self.R1_,self.RR1,lettre)
		lettre = self.TC[lettre]
		return lettre

	def coder_une_lettre_exemple(self,lettre):
		print ("lettre",lettre)
		lettre = self.TC[lettre]
		print ("sortie du TC",lettre)
		lettre = r.passage_rotor(self.R1,self.RR1,lettre)
		print ("sortir R1",lettre)
		lettre = r.passage_rotor(self.R2,self.RR2,lettre)
		print ("sortir R2",lettre)
		lettre = r.passage_rotor(self.R3,self.RR3,lettre)
		print ("sortir R3",lettre)
		lettre = self.REF[lettre]
		print ("sortir ref",lettre)
		lettre = r.passage_rotor(self.R3_,self.RR3,lettre)
		print ("sortir R3 -1",lettre)
		lettre = r.passage_rotor(self.R2_,self.RR2,lettre)
		print ("sortir R2 -1",lettre)
		lettre = r.passage_rotor(self.R1_,self.RR1,lettre)
		print ("sortir R1 -1",lettre)
		lettre = self.TC[lettre]
		print ("sortie TC",lettre)
		return lettre

	def coder_MESSAGE (self):
		for i in self.MESSAGE:
			self.MESSAGE_ += [self.coder_une_lettre(i)]
			self.RR1,self.RR2,self.RR3 = f.actualisation_des_reglages(self.RR1,self.RR2,self.RR3)


