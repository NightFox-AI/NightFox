class Boardpos :
	def __init__(self):
		#self.a=[[0 for i in range(6,-1,-1)] for j in range(5,-1,-1)]
		self.a=[[0 for i in range(0,7)] for j in range(0,6)]
		#self.a[0][1]=1
		print("The format is ")
		print(" 0  1  2  3  4  5  6")
		
		"""
		self.a= [ 
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[1, 1, 0, 0, 1, 0, 0],
			[1, 2, 2, 2, 1, 2, 0],
			[2, 2, 2, 1, 1, 2, 1],
			[2, 1, 2, 2, 2, 2, 1],
			]
		"""
		for i in range(0,6):
			print(self.a[i])