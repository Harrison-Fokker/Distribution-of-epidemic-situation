import os

class InSpect():
	def __init__(self,dirs):
		try:
			os.makedirs(dirs)
		except:
			pass
		else:
			pass
