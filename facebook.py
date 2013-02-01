#!/usr/bin/python 


import gtk
import webkit
import gobject



gobject.threads_init()
win = gtk.Window()
win.set_size_request(1024, 800)
win.set_title("Facebook for Ubuntu")
win.set_resizable(False)
win.set_position(gtk.WIN_POS_CENTER)
bro = webkit.WebView()
bro.open("http://m.facebook.com")
win.add(bro)
win.show_all()

gtk.main()
