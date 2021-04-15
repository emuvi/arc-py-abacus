import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.upload = tk.Button(self, text="Upload")
        self.upload.pack(side=tk.TOP)
        self.list = tk.Listbox(self)
        self.list.pack(side=tk.LEFT, fill=tk.BOTH)
        for values in range(100): 
            self.list.insert(tk.END, values) 
        self.scroll = tk.Scrollbar(self)
        self.scroll.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.list.config(yscrollcommand = self.scroll.set)
        self.scroll.config(command = self.list.yview)
        self.download = tk.Button(self, text="Download")
        self.download.pack(side=tk.BOTTOM)
        

        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side=tk.BOTTOM)

    def say_hi(self):
        print("hi there, everyone!")

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("Abacus")
    root.eval('tk::PlaceWindow . center')
    app = Application(master=root)
    app.mainloop()