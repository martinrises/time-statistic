from item_record import ItemRecord

class DayRecord:
	def __init__(self, date, data_strs):
		self.date = date
		self.data_strs = data_strs
		self.__data = []

	@property
	def data(self):
		if len(self.__data) == 0:
			for data_str in self.data_strs:
				self.__data.append(ItemRecord(data_str))
		return self.__data