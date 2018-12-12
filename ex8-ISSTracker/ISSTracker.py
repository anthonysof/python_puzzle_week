#!!!!Python3!!!!

import json
import turtle
import urllib.request
import time

def main():
	url = 'http://api.open-notify.org/astros.json'
	response = urllib.request.urlopen(url)
	result = json.loads(response.read())

	print('People in space: ', result['number'])
	astronauts = result['people']
	for astronaut in astronauts:
		print(astronaut['name'] + " Craft: " + astronaut['craft'])

	screen = turtle.Screen()
	screen.setup(1280, 720)
	screen.setworldcoordinates(-180, -90, 180, 90)
	screen.bgpic('map.gif')

	screen.register_shape('iss.gif')
	iss = turtle.Turtle()
	iss.shape('iss.gif')
	iss.setheading(90)
	text1 = turtle.Turtle()
	text1.penup()
	text1.goto(-180, -90)
	text2 = turtle.Turtle()
	text2.penup()
	text2.goto(-140, -90)

	while True:
		text1.clear()
		text2.clear()
		url = 'http://api.open-notify.org/iss-now.json'
		response = urllib.request.urlopen(url)
		result = json.loads(response.read())

		location = result['iss_position']
		lat = float(location['latitude'])
		lon = float(location['longitude'])
		text1.write(lat, font=("Arial", 16, "bold"))
		text2.write(lon, font=("Arial", 16, "bold"))

		

		iss.penup()
		iss.goto(lon, lat)


		print(lon)
		print(lat)
		#turtle.update_idletasks()
		turtle.update()
		time.sleep(5)
		
	

	


if __name__ == '__main__':
	main()