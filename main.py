import random

print('=========================================')
print('  Hello, it is mini rpg game on python!  ')
print('=========================================')
print('')

nameHero = input('Enter name your hero: ')
# hero hp
# enemy hp random
# boss hp

# atack hero random
# atack enemy random
# atack boss random + func
# wawe 5 enemy + 1 boss
# lvl system for hero, xp system, xp drop after kill enemy or boss

# backpage, invetory
# item who spawn: heal bottle, new sword, armor, ring(for stat +hp, +dps)

# after kill enemy you might, take loot, next wawe, check backpage, check
hpHero = 10
invetory = {}


numberEnemy = {
	'first': 3, 
	'second': 10, 
	'three': 3,
	'forth': 5,
	'fiveth': 5,
}
wave = 0
maxWave = 1
# print(numberEnemy)

while wave < maxWave:
	print('wave', wave)
	attackHero = random.randint(1,2)
	attackEnemy = random.randint(1,2)

	print('Menu')
	print('1 next wave')
	print('2 check invetory')
	print('3 exit game')

	menu = int(input('Select answer: '))

	if menu == 3:
		wave = maxWave
		print('Quit the game, bye!')
	elif menu == 2:
		print(invetory)
	if wave == 0 and menu == 1:
		enemy = numberEnemy.get('first')
		while enemy > 0:
			enemy = enemy - attackHero
			print('hp 1', enemy)
			print('attack', attackHero)

		wave += 1
		print('wave', wave)


	



