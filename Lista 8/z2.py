import gi.repository
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango
import sqlite3

class Window(Gtk.Window):
    def __init__(self, title, db):
        self.db_ref = db
        super().__init__()
        self.set_title(title)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("destroy", end_program, self.db_ref)

def end_program(_, db):
    db.close()
    Gtk.main_quit()

def db_connect():
    db = sqlite3.connect("l8z2db.db")
    return db

def find_res(_, ls, en, db_edit, cont, program):
    param = ls.get_active_text()
    val = en.get_text()
    cont.destroy()
    cont = Gtk.Grid()

    db_edit.execute("SELECT * FROM cds where " + param + " = '" + val + "';")
    ls = Gtk.ListStore(int, str, str)
    for row in db_edit:
        print(list(row))
        ls.append(list(row))

    view = Gtk.TreeView(model = ls)
    # for each column
    for i, column in enumerate(["ID", "Authors", "Title"]):
        # cellrenderer to render the text
        cell = Gtk.CellRendererText()
        # the text in the first column should be in boldface
        if i == 0:
            cell.props.weight_set = True
            cell.props.weight = Pango.Weight.BOLD
        # the column is created
        col = Gtk.TreeViewColumn(column, cell, text=i)
        # and it is appended to the treeview
        view.append_column(col)

    cont.attach(view, 0, 0, 6, 6)
    program.add(cont)
    program.show_all()


def find_itf(_, cont, db_edit, program):   #find interface
    cont.destroy()
    cont = Gtk.Grid()

    cb = Gtk.ComboBoxText()
    cb.append_text("Authors")
    cb.append_text("Title")
    cb.set_active(0)

    en = Gtk.Entry()
    confirm = Gtk.Button.new_with_label("Confirm")
    confirm.connect("clicked", find_res, cb, en, db_edit, cont, program)

    cont.attach(cb, 0, 0, 5, 2)
    cont.attach(en, 5, 0, 15, 2)
    cont.attach(confirm, 4, 2, 7, 2)

    program.add(cont)
    program.show_all()

def ins_res(_, db_edit, auth_en, title_en, cont, program):
    auth_data = auth_en.get_text()
    title_data = title_en.get_text()
    db_edit.execute("INSERT INTO cds (Authors, Title) values ('" + auth_data + "', '" + title_data + "');")
    fin_label = Gtk.Label("Operation succeeded!")
    cont.pack_start(fin_label, True, True, 5)
    program.show_all()
    db_edit.execute("SELECT * from cds")
    #for row in db_edit:
        #print(row)
    #zapisać!!!


def ins_itf(_, cont, db_edit, program): #insert interface
    cont.destroy()
    cont = Gtk.VBox()

    auth_lab = Gtk.Label("Insert author's nickname")
    title_lab = Gtk.Label("Insert CD's title")
    auth_en = Gtk.Entry()
    title_en = Gtk.Entry()
    confirm = Gtk.Button.new_with_label("Confirm")
    confirm.connect("clicked", ins_res, db_edit, auth_en, title_en, cont, program)

    cont.pack_start(auth_lab, True, True, 2)
    cont.pack_start(auth_en, True, True, 3)
    cont.pack_start(title_lab, True, True, 2)
    cont.pack_start(title_en, True, True, 3)
    cont.pack_start(confirm, True, True, 5)

    program.add(cont)
    program.show_all()


def main():
    db = db_connect()
    editor = db.cursor()

    program = Window("CD Database", db)
    cont = Gtk.Box()
    find = Gtk.Button.new_with_label("Find")
    find.connect("clicked", find_itf, cont, editor, program)
    add = Gtk.Button.new_with_label("Add")
    add.connect("clicked", ins_itf, cont, editor, program)
    cont.pack_start(find, True, True, 2)
    cont.pack_start(add, True, True, 2)

    editor.execute("SELECT Authors, Title from cds")
    for row in editor:
        print(row)

    program.add(cont)
    program.show_all()

    #combo box
    #może list store

main()
Gtk.main()