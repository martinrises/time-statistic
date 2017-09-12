import re
from record import DayRecord

def get_daily_datas(path='log.txt'):

	datas = []
	with open(path, 'r', encoding='UTF-8') as f:
		lines = f.readlines()
		lines = list(filter(lambda line: line.strip() != '', lines))
		lines = list(map(lambda line: line[:len(line) - 1], lines))
		
		last_index = 0
		pattern = r"[0-9]+"
		for i in range(1, len(lines)):
			line = lines[i]
			match = re.match(pattern, line)
			if match is not None:
				datas.append(DayRecord(lines[last_index], lines[last_index + 1: i]))
				last_index = i
		datas.append(DayRecord(lines[last_index], lines[last_index + 1: len(lines)]))
	return datas

def get_minute(start, end):
	start_minute = int(start[0:2]) * 60 + int(start[2:4])
	end_minute = int(end[0:2]) * 60 + int(end[2:4])
	return end_minute - start_minute

def add_value(dict, key, value):
	key = str(key)
	v = dict.get(key)
	if v is None:
		dict[key] = value
	else:
		dict[key] = v + value

def statistic_daily(daily_records):
	for daily_record in daily_records:
		categories = {}
		issues = {}
		for item_record in daily_record.data:
			minute = get_minute(item_record.start, item_record.end)
			category = item_record.category
			name = item_record.name
			add_value(categories, category, minute)
			add_value(issues, name, minute)

		print(daily_record.date)
		print(categories)
		print(issues)

datas = get_daily_datas()
statistic_daily(datas)