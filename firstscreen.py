#!/usr/bin/python
# -*- coding: utf-8 -*-


from Tkinter import *


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.vector_inicial = None
        self.vector_final = None
        self.initUI()
        
    def initUI(self):
    	self.parent.title("Eight Puzzle")        
        self.pack(fill=BOTH, expand=1)
        
        self.label_inicio = Label(self, text="Valor inicial")
        self.label_inicio.grid(column=0,row=0,sticky='W')
        
        self.label_final = Label(self, text="Valor final")
        self.label_final.grid(column=0,row=1,sticky='W')
        
        self.setar_inicio = Entry(self)
        self.setar_inicio.grid(column=1,row=0,sticky='EW')
        
        self.setar_final = Entry(self)
        self.setar_final.grid(column=1,row=1,sticky='EW')
        
        cmd1 = lambda: self.set_values()
        self.button_set = Button(self, text=u'Setar Valores', command = cmd1)
        self.button_set.grid(column=0,row=2,sticky='EW')
        
        cmd2 = lambda: self.hide_app()
        self.button_iniciar = Button(self, text=u'Iniciar', command = cmd2)
        self.button_iniciar.grid(column=1,row=2,sticky='EW')
        
    def hide_app(self):
    	#self.pack_forget()
    	#self.parent.withdraw()
    	self.parent.destroy()
    
    def set_values(self):
    	if len(self.setar_inicio.get()) > 9 and len(self.setar_inicio.get()) < 18:
    		novo_vector = self.setar_inicio.get()
    		if novo_vector == '':
    			print 'joao1'
    		else:
    			traducao_vector = novo_vector.split(',')
    			print traducao_vector
    			print len(traducao_vector)
    			for i in range(len(traducao_vector)):
    				traducao_vector[i] = int(traducao_vector[i])
    				if traducao_vector[i] == 0:
    					traducao_vector[i] = 9
    			print traducao_vector
    		print novo_vector
    		self.vector_inicial = traducao_vector
    	if len(self.setar_final.get()) > 9 and len(self.setar_final.get()) < 18:
    		novo_vector = self.setar_final.get()
    		if novo_vector == '':
    			print 'joao2'
    		else:
    			traducao_vector = novo_vector.split(',')
    			print traducao_vector
    			print len(traducao_vector)
    			for i in range(len(traducao_vector)):
    				traducao_vector[i] = int(traducao_vector[i])
    				if traducao_vector[i] == 0:
    					traducao_vector[i] = 9
    		print novo_vector
    		self.vector_final = traducao_vector
    	

def main():
  
    root = Tk()
    root.geometry("270x100+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  