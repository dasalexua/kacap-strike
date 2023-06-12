import json

enemies = {
	"Мобік": {
		"health": 80,
		"damage": [3,8],
		"minlvl": 0,
		"maxlvl": 3
	},
	"Мобік Рів.2": {
		"health": 90,
		"damage": [3,11],
		"minlvl": 2,
		"maxlvl": 4
	},
	"Кацап": {
		"health": 100,
		"damage": [5,11],
		"minlvl": 3,
		"maxlvl": 10,
	},
	"Вагнерівець": {
		"health": 150,
		"damage": [8,13],
		"minlvl": 7,
		"maxlvl": 9,
	},
	"Досвідчений вагнерівець": {
		"health": 160,
		"damage": [9,15],
		"minlvl": 9,
		"maxlvl": 14,
	},
	"Бос: Прігожин": {
		"health": 200,
		"damage": [14,20],
		"minlvl": 15,
		"maxlvl": 15,
	},
	"Елітний вагнерівець": {
		"health": 190,
		"damage": [15,23],
		"minlvl": 16,
		"maxlvl": 20,
	},
	"Еліта ЗСрф": {
		"health": 250,
		"damage": [16,24],
		"minlvl": 17,
		"maxlvl": 19,
	},
	"Бос: Хуйло (путін)": {
		"health": 300,
		"damage": [20,27],
		"minlvl": 20,
		"maxlvl": 20,
	}
}

health = {
	"1": 100,
	"2": 100,
	"3": 105,
	"4": 110,
	"5": 115,
	"6": 120,
	"7": 130,
	"8": 140,
	"9": 155,
	"10": 175,
	"12": 180,
	"13": 180,
	"14": 195,
	"15": 200,
	"16": 210,
	"17": 230,
	"18": 250,
	"19": 275,
	"20": 300
}

damage = {
	"1": [5,9],
	"2": [5,9],
	"3": [5,9],
	"4": [5,10],
	"5": [6,11],
	"6": [7,12],
	"7": [8,13],
	"8": [9,14],
	"9": [10,16],
	"10": [10,17],
	"12": [10,18],
	"13": [10,20],
	"14": [12,20],
	"15": [15,20],
	"16": [17,21],
	"17": [17,23],
	"18": [18,24],
	"19": [20,24],
	"20": [21,26]
}


#Functions
def opendb():
	with open('data.json', 'r') as f: return json.load(f)

def savedb(data):
	with open('data.json', 'w') as f: json.dump(data,f,indent=4)

def change(db_name,db_value,db_type):
	data = opendb()
	if db_type == 0:
		data[db_name] = db_value
	if db_type == 1:
		data[db_name] += db_value
	if db_type == 2:
		data[db_name] -= db_value	
	savedb(data)