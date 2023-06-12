import random
import sys
import time
from config import *

#Кацап
Enemy_Name = "**MISSING КАЦАП**"
Enemy_HP = 666
Enemy_Damage = [0,0]
Enemy_Crit = 2
Enemy_Freezed = False

#Ви
Level = 1
HP = 100
Damage = [5,9]
Crit = 2

def stat():
	print("\n")
	print(
		f"Ви:\n"
		f" ♥{HP}\n"
		f"{Enemy_Name}:\n"
		f" ♥{Enemy_HP}\n"
	)

def start():
	global HP
	global Level
	global Damage
	data = opendb()
	if not "level" in data: change("level",0,0)
	if not "freeze" in data: change("freeze",0,0)
	data = opendb()
	Level = data["level"]
	if Level > len(health.keys()):
		input("Ви повністю пройшли цю \"гру\"! ")
		sys.exit()
	HP = health[str(Level)]
	Damage = damage[str(Level)]

def attack():
	for _ in range(10): print("\n")
	global Enemy_HP
	if random.randint(1,3) == 3 and not Enemy_Freezed:
		print(f"\n! {Enemy_Name} уклонився від вашої атаки")
	else:
		if random.randint(1,5) == 3:
			dmg = random.randint(int(Damage[0]*Crit),int(Damage[1]*Crit))
			Enemy_HP -= dmg
			print(f"\n> Ви сильно вдарили {Enemy_Name}!")
		else:
			dmg = random.randint(Damage[0],Damage[1])
			Enemy_HP -= dmg
			print(f"\n> Ви вдарили {Enemy_Name}!")


def hurt():
	global HP
	if random.randint(1,3) == 3:
		print(f"\n> Ви уклонилися від атаки {Enemy_Name}")
	else:
		if random.randint(1,5) == 3:
			dmg = random.randint(int(Enemy_Damage[0]*Enemy_Crit),int(Enemy_Damage[1]*Enemy_Crit))
			HP -= dmg
			print(f"\n!! Вас сильно вдарив {Enemy_Name}!")
		else:
			dmg = random.randint(Enemy_Damage[0],Enemy_Damage[1])
			HP -= dmg
			print(f"\n! {Enemy_Name} вдарив вас!")


def win():
	global Level
	global HP
	global Damage
	change("level",1,1)
	data = opendb()
	Level = data["level"]
	if Level > len(health.keys()):
		input("Ви перемогли і пройшли цю \"гру\"! ")
		sys.exit()
	HP = health[str(Level)]
	Damage = damage[str(Level)]
	if random.randint(1,4) == 2:
		change("freeze",1,1)
		print("\n! Ви знайшли: Обморожуючий предмет х1")
	

def defeat():
	global Level
	global HP
	global Damage
	HP = health[str(Level)]
	Damage = damage[str(Level)]

def new_enemy():
	global Enemy_Name
	global Enemy_HP
	global Enemy_Damage
	global Enemy_Freezed
	Enemy_Freezed = False
	rndenemies = []
	for enemy in enemies:
		if enemies[enemy]["minlvl"] <= Level and enemies[enemy]["maxlvl"] >= Level:
			rndenemies.append(enemy)
	try:
		rndenemy = random.choice(rndenemies)
		Enemy_Name = rndenemy
		Enemy_HP = enemies[rndenemy]["health"]
		Enemy_Damage = enemies[rndenemy]["damage"]
	except: pass
	print(Enemy_Name + " з'явився!\n")
	time.sleep(3)


start()
new_enemy()
while True:
	data = opendb()
	print(
		f"## {Enemy_Name} ##\n"
		"0 - Пропустити хід\n"
		"1 - Атакувати\n"
		"2 - Обійняти\n"
		f"3 - Обморозити (Залишилося {data['freeze']})"
	)
	act = input("Ваш вибір: ")

	if act == "1":
		attack()
		time.sleep(1)
		if Enemy_Freezed:
			print(f"\n! {Enemy_Name} не може вас атакувати")
		else:
			hurt()
	elif act == "2":
		if Enemy_Freezed:
			print(f"\n> Ви підішли до {Enemy_Name} і обійняли його, від цього він разморозився і вдарив вас")
			Enemy_Freezed = False
			HP -= Enemy_Damage[0]
		else:
			print(f"\n> Ви спробували наблизитись до {Enemy_Name}, але він вас вдарив.")
			HP -= Enemy_Damage[0]
	elif act == "3":
		if data["freeze"] > 0:
			if not Enemy_Freezed:
				print(f"\n> Ви заморозили {Enemy_Name}, тепер він не зможе вас атакувати")
				change("freeze",1,2)
				Enemy_Freezed = True
				Enemy_HP -= 1
			else:
				print(f"⨉ {Enemy_Name} вже заморожений!")
		else:
			print("\n⨉ У вас немає обморожуючих предметів!")
	else:
		if Enemy_Freezed:
			print(f"\n! {Enemy_Name} не може вас атакувати")
		else:
			hurt()
		time.sleep(1)
		print(f"\n> Ви нічого не зробили")

	time.sleep(1.5)

	if Enemy_Freezed and random.randint(1,6) == 3:
		print(f"\n! {Enemy_Name} розморозився!")
		Enemy_Freezed = False
	if Enemy_HP < 1:
		print(f"\n✓ {Enemy_Name}а переможено!")
		win()
		time.sleep(2)
		new_enemy()
	elif HP < 1:
		print("\n☠ Ви померли...")
		defeat()
		time.sleep(2)
		new_enemy()
	else:
		stat()