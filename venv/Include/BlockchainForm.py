from tkinter import *
from tkinter.ttk import Frame, Label, Entry, Button
import tkinter.messagebox
import datetime as timehelper
from Block import Block

root = Tk()
blocks = []

# def update_listbox():
# 	#Clear the current list
# 	clear_chain()
# 	#Populate the listbox
# 	for task in tasks:
# 		lb_tasks.insert("end", task)
#
#
# def clear_chain():
# 	lb_tasks.delete(0, "end")

class BlockchainFrm(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(padx=5,pady=10)
        self.parent = parent
        self.initUI()
        self.isEdit = False
        self.index = 0

    def initUI(self):
        self.parent.title("Chain Of Block")
        self.pack(fill=X, expand=False)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        self.lbl2 = Label(frame2, text="Data", width=8)
        self.lbl2.pack(fill=X, side=LEFT, padx=3, pady=5)

        self.entry2 = Entry(frame2)
        self.entry2.pack(fill=X, side=LEFT, padx=2, expand=False)

        btnCheckValid = Button(frame2, text="Check", command=self.check_valid)
        btnCheckValid.pack(fill=X, side=RIGHT)

        self.edtBtn = Button(frame2, text="Edit Block", command=self.turn_on_edit)
        self.edtBtn.pack(fill=X, side=RIGHT)

        btnSave = Button(frame2, text="Add Block", command=self.add_block)
        btnSave.pack(fill=X,side=RIGHT)

        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=False)

        self.lstView = Listbox(frame3, width=1000)
        self.lstView.pack(side=BOTTOM, padx=2, pady=2)
        self.lstView.bind("<<ListboxSelect>>", self.onSelect)

    def turn_on_edit(self):
        if (self.isEdit):
            self.isEdit = False
            self.edtBtn.config(text='Edit Block')
            blocks[self.index].data = self.entry2.get()
            bl = blocks[self.index]
            self.lstView.delete(self.index)
            self.lstView.insert(self.index,str(bl.index) +'. ' +str(bl.data) + '   '  + str(bl.timestamp.strftime('%d/%m/%y %H:%M:%S'))+ '  ' + str(bl.hash))

            self.reload_chain()
        else:
            self.isEdit = True
            self.edtBtn.config(text='Save Change')
            self.entry2.delete(0,'end')



    def add_block(self):
        # Get the task to add
        data = self.entry2.get()
        num = len(blocks)
        if (len(blocks) == 0):
            bl = Block(num,data,'0')
        else:
            bl = Block(num, data, blocks[-1].hash)

        blocks.append(bl)

        self.reload_chain()

    def reload_chain(self):
        self.lstView.delete(0,'end')
        for i in blocks:
            self.lstView.insert(END,str(i.index) +'. ' +str(i.data) + '   '  + str(i.timestamp.strftime('%d/%m/%y %H:%M:%S')) + '  ' + str(i.hash))


    def onSelect(self, val):

        sender = val.widget
        self.index = sender.curselection()[0]
        if (self.isEdit):
            self.entry2.delete(0, 'end')
            self.entry2.insert(0, str(blocks[int(self.index)].data))

            self.entry2.focus()
        else:
            bl = blocks[self.index]
            rs = tkinter.messagebox.showinfo("Infomation",
                                             "Data: " + str(bl.data)
                                             + "\nCreateDate: " + str(bl.timestamp)
                                             + "\nKey: " + str(bl.hash)
                                             + "\nPrevious Key: " + str(bl.previous_hash))

    def checkValidKey(self):
        for i in range(1,len(blocks)-1):
            crrBl = blocks[i]
            prvBl = blocks[i-1]
            if (crrBl.hash != crrBl.hash_block()):
                return False
            if (crrBl.previous_hash != prvBl.hash):
                return False
        return True

    def check_valid(self):
        if self.checkValidKey():
            tkinter.messagebox.showinfo("Good Security","Nice Blockchain")
        else:
            tkinter.messagebox.showerror("ERRORRRRRRR!!!","Having Security Error")



root.geometry("550x200+200+300")
app = BlockchainFrm(root)
root.mainloop()