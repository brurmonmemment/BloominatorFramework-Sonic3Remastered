import tkinter as GuiLib
from tkinter.filedialog import asksaveasfilename as SaveAsDialog, askopenfile as OpenDialog
from tkinter import Tk as GuiLibI, ttk as GuiWidget

Window   = GuiLibI()
MenuBar  = GuiLib.Menu(Window)
Notebook = GuiWidget.Notebook(Window)

Window.title("Scene Configuration Manager")
Window.geometry("848x480")

SceneData = {}

class File:
    @staticmethod
    def ExportSceneCfg():
        path = SaveAsDialog(defaultextension=".bin",
                            filetypes=[("Scene Configuration File", "SceneConfig.bin")])
        if not path:
            return

        with open(path, "wb") as SceneConfigBinary:
            Lines = [b"SceneConfig\x00\x00List\x00\x00"]

            for Category in SceneData:
                Lines.append(f"\x14\x14 {Category}\x00".encode())
                for Scene in SceneData[Category]:
                    Lines.append(f"\x14 {Scene[0]} - {Scene[1]}\x00".encode())

            for Line in Lines:
                SceneConfigBinary.write(Line)

    @staticmethod
    def OpenSceneCfg():
        OpenDialog(defaultextension=".bin",
                   filetypes=[("Scene Configuration File", "SceneConfig.bin")])

class Categories:
    @staticmethod
    def New():
        Popup = GuiLib.Toplevel(Window)
        Popup.title("New Category")

        GuiLib.Label(Popup,
                     text="Category Name:").pack()
        CatNameEntry = GuiLib.Entry(Popup)
        CatNameEntry.pack(pady=5)

        def AddCategory():
            CatName = CatNameEntry.get().strip()
            if not CatName or CatName in SceneData:
                Popup.destroy()
                return

            SceneData[CatName] = []

            NewTab = GuiWidget.Frame(Notebook)
            Notebook.add(NewTab,
                         text=CatName)
            Notebook.select(NewTab)

            SceneListFrame = GuiLib.Frame(NewTab)
            SceneListFrame.pack(pady=5,
                                fill="x")

            def AddSceneRow():
                Row = GuiLib.Frame(SceneListFrame)
                Row.pack(pady=2,
                         fill="x")

                SceneNameVar  = GuiLib.StringVar()
                FolderNameVar = GuiLib.StringVar()

                SceneNameEntry  = GuiLib.Entry(Row,
                                               textvariable=SceneNameVar,
                                               width=30,
                                               fg="grey")
                FolderNameEntry = GuiLib.Entry(Row,
                                               textvariable=FolderNameVar,
                                               width=40,
                                               fg="grey")

                SceneNameEntry.insert(0,
                                      "Scene Name")
                FolderNameEntry.insert(0,
                                       "Folder Name")

                def ClearPlaceholder(event, entry, var, text):
                    if var.get() == text:
                        entry.delete(0,
                                     "end")
                        entry.config(fg="black")

                def RestorePlaceholder(event, entry, var, text):
                    if var.get() == "":
                        entry.insert(0,
                                     text)
                        entry.config(fg="grey")

                SceneNameEntry.bind("<FocusIn>",
                                    lambda e: ClearPlaceholder(e, SceneNameEntry, SceneNameVar, "Scene Name"))
                SceneNameEntry.bind("<FocusOut>",
                                    lambda e: RestorePlaceholder(e, SceneNameEntry, SceneNameVar, "Scene Name"))

                FolderNameEntry.bind("<FocusIn>",
                                     lambda e: ClearPlaceholder(e, FolderNameEntry, FolderNameVar, "Folder Name"))
                FolderNameEntry.bind("<FocusOut>",
                                     lambda e: RestorePlaceholder(e, FolderNameEntry, FolderNameVar, "Folder Name"))

                SceneNameEntry.pack(side="left",
                                    padx=2)
                FolderNameEntry.pack(side="left",
                                     padx=2)

                RemoveButton = GuiLib.Button(Row,
                                             text="X",
                                             command=lambda: RemoveScene())
                RemoveButton.pack(side="left",
                                  padx=5)

                SceneData[CatName].append(["", ""])
                SceneIndex = len(SceneData[CatName]) - 1

                def UpdateScene(*_):
                    name   = SceneNameVar.get()
                    folder = FolderNameVar.get()
                    if name != "Scene Name":
                        SceneData[CatName][SceneIndex][0] = name.strip()
                    if folder != "Folder Name":
                        SceneData[CatName][SceneIndex][1] = folder.strip()

                def RemoveScene():
                    Row.destroy()
                    SceneData[CatName][SceneIndex] = None

                SceneNameVar.trace_add("write",
                                       UpdateScene)
                FolderNameVar.trace_add("write",
                                        UpdateScene)

            GuiLib.Button(NewTab,
                          text="Add Scene",
                          command=AddSceneRow).pack(pady=5)
            AddSceneRow()

            Popup.destroy()

        GuiLib.Button(Popup,
                      text="OK",
                      command=AddCategory).pack(pady=5)

Menu_File = GuiLib.Menu(MenuBar, tearoff=0)
Menu_File.add_command(label="Open Scene Config",
                      command=File.OpenSceneCfg)
Menu_File.add_command(label="Save As",
                      command=File.ExportSceneCfg)
Menu_File.add_command(label="Exit",
                      command=Window.quit)
MenuBar.add_cascade(label="File",
                    menu=Menu_File)

Menu_Categories = GuiLib.Menu(MenuBar,
                              tearoff=0)
Menu_Categories.add_command(label="New",
                            command=Categories.New)
MenuBar.add_cascade(label="Categories",
                    menu=Menu_Categories)

Window.config(menu=MenuBar)
Notebook.pack(padx=5, pady=5, fill="both", expand=True)
Window.mainloop()