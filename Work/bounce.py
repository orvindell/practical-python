# bounce.py
#
# Exercise 1.5
height = 100
no_bounces = 10

while no_bounces > 0:
	height = 0.6*height
	no_bounces = no_bounces - 1
	print(round(height,4))


