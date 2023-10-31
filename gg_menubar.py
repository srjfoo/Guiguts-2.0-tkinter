# GGmenubar class is tk.Menu, used for main menubar
# Creates its child menus

import re
import tkinter as tk

from gg_menu import GGmenu
from gg_tkutils import isMac


class GGmenubar(tk.Menu):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.initFileMenu(root)
        self.initEditMenu(root)
        self.initViewMenu(root)
        self.initHelpMenu(root)
        self.initOSMenu(root)

    def initFileMenu(self, root):
        menu_file = GGmenu(self, "~File")
        menu_file.addButton("~Open...", root.openFile, "Cmd/Ctrl+O")
        menu_file.addButton("~Save", root.saveFile, "Cmd/Ctrl+S")
        menu_file.addButton("Save ~As...", root.saveasFile, "Cmd/Ctrl+Shift+S")
        menu_file.add_separator()
        menu_file.addButton("~Quit", root.quitProgram, "Cmd+Q" if isMac() else "")

    def initEditMenu(self, root):
        menu_edit = GGmenu(self, "~Edit")
        menu_edit.addButton("~Undo", "<<Undo>>", "Cmd/Ctrl+Z")
        menu_edit.addButton("~Redo", "<<Redo>>", "Cmd+Shift+Z" if isMac() else "Ctrl+Y")
        menu_edit.add_separator()
        menu_edit.addCutCopyPaste()
        menu_edit.add_separator()
        menu_edit.addButton("Select ~All", "<<SelectAll>>", "Cmd/Ctrl+A")
        menu_edit.add_separator()
        menu_edit.addButton("Pre~ferences...", root.showMyPreferencesDialog)

    def initViewMenu(self, root):
        menu_view = GGmenu(self, "~View")
        menu_view.addButton("~Dock", root.dockImage, "Cmd/Ctrl+D")
        menu_view.addButton("~Float", root.floatImage, "Cmd/Ctrl+F")
        menu_view.addButton("~Load Image", root.loadImage, "Cmd/Ctrl+L")

    def initHelpMenu(self, root):
        menu_help = GGmenu(self, "~Help")
        menu_help.addButton("Guiguts ~Manual", root.helpManual)
        menu_help.addButton("About ~Guiguts", root.helpAbout)

    def initOSMenu(self, root):
        if isMac():
            # Apple menu
            menu_app = GGmenu(self, "", name="apple")
            menu_app.addButton("About ~Guiguts", root.helpAbout)
            menu_app.add_separator()
            # Window menu
            menu_window = GGmenu(self, "Window", name="window")
        else:
            menu_app = None