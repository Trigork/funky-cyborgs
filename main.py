#!/usr/bin/python
# __*__ conding: utf-8 __*__

from gi.repository import Gtk
from gi.repository import GdkPixbuf

class App:
	def __init__(self):
		builder=Gtk.Builder()
		builder.add_from_file("interfaz.glade")
		builder.connect_signals(self)
		principal=builder.get_object("window1")
		principal.show_all()
		nEvento=builder.get_object("dialog1")
		login=builder.get_object("window2")
		about=builder.get_object("window3")
		

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
	
	def on_menu_nuevo(self,principal,nEvento):
		
		print("Nuevo")
		nEvento.show_all()
		
	
	def on_menu_eliminar(self,principal):
	
		print("Eliminar")
	
	def on_menu_salir(self,principal):
	
		print("Salir")
		
	def on_menu_logoff(self,principal):
	
		print("Logoff")	
	
	def on_menu_preferencias(self,principal):
	
		print("Preferencias")
	
	def on_menu_about(self,principal):
	
		print("About")
	
#Nuevo evento

	def on_newevent_cancelar(self,principal):

		print("Cancelar")
		nEvento.destroy()
	def on_newevent_aceptar(self,principal):
	
		print("Aceptar")
		nEvento.destroy()	
#Login

	def on_login_cancelar(self,principal):
	
		print("Cancelar")	
		
	def on_login_connect(self,principal):
	
		print("Conectar")
		
#About

	def on_about_salir(self,principal):
		
		print("Salir")

App()

Gtk.main()
