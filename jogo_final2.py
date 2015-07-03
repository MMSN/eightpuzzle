#!/usr/bin/python
# -*- coding: utf-8 -*-

import puzzle
from Tkinter import *
import tkMessageBox as box

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
    			print 'inicio'
    		else:
    			traducao_vector = novo_vector.split(',')
    			#print traducao_vector
    			#print len(traducao_vector)
    			for i in range(len(traducao_vector)):
    				traducao_vector[i] = int(traducao_vector[i])
    				if traducao_vector[i] == 0:
    					traducao_vector[i] = 9
    			#print traducao_vector
    		#print novo_vector
    		self.vector_inicial = traducao_vector
    	if len(self.setar_final.get()) > 9 and len(self.setar_final.get()) < 18:
    		novo_vector = self.setar_final.get()
    		if novo_vector == '':
    			print 'final'
    		else:
    			traducao_vector = novo_vector.split(',')
    			#print traducao_vector
    			#print len(traducao_vector)
    			for i in range(len(traducao_vector)):
    				traducao_vector[i] = int(traducao_vector[i])
    				if traducao_vector[i] == 0:
    					traducao_vector[i] = 9
    		#print novo_vector
    		self.vector_final = traducao_vector
    		
class Example2(Frame):
  
    def __init__(self, parent, tabuleiro):
        Frame.__init__(self, parent)   
        
        self.target = [[0,0,0,0,0],[0,1,2,3,0],[0,4,5,6,0],[0,7,8,9,0],[0,0,0,0,0]]
        self.mesa = tabuleiro
        self.table = None
        self.celula_branca = None
        self.ordem = []
        self.ordemX = None
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Eight Puzzle")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        
        #self.table = self.mesa.shuffle()
        self.table = self.mesa.vector
        #print self.table
        
        img = PhotoImage(file="red1gif.gif")
        cmd1 = lambda: self.opt_1()
    	self.button1 = Button(canvas, image=img, command = cmd1)
    	self.button1.img = img  # store a reference to the image as an attribute of the widget
    	#self.button1.grid(row=1, column=1)
        
        img2 = PhotoImage(file="red2gif.gif")
        cmd2 = lambda: self.opt_2()
    	self.button2 = Button(canvas, image=img2, command = cmd2)
    	self.button2.img = img2  # store a reference to the image as an attribute of the widget
    	#self.button2.grid(row=1, column=2)
        
        img3 = PhotoImage(file="red3gif.gif")
        cmd3 = lambda: self.opt_3()
    	self.button3 = Button(canvas, image=img3, command = cmd3)
    	self.button3.img = img3  # store a reference to the image as an attribute of the widget
    	#self.button3.grid(row=1, column=3)
    	
    	img4 = PhotoImage(file="red4gif.gif")
    	cmd4 = lambda: self.opt_4()
    	self.button4 = Button(canvas, image=img4, command = cmd4)
    	self.button4.img = img4  # store a reference to the image as an attribute of the widget
    	#self.button4.grid(row=2, column=1)
    	
    	img5 = PhotoImage(file="red5gif.gif")
    	cmd5 = lambda: self.opt_5()
    	self.button5 = Button(canvas, image=img5, command = cmd5)
    	self.button5.img = img5  # store a reference to the image as an attribute of the widget
    	#self.button5.grid(row=2, column=2)
    	
    	img6 = PhotoImage(file="red6gif.gif")
    	cmd6 = lambda: self.opt_6()
    	self.button6 = Button(canvas, image=img6, command = cmd6)
    	self.button6.img = img6  # store a reference to the image as an attribute of the widget
    	#self.button6.grid(row=2, column=3)
    	
    	img7 = PhotoImage(file="red7gif.gif")
    	cmd7 = lambda: self.opt_7()
    	self.button7 = Button(canvas, image=img7, command = cmd7)
    	self.button7.img = img7  # store a reference to the image as an attribute of the widget
    	#self.button7.grid(row=3, column=1)
    	
    	img8 = PhotoImage(file="red8gif.gif")
    	cmd8 = lambda: self.opt_8()
    	self.button8 = Button(canvas, image=img8, command = cmd8)
    	self.button8.img = img8  # store a reference to the image as an attribute of the widget
    	#self.button8.grid(row=3, column=2)
    	
    	img9 = PhotoImage(file="brancogif.gif")
    	self.button9 = Button(canvas, image=img9)
    	self.button9.img = img9  # store a reference to the image as an attribute of the widget
    	#self.button9.grid(row=3, column=3)
    	
    	aux2 = []
        for i in range(1, 4):
        	for j in range(1, 4):
        		if self.table[i][j] == 1:
        			self.button1.grid(row=i, column=j)
        			self.ordem.append(1)
        		elif self.table[i][j] == 2:
        			self.button2.grid(row=i, column=j)
        			self.ordem.append(2)
        		elif self.table[i][j] == 3:
        			self.button3.grid(row=i, column=j)
        			self.ordem.append(3)
        		elif self.table[i][j] == 4:
        			self.button4.grid(row=i, column=j)
        			self.ordem.append(4)
        		elif self.table[i][j] == 5:
        			self.button5.grid(row=i, column=j)
        			self.ordem.append(5)
        		elif self.table[i][j] == 6:
        			self.button6.grid(row=i, column=j)
        			self.ordem.append(6)
        		elif self.table[i][j] == 7:
        			self.button7.grid(row=i, column=j)
        			self.ordem.append(7)
        		elif self.table[i][j] == 8:
        			self.button8.grid(row=i, column=j)
        			self.ordem.append(8)
        		else:
        			self.ordemX = len(self.ordem)
        			self.ordem.append(9)
        			aux2.append(i)
        			aux2.append(j)
        			self.celula_branca = aux2
        			#print self.celula_branca
        			self.button9.grid(row=i, column=j)
        
        """
        square1 = canvas.create_rectangle(30, 10, 120, 80, 
            outline="#fb0", fill="#fb0")
        square2 = canvas.create_rectangle(150, 10, 240, 80, 
            outline="#f50", fill="#f50")
        square3 = canvas.create_rectangle(270, 10, 370, 80, 
            outline="#05f", fill="#05f")
        
        square4 = canvas.create_rectangle(30, 100, 120, 170, 
            outline="#fb0", fill="#fb0")
        square5 = canvas.create_rectangle(150, 100, 240, 170, 
            outline="#f50", fill="#f50")
        square6 = canvas.create_rectangle(270, 100, 370, 170, 
            outline="#05f", fill="#05f")
               
        square7 = canvas.create_rectangle(30, 190, 120, 260, 
            outline="#fb0", fill="#fb0")
        square8 = canvas.create_rectangle(150, 190, 240, 260, 
            outline="#f50", fill="#f50")
        square9 = canvas.create_rectangle(270, 190, 370, 260, 
            outline="#05f", fill="#05f")       
        """
        canvas.pack(fill=BOTH, expand=1)
        
    def opt_1(self):
    	self.movement(1)
    	
    def opt_2(self):
    	self.movement(2)
    	
    def opt_3(self):
    	self.movement(3)
    	
    def opt_4(self):
    	self.movement(4)
    	
    def opt_5(self):
    	self.movement(5)
    	
    def opt_6(self):
    	self.movement(6)
    	
    def opt_7(self):
    	self.movement(7)
    	
    def opt_8(self):
    	self.movement(8)
        
    def movement(self, x):
    	tentativa = self.mesa.test_adj(x)
    	if tentativa == True:
    		#print 'True'
    		aux = []
    		for i in range(1,4):
    			for j in range(1,4):
    				if self.table[i][j] == x:
    					aux.append(i)
    					aux.append(j)
    		#print 'aux',aux
    		#print self.ordem
    		#print self.ordemX
    		
    		for k in range(len(self.ordem)):
    			if self.ordem[k] == x:
    				if self.ordem[k] == 1:
    					self.button1.grid(row=self.celula_branca[0], column=self.celula_branca[1])
    					self.button9.grid(row=aux[0], column=aux[1])
    				elif self.ordem[k] == 2:
    					self.button2.grid(row=self.celula_branca[0], column=self.celula_branca[1])
    					self.button9.grid(row=aux[0], column=aux[1])
    				elif self.ordem[k] == 3:
    					self.button3.grid(row=self.celula_branca[0], column=self.celula_branca[1])
    					self.button9.grid(row=aux[0], column=aux[1])
    				elif self.ordem[k] == 4:
    					self.button4.grid(row=self.celula_branca[0], column=self.celula_branca[1])
    					self.button9.grid(row=aux[0], column=aux[1])
    				elif self.ordem[k] == 5:
    					self.button5.grid(row=self.celula_branca[0], column=self.celula_branca[1])
    					self.button9.grid(row=aux[0], column=aux[1])
    				elif self.ordem[k] == 6:
    					self.button6.grid(row=self.celula_branca[0], column=self.celula_branca[1])
    					self.button9.grid(row=aux[0], column=aux[1])
    				elif self.ordem[k] == 7:
    					self.button7.grid(row=self.celula_branca[0], column=self.celula_branca[1])
    					self.button9.grid(row=aux[0], column=aux[1])
    				elif self.ordem[k] == 8:
    					self.button8.grid(row=self.celula_branca[0], column=self.celula_branca[1])
    					self.button9.grid(row=aux[0], column=aux[1])

    					
    				self.celula_branca = aux
    				#print 'celula branca',self.celula_branca
    				self.ordem[k] = 9
    				#print 'ordem',self.ordem[k]
    				self.ordem[self.ordemX]=x
    				self.ordemX=k
    				#print 'ordem',self.ordem,self.ordemX
    				break
    		self.mesa.movement(x,1)
    		
    		if self.mesa.vector == self.target:
    			#print "Mateus"
    			box.showinfo(
        		"Eight Puzzle", 
        		"Parabens, voce solucionou o jogo!"
        		)
        		exit(0)
    		
    	else:
    		print 'False'
        
    def key(self, event):
        print "pressed", repr(event.char)
        if event.char == 's':
        	print 'solving'
        	answer = self.mesa.breadth()
        	#box.showinfo("Information", "Download completed")
        	decisao = box.askquestion(
            "Eight Puzzle",
            "Solução: %s. \n Deseja ver caminhos testados?" % answer
        	)
        	print decisao
        	if decisao == 'yes':
        		box.showinfo(
        		"Eight Puzzle", 
        		"%s" % self.mesa.vector_breadth_used
        		)
        if event.char == 'd':
        	print 'solving'
        	self.mesa.pre_deep()
        	answer = self.mesa.deep()
        	#box.showinfo("Information", "Download completed")
        	decisao = box.askquestion(
            "Eight Puzzle",
            "Solução: %s. Demais solucoes %s\n Deseja ver caminhos testados?" % answer
        	)
        	if decisao == 'yes':
        		box.showinfo(
        		"Eight Puzzle", 
        		"%s" % self.mesa.vector_tried
        		)


    def callback(self, event):
        self.focus_set()
        print "clicked at", event.x, event.y

def main():
    
    root = Tk()
    root.geometry("270x100+300+300")
    app = Example(root)
    root.mainloop()
    
    print app.vector_inicial
    print app.vector_final
    
    mesa = puzzle.table()
    
    if app.vector_inicial != None:
    	if app.vector_final != None: 
    		if app.vector_inicial != app.vector_final:
    			print 'setar 2'
    			mesa.set_vector(app.vector_inicial)
    			mesa.set_target(app.vector_final)
    	else:
    		mesa.set_vector(app.vector_inicial)
    elif app.vector_final != None:
    	mesa.set_target(app.vector_final)
    	mesa.shuffle()
    #elif app.vector_inicial == None and app.vector_final == None:
    else:
    	print 'ola'
    	mesa.shuffle()
    	
    	
    root2 = Tk()
    ex = Example2(root2, mesa)
    root2.geometry("306x350+300+300")
    #root = Frame(root, width=600, height=600)
    root2.bind("<Key>", ex.key)
    #root.bind("<Button-1>", ex.callback)
    #root.pack()
    root2.mainloop()
    
    



if __name__ == '__main__':
    main()  