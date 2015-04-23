# Fichier principal du projet
# -*- coding: utf8 -*-
#!/usr/bin/python
import pygtk
import dvd
pygtk.require("2.0")
import gtk

class GuiAjout(gtk.Window):
	# Champs à remplir
	titre = gtk.Entry()
	etagere = gtk.Entry()
	lieu = gtk.Entry()
	maBibli = dvd.Bibliotheque()

	def __init__(self,bibli):
		# Fenetre d'ajout
		GuiAjout.maBibli = bibli
		fenetreAjout = gtk.Window()
		fenetreAjout.set_title("Ajout d'un nouveau titre")
		fenetreAjout.connect("destroy",fenetreAjout.destroy)
		fenetreAjout.set_position(gtk.WIN_POS_CENTER)
		fenetreAjout.activate_focus()

		GuiAjout.lieu.set_text("Liernu")

		# Boutons d'action
		finir = gtk.Button("Sauver et Fermer")
		finir.connect_object("clicked",self.finirClicked,self)
		autreAjout = gtk.Button("Nouvel ajout")

		# Structure de la fenetre
		vboite = gtk.VBox()
		vboite.pack_start(GuiAjout.titre)
		vboite.pack_start(GuiAjout.etagere)
		vboite.pack_start(GuiAjout.lieu)

		hboite = gtk.HBox()
		hboite.pack_start(finir)
		hboite.pack_start(autreAjout)

		vboite.pack_start(hboite)

		fenetreAjout.add(vboite)
		fenetreAjout.show_all()

	def finirClicked(self,widget):
		titre = GuiAjout.titre.get_text()
		etagere = GuiAjout.etagere.get_text()
		lieu = GuiAjout.lieu.get_text()
		GuiAjout.maBibli.addFilm(dvd.Dvd(titre,lieu,etagere))
		widget.destroy()

class GUI(gtk.Window):
	maBibli = dvd.Bibliotheque()
	def __init__(self,bibli):
		super(GUI, self).__init__()
		maBibli = bibli

		# Main Window + parameters
		self.set_title("SmartD")
		self.connect("destroy",self.on_fenetre_destroy)
		self.set_position(gtk.WIN_POS_CENTER)
		self.activate_focus()
		self.set_geometry_hints(None,min_width=300,min_height=200)

		# treeView containing the list
		self.fond = gtk.TreeView()
		self.updateListe(maBibli)

		# Boutton d'ajout
		ajoutBouton = gtk.Button(stock=gtk.STOCK_ADD)
		ajoutBouton.connect("clicked",self.trigerAjout)
		ajoutBouton.set_use_stock(True)
		ajoutBouton.set_image_position(gtk.POS_LEFT)

		# MaJ des colonnes
		self.updateListe(maBibli)

		# Vert Layout
		vboite = gtk.VBox()
		vboite.pack_start(self.fond)
		vboite.pack_start(ajoutBouton)

		self.add(vboite)
		self.show_all()

	def updateListe(self, bibli):
		# Vidage du fond
		for col in self.fond.get_columns():
			self.fond.remove_column(col)

		# Remplissage de la liste
		liste = gtk.ListStore(str,str,str)
		for film in maBibli.liste:
			liste.append([film.titre,film.etagere,film.lieu])

		# Remplisage du fond
		self.fond.set_model(liste)
		self.fond.set_headers_visible(True)
		self.fond.set_rules_hint(True)
		self.create_columns(self.fond)

	def create_columns(self, treeView):
		# Structure de la liste de DVD
		rendererText = gtk.CellRendererText()
		column = gtk.TreeViewColumn("Titre", rendererText, text=0)
		column.set_sort_column_id(0)
		treeView.append_column(column)

		rendererText = gtk.CellRendererText()
		column = gtk.TreeViewColumn("Etagere", rendererText, text=1)
		column.set_sort_column_id(1)
		treeView.append_column(column)

		rendererText = gtk.CellRendererText()
		column = gtk.TreeViewColumn("Lieu", rendererText, text=2)
		column.set_sort_column_id(2)
		treeView.append_column(column)

	def addRow(self,film):
		# Ajoute un ligne (un film) dans la liste
		self.listeGenerale.append([film.titre,film.Lieu,film.etagere])

	def trigerAjout(self,widget):
		ajout = GuiAjout(maBibli)
		self.updateListe(maBibli)

	def on_fenetre_destroy(self, widget):
		gtk.main_quit()

if __name__ == "__main__":
	maBibli = dvd.Bibliotheque()
	maBibli.load()
	GUI(maBibli)

	gtk.main()
	maBibli.save()
