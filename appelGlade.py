#!/usr/bin/python
import pygtk
pygtk.require("2.0")
import gtk

class HelloWorld:
	def __init__(self):
		interface = gtk.Builder()
		interface.add_from_file('layout.glade')

		interface.connect_signals(self)

	def on_mainWindow_destroy(self, widget):
		gtk.main_quit()

if __name__ == "__main__":
	HelloWorld()
	gtk.main()
