# - Importing random to set random color for alien colors
import random
alien_colors = ['green','yellow','red']
player_score = 0
alien_color = alien_colors[random.randint(0,2)]
print(f"Original alien color is {alien_color}.")

# - 5-3 - Statement to test if alien color is green.  If yes, assign player 5 points

if alien_color == 'green':
	player_score = player_score + 5
elif alien_color == 'yellow':
	player_score = player_score + 10
elif alien_color == 'red':
	player_score = player_score + 15

# - 5-5 example with if and elif statements.
print(f"Alien is {alien_color}. Player receives {player_score} points! Player score is currently {player_score}.")

