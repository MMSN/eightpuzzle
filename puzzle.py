import random


class table():

    def __init__(self):
        self.vector = [[0,0,0,0,0],[0,1,2,3,0],[0,4,5,6,0],[0,7,8,9,0],[0,0,0,0,0]]
        self.target = [[0,0,0,0,0],[0,1,2,3,0],[0,4,5,6,0],[0,7,8,9,0],[0,0,0,0,0]]
        self.clone = [[0,0,0,0,0],[0,1,2,3,0],[0,4,5,6,0],[0,7,8,9,0],[0,0,0,0,0]]
        self.missing_x = 3
        self.missing_y = 3
        self.wrong = 0
        self.wrong_vector = []
        self.wrong_dist = []
        self.vector_breadth = []
        self.vector_tried = []
        self.vector_exausted = []
        self.vector_breadth_used = []
        self.solucao_breadth = None
        self.solucao_deep = None
        self.solucoes_deep = []

    def shuffle(self):
        num_swap = random.randint(20, 41)
        #print str(num_swap)+'\n'
        
        for i in range(num_swap):
        	direction_swap = random.randint(1, 4)
        	if direction_swap == 1:
        		if self.vector[self.missing_x-1][self.missing_y] != 0:
        			#print self.vector[self.missing_x-1][self.missing_y]
        			swap_num = self.vector[self.missing_x-1][self.missing_y]
        			self.vector[self.missing_x-1][self.missing_y] = self.vector[self.missing_x][self.missing_y]
        			self.vector[self.missing_x][self.missing_y] = swap_num
        			self.missing_x = self.missing_x - 1
        	elif direction_swap == 2:
        		if self.vector[self.missing_x][self.missing_y-1] != 0:
        			self.vector[self.missing_x-1][self.missing_y]
        			swap_num = self.vector[self.missing_x][self.missing_y-1]
        			self.vector[self.missing_x][self.missing_y-1] = self.vector[self.missing_x][self.missing_y]
        			self.vector[self.missing_x][self.missing_y] = swap_num
        			self.missing_y = self.missing_y - 1
        	elif direction_swap == 3:
        		if self.vector[self.missing_x+1][self.missing_y] != 0:
        			self.vector[self.missing_x-1][self.missing_y]
        			swap_num = self.vector[self.missing_x+1][self.missing_y]
        			self.vector[self.missing_x+1][self.missing_y] = self.vector[self.missing_x][self.missing_y]
        			self.vector[self.missing_x][self.missing_y] = swap_num
        			self.missing_x = self.missing_x + 1
        	elif direction_swap == 4:
        		if self.vector[self.missing_x][self.missing_y+1] != 0:
        			self.vector[self.missing_x-1][self.missing_y]
        			swap_num = self.vector[self.missing_x][self.missing_y+1]
        			self.vector[self.missing_x][self.missing_y+1] = self.vector[self.missing_x][self.missing_y]
        			self.vector[self.missing_x][self.missing_y] = swap_num
        			self.missing_y = self.missing_y + 1
        
        self.clone = self.vector
        if self.vector == self.target:
        	self.shuffle()
        else:
        	return self.vector
    
    def movement(self,x, clone_num):
    	#print x
    	aux = []
    	if self.test_adj(x) == True:
	        swap_movement_x = 0
	        swap_movement_y = 0
	        for i in range(len(self.vector)):
	    	    for j in range(len(self.vector[i])):
	    			if self.vector[i][j] == int(x):
	    				swap_movement_x = i
	    				swap_movement_y = j
	    				aux.append(swap_movement_x)
	    				aux.append(swap_movement_y)
	    	aux = self.vector[swap_movement_x][swap_movement_y]
	    	self.vector[swap_movement_x][swap_movement_y] = self.vector[self.missing_x][self.missing_y]
	    	self.vector[self.missing_x][self.missing_y] = aux
	    	self.missing_x = swap_movement_x
	    	self.missing_y = swap_movement_y
	    	#print 'coor',self.missing_x,self.missing_y
    	if clone_num == int(1):
    		self.clone = self.vector
    	return aux
    
    def test_adj(self,x):
    	if self.vector[self.missing_x+1][self.missing_y] == int(x):
    		return True
    	elif self.vector[self.missing_x-1][self.missing_y] == int(x):
    		return True
    	elif self.vector[self.missing_x][self.missing_y+1] == int(x):
    		return True
    	elif self.vector[self.missing_x][self.missing_y-1] == int(x):
    		return True
    	else:
    		return False
    
    def find_coor(self, num, which):
    	for i in range(1,4):
		    for j in range(1,4):
		    	if self.target[i][j] == int(num):
		    		if which == int(1):
		    			return i
		    		else:
		    			return j
    
    def measure(self):
    	for i in range(1,4):
    		for j in range(1,4):
    			if self.vector[i][j] < 9:
    				if self.vector[i][j] != self.target[i][j]:
    					self.wrong = self.wrong + 1
    					self.wrong_vector.append(self.vector[i][j])
    					real_x = self.find_coor(self.vector[i][j], 1)
    					real_y = self.find_coor(self.vector[i][j], 2)
    					#print i,j,real_x,real_y
    					#print self.wrong, self.wrong_vector
    
    def print_table(self):
    	#for i in range(len(self.vector)):
    		#print self.vector[i]
    		#for j in range(len(self.vector[i])):
    		#	print self.vector[i][j]
    	for i in range(1,4):
    		printable = []
    		for j in range(1,4):
    			printable.append(self.vector[i][j])
    			#print self.vector[i][j]
    		print printable
    
    def possibilities(self, x):
    	
    	if self.vector[self.missing_x+1][self.missing_y] != 0 and self.vector[self.missing_x+1][self.missing_y] != int(x):
    		aux = []
    		#aux.append('D')
    		aux.append(self.vector[self.missing_x+1][self.missing_y])
    		self.vector_breadth.append(aux)
    	
    	if self.vector[self.missing_x-1][self.missing_y] != 0 and self.vector[self.missing_x-1][self.missing_y] != int(x):
    		aux = []
    		#aux.append('U')
    		aux.append(self.vector[self.missing_x-1][self.missing_y])
    		self.vector_breadth.append(aux)
    	
    	if self.vector[self.missing_x][self.missing_y+1] != 0 and self.vector[self.missing_x][self.missing_y+1] != int(x):
    		aux = []
    		#aux.append('R')
    		aux.append(self.vector[self.missing_x][self.missing_y+1])
    		self.vector_breadth.append(aux)
    	
    	if self.vector[self.missing_x][self.missing_y-1] != 0 and self.vector[self.missing_x][self.missing_y-1] != int(x):
    		aux = []
    		#aux.append('L')
    		aux.append(self.vector[self.missing_x][self.missing_y-1])
    		self.vector_breadth.append(aux)
    	

    
    def breadth(self):
    	kml = 0
    	self.possibilities(0)
    	#print self.vector_breadth
    	i = 0
    	#while kml < 5:
    	while len(self.vector_breadth) > 0:
    		for j in range(len(self.vector_breadth)):
    			aux = []
    			#print j
    			#print "NOVA TENTATIVA"+str(self.vector_breadth[0])
    			self.vector_breadth_used.append(self.vector_breadth[0])
    			for i in range(len(self.vector_breadth[0])):
    				#print self.vector_breadth[0][i]
    				self.movement(self.vector_breadth[0][i], 0)
    				#self.print_table()
    			if self.vector == self.target:
    				for i in range(1,len(self.vector_breadth[0])+1):
    					#print "DESFAZER",self.vector_breadth[0][-i]
    					self.movement(self.vector_breadth[0][-i], 0)
    				self.solucao_breadth = self.vector_breadth[0]
    				print 'solucao breadth',self.solucao_breadth
    				return self.solucao_breadth
    			else:
    				for i in range(1,len(self.vector_breadth[0])+1):
    					#print "DESFAZER",self.vector_breadth[0][-i]
    					self.movement(self.vector_breadth[0][-i], 0)
    				aux.append(self.vector_breadth[0][0])
    				self.vector_tried.append(self.vector_breadth[0])
    				self.vector_breadth.pop(0)
				#print 'TENTADOS'+str(self.vector_tried)
				#print 'POSSIBILIDADES'+str(self.vector_breadth)				
			if len(self.vector_breadth) == 0 and len(self.vector_tried) > 0:
				self.vector = self.clone
				#print str(self.vector_tried[0])+'reverse'
				aux_num = self.vector_tried[0]
				#print str(aux_num)+'aux num'
				self.vector_tried.pop(0)
				#print aux_num[0]
				for l in range(len(aux_num)):
					#print "AQUI"+str(aux_num[l])
					self.movement(aux_num[l], 0)
				self.possibilities(aux_num[-1])
				for l in range(1,len(aux_num)+1):
					#print "AQUI"+str(aux_num[l])
					self.movement(aux_num[-l], 0)
				#print 'NOVO BREADTH'+str(self.vector_breadth)
				#print 'aux num'+str(aux_num)
				for l in range(len(self.vector_breadth)):
					self.vector_breadth[l] = aux_num + self.vector_breadth[l]
					#print self.vector_breadth[l]
				#print self.vector_breadth
    		kml = kml + 1
    		
    def pre_deep(self):
    	self.possibilities(0)
    	
    def deep(self):
		asdf = 0
		#print self.vector_breadth
		while len(self.vector_breadth) > 0:
			
			for i in range(len(self.vector_breadth[0])):
				self.movement(self.vector_breadth[0][i], 0)
				#self.print_table()
			if self.vector == self.target:
				#print 'lex'
				if self.solucao_deep == None:
					self.solucao_deep = self.vector_breadth[0]
				else:
					if len(self.vector_breadth[0]) < len(self.solucao_deep):
						self.solucoes_deep.append(self.solucao_deep)
						self.solucao_deep = self.vector_breadth[0]
					else:
						self.solucoes_deep.append(self.vector_breadth[0])
				#return True
			#else:
			#print 'patriota',self.vector_breadth[0][0]
			patriota = self.vector_breadth[0]
			aux = []
			for i in range(1,len(self.vector_breadth)):
				aux.append(self.vector_breadth[i])
			self.vector_breadth = []
			self.vector_breadth.append(patriota)
			#print 'aux',aux
			self.possibilities(self.vector_breadth[0][-1])
			for i in range(len(self.vector_breadth)):
				if i > 0:
					self.vector_breadth[i] = self.vector_breadth[0] + self.vector_breadth[i]
						
			for i in range(1,len(self.vector_breadth[0])+1):
				self.movement(self.vector_breadth[0][-i], 0)
				#self.print_table()
			self.vector_tried.append(self.vector_breadth[0])
			self.vector_breadth.pop(0)
			self.vector_breadth = self.vector_breadth + aux
			#print 'vector breadth',self.vector_breadth
			#print 'vector tried',self.vector_tried
			#print 'novo patriota',self.vector_breadth[0]
			#print 'len novo patriota',len(self.vector_breadth[0])
			aux2 = []
			for i in range(len(self.vector_breadth)):
				if len(self.vector_breadth[i]) > 12:
					self.vector_exausted.append(self.vector_breadth[i])
				else:
					aux2.append(self.vector_breadth[i])
			self.vector_breadth = []
			self.vector_breadth = aux2
			#print 'vector exausted',self.vector_exausted
			#print 'vector breadth',self.vector_breadth
				
			asdf = asdf + 1
		print 'melhor solucao',self.solucao_deep
		print 'demais solucoes',self.solucoes_deep
		return self.solucao_deep

    def check_vector(self, vector):
	    num_changes = 0
	    n = 0
	    for i  in range(len(vector)):
	        n = i
	        while n < len(vector):
	            if vector[n]> 0 and vector[n] < 9 and vector[i] != 9:
	                if vector[i] > vector[n]:
	                    num_changes = num_changes + 1
	            n = n + 1
        
		print num_changes
	    if num_changes%2 == 0:
	        #print 'par'
	        return True
	    else:
	        #print 'impar'
	        return False

    def set_vector(self, vector):
		par_impar = self.check_vector(vector)
		if par_impar == True:
			aux = 0
			for i in range(1,4):
				for j in range(1,4):
					if vector[aux] == 9:
						self.missing_x = i
						self.missing_y = j
					self.vector[i][j] = vector[aux]
					aux = aux + 1
			self.clone = self.vector
			print self.vector
			print self.clone
			print self.missing_x
			print self.missing_y
			return True
		else:
			return False

    def set_target(self, vector):
    	par_impar = self.check_vector(vector)
    	if par_impar == True:
			aux = 0
			for i in range(1,4):
				for j in range(1,4):
					self.target[i][j] = vector[aux]
					aux = aux + 1
			print self.target
			return True
    	else:
			return False

	    		
    	
    	
if __name__ == "__main__":
	tabuleiro = table()
	tabuleiro.shuffle()
	tabuleiro.measure()
	tabuleiro.print_table()
	gate = True
	while gate == True:
		command = raw_input()
		true_command = command.split()
		if true_command[0] == 'exit' or true_command[0] == 'quit':
			gate = False
		elif true_command[0] == 'mov':
			#print 'Change'
			if true_command[1] != 9:
				#print 'Change2'
				tabuleiro.movement(true_command[1], 1)
		elif true_command[0] == 'solve':
			tabuleiro.breadth()
		elif true_command[0] == 'deep':
			tabuleiro.pre_deep()
			tabuleiro.deep()
		elif true_command[0] == 'set':
			if true_command[1] == 'vector':
				n = 0
				aux = []
				while n < 9:
					number = int(raw_input())
					aux.append(number)
					n = n + 1
				tabuleiro.set_vector(aux)
			elif true_command[1] == 'target':
				n = 0
				aux = []
				while n < 9:
					number = int(raw_input())
					aux.append(number)
					n = n + 1
				tabuleiro.set_target(aux)
		print 'Done'
		tabuleiro.print_table()
		if tabuleiro.vector == tabuleiro.target:
			print 'You have solved the puzzle!'
			gate = False
		