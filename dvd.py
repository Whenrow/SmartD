# Ressources du Projet : classe DVD et fonctions
# -*- coding: utf8 -*-

import json

class Dvd():
	""" Objet de type dvd represantant un film"""
	def __init__(self, titre, lieu, etagere):
		# Capitalize each word
		titre = " ".join([mot.title() for mot in titre.split(" ")])

		self._titre   = titre
		self._lieu    = lieu.title()
		self._etagere = etagere.title()

	def __str__(self):
		string = ""
		string += self._titre
		if self._lieu != "Liernu":
			string += " a "
			string += self._lieu
		else:
			string += " sur l'etagere "
			string += self._etagere
		return string

	def titre():
	    doc = "The titre property."
	    def fget(self):
	        return self._titre
	    def fset(self, value):
	        self._titre = value
	    def fdel(self):
	        del self._titre
	    return locals()
	titre = property(**titre())

	def lieu():
	    doc = "The lieu property."
	    def fget(self):
	        return self._lieu
	    def fset(self, value):
	        self._lieu = value
	    def fdel(self):
	        del self._lieu
	    return locals()
	lieu = property(**lieu())

	def etagere():
	    doc = "The etagere property."
	    def fget(self):
	        return self._etagere
	    def fset(self, value):
	        self._etagere = value
	    def fdel(self):
	        del self._etagere
	    return locals()
	etagere = property(**etagere())

	def serialize(self):
		""" Serialize l'objet au format json"""
		return {"titre" : self._titre,
				"etagere" : self._etagere,
				"lieu" : self._lieu}

class Bibliotheque():
	""" Liste de films """
	def __init__(self):
		self._liste = []

	def __str__(self):
		# liste de tout les titre
		l = [x.titre for x in self.liste]
		l = "[" + ",".join(l) + "]"
		return l

	def liste():
	    doc = "The liste property."
	    def fget(self):
	        return self._liste
	    def fset(self, value):
	        self._liste = value
	    def fdel(self):
	        del self._liste
	    return locals()
	liste = property(**liste())

	def tri(self,item = 'titre'):
		""" Tri de la liste de films suivant une certaine cle"""
		if item == 'titre':
			self._liste.sort(key = lambda x: x.titre)
		elif item == 'lieu':
			self._liste.sort(key = lambda x: x.lieu)
		elif item == 'etagere':
			self._liste.sort(key = lambda x : x.etagere)

	def load(self):
		""" Charge la liste dans le json """
		fichier = open("/home/will/Dropbox/SmartD/films.json",'r')
		films = json.load(fichier)
		for film in films:
			dvd = Dvd(film["titre"],film["lieu"],film["etagere"])
			self._liste.append(dvd)
		fichier.close()

	def save(self):
		""" Sauve la liste des film dans le fichier json"""
		fichier = open("films.json",'w')
		json.dump([film.serialize() for film in self._liste],fichier)

		fichier.close()

	def addFilm(self,film):
		""" Ajoute un film a la bibliotheque """
		if film.titre not in [dvd.titre for dvd in self.liste]:
			self._liste.append(film)
		else:
			print "Film deja present"
