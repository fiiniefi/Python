import gi.repository
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
import os
import imghdr

now = 0

class Window(Gtk.Window):
    def __init__(self, title):
        super().__init__()
        self.set_title(title)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("destroy", self.destroy)
        self.set_destroy_with_parent(False)

def fill_list(path, files):
    how_many = 0
    for file in os.listdir(path):
        if imghdr.what(path + "\\\\" + file):
            print(file) #debug
            files.append((path + "\\\\" + file))
            how_many += 1
    return how_many

def next(button, files, img, how_many):
    global now
    print(files[now % how_many]) #debug
    pixb = GdkPixbuf.Pixbuf.new_from_file_at_size(files[now % how_many], 400, 300)
    img.set_from_pixbuf(pixb)
    now += 1
    print(now)

def assgn(button, link, path, program, cont):
    path = link.get_text()
    if os.path.isdir(path):
        files = []
        how_many = fill_list(path, files)
        pic_window(program, cont, files, how_many)
        #print(path)  #debug

def pic_window(program, cont, files, how_many):
    cont.destroy()
    cont = Gtk.Grid()
    img = Gtk.Image()
    next(None, files, img, how_many)
    nxt = Gtk.Button.new_with_label("Następny")
    nxt.connect("clicked", next, files, img, how_many)
    ext = Gtk.Button.new_with_label("Menu główne")
    ext.connect("clicked", main_window, program)
    cont.attach(img, 0, 0, 11, 11)
    cont.attach(nxt, 1, 12, 4, 2)
    cont.attach(ext, 6, 12, 4, 2)
    program.add(cont)
    program.show_all()

def cb(link):
    link.progress_pulse()

def chs_img(button, program, cont):
    chs = Gtk.FileChooserDialog("Wybierz zdjęcie", program, Gtk.FileChooserAction.OPEN,
                                ("Wyjdź", Gtk.ResponseType.CANCEL, "Wybierz", Gtk.ResponseType.OK))
    resp = chs.run()
    filen = ""
    if resp == Gtk.ResponseType.OK:
        filen = chs.get_filename()
        #print(filen) #debug
    chs.destroy()
    pic_window(program, cont, [filen], 1)

def main_window(button, program):
    if program != None:
        temp = program
        program = Window("Przeglądarka obrazków")
        temp.destroy()
    else:
        program = Window("Przeglądarka obrazków")
    cont = Gtk.VBox()
    program.add(cont)
    info = Gtk.Label("Podaj ścieżkę do pliku lub folderu")
    link = Gtk.Entry()
    link.set_text("Ścieżkę wpisz tutaj...")
    multi = Gtk.Button.new_with_label("Zatwierdź")
    path = ""
    multi.connect("clicked", assgn, link, path, program, cont)
    #link.connect("changed", cb)
    #link.set_progress_pulse_step(0.02)
    single = Gtk.Button.new_with_label("Wybierz Zdjęcie")
    single.connect("clicked", chs_img, program, cont)
    cont.pack_start(info, True, True, 3)
    cont.pack_start(link, True, True, 3)
    cont.pack_start(multi, True, False, 3)
    cont.pack_start(single, True, False, 3)
    #cont.pack_start(fch, True, False, 2)
    program.show_all()


main_window(None, None)
Gtk.main()
