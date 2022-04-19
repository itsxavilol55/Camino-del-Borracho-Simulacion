from turtle import *
import random
print("cuantas veces se quiere hacer la simulacion?")
total = int(input())
speed(0.001)
delay(0.001)
medidaTotal=250
color("black")
#pinta los ejes X Y 
forward(medidaTotal)#eje X
forward(-medidaTotal*2)
home()
seth(90)
forward(medidaTotal)#eje Y
forward(-medidaTotal*2)
home()
for i in range(22): #dibuja las divisiones de los eje X
	if(i==11):
		home()
	if(i>=11):
		setx(-(i-11)*medidaTotal/10)
	else:
		setx(i*medidaTotal/10)
	seth(90)
	forward(10)
	forward(-20)
	seth(0)
	sety(0)
home()
seth(0)
for i in range(22): #dibuja las divisiones de los eje Y
	if(i==11):
		home()
	if(i>=11):
		sety(-(i-11)*medidaTotal/10)
	else:
		sety(i*medidaTotal/10)
	seth(180)
	forward(10)
	forward(-20)
	seth(90)
	setx(0)
home()
speed(0.07)
delay(0.08)
width(2)
color("#7bf")
num =0
Aciertos=0
for i in range(total): #intera dependiendo del total de veces
	distancia =0
	setx(0)
	sety(0)
	down()
	rojo = random.random()
	verde = random.random()
	azul = random.random()
	color(rojo,verde,azul)
	print("Simulacion:"+str(i+1))
	for j in range(10): #dibuja las cuadras del borracho
		num = random.random()
		if(num <= 0.25):# camina hacia el norte
			seth(90)
		if(num > 0.25 and num <= 0.5):# camina hacia el sur
			seth(270)
		if(num > 0.5 and num <= 0.75): #camina hacia el este
			seth(0)
		if(num > 0.75): #camina hacia el oeste
			seth(180)
		forward(medidaTotal/10)
		coorX = int(round(xcor())/(medidaTotal/10))#convierte las coordenadas
		coorY = int(round(ycor())/(medidaTotal/10))
		print(str(round(num,3))+" ("+str(coorX)+","+str(coorY)+")")
	distancia = abs(coorX) + abs(coorY)
	print("distancia:"+ str(distancia))
	if(distancia >= 2):
		Aciertos+= 1
		print("EXITO!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("")
	#dibuja la X de donde quedo el borracho
	seth(45)
	forward(10)
	forward(-20)
	forward(10)
	seth(-45)
	forward(10)
	forward(-20)
	#cortar el trazo del dibujo y reincia el angulo con seth(0)
	up()
	seth(0)
print("Aciertos:")
print(Aciertos)
print("Probabilidad:")
print(Aciertos/total)
done()