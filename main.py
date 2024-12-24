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
hpEnemy = 3
wave = 0


attackHero = random.randint(3,5)
attackEnemy = random.randint(1,2)

while wave < 5:
	
	numberEnemy = numberEnemy + 1
