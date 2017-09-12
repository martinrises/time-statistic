class ItemRecord:
	def __init__(self, data_str):
		self.dataStr = data_str

	@property
	def dataStr(self):
		return self.__data_str

	@dataStr.setter
	def dataStr(self, data_str):
		temp = data_str.replace('，', ',').strip()
		self.__data_str = temp

	@property
	def datas(self):
		datas = self.dataStr.split(',')
		return list(map(lambda s: s.strip(), datas))

	@property
	def name(self):
		return self.datas[0]

	@property
	def category(self):
		return self.datas[1]

	@property
	def start(self):
		return self.datas[2]

	@property
	def end(self):
		return self.datas[3]

	@property
	def tags(self):
		return self.datas[4:]