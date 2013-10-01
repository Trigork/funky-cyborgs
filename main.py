#!/usr/bin/python
# __*__ conding: utf-8 __*__

from gi.repository import Gtk
from gi.repository import GdkPixbuf

class App:
	def __init__(self):
		builder=Gtk.Builder()
		builder.add_from_file("interfaz.glade")
		builder.connect_signals(self)
		self.principal=builder.get_object("window1")
		#principal.show_all()
		self.nEvento=builder.get_object("dialog1")
		self.login=builder.get_object("window2")
		self.login.show_all()
		self.about=builder.get_object("window3")
		
		

#Ventana Principal
	
	def on_anterior(self,principal):
	
		print("Anterior")
	
	def on_siguiente(self,principal):
	
		print("Siguiente")
	
	def on_info(self,principal):
	
		print("Info")
	
	def on_dia(self,principal):
	
		print("Dia")
	
	#Menu
	
	def on_menu_nuevo(self,principal):
		
		print("Nuevo")
		
		self.nEvento.show_all()
		
	
	def on_menu_eliminar(self,principal):
	
		print("Eliminar")
	
	def on_menu_salir(self,principal):
	
		print("Salir")
		quit(-1)
		
	def on_menu_logoff(self,principal):
	
		print("Logoff")
		self.principal.hide()
		self.login.show_all()
	
	def on_menu_preferencias(self,principal):
	
		print("Preferencias")
	
	def on_menu_about(self,principal):
	
		print("About")
		self.about.show_all()
	
#Nuevo evento

	def on_newevent_cancelar(self,principal):

		print("Cancelar")
		self.nEvento.hide()
	def on_newevent_aceptar(self,principal):
	
		print("Aceptar")
		self.nEvento.hide()
#Login

	def on_login_cancelar(self,principal):
	
		print("Cancelar")
		exit(-1)	
		
	def on_login_connect(self,principal):
	
		print("Conectar")
		self.login.hide()
		self.principal.show_all()
		
		
#About

	def on_about_salir(self,principal):
		
		print("Salir")
		self.about.hide()
		
#Salir

	def on_quit(self,principal):
		
		exit(-1)

App()

Gtk.main()
