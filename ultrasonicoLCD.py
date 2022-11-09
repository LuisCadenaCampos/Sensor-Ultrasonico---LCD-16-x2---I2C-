"""
Autor original de la biblioteca I2C LCD 16x2
Usuario de Github: T-622
Version: 1.0.0
Fuente: https://github.com/T-622/RPI-PICO-I2C-LCD.git


Autor del codigo: Cadena Campos Luis
Fecha de creacion: 01/11/2022
Version de codigo: 1.0.0
Correo:luis14oriente@gmail.com

""" 
#Traemos nuestras bibliotecas
from machine import Pin,I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import utime

#Indicamos la direccion del i2c
I2C_ADDR   = 0x27
#Declaramos el numero de renglones y columnas
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0,sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c,I2C_ADDR,I2C_NUM_ROWS,I2C_NUM_COLS)

#Declaramos los pins a usar para echo y trigger
trigger = Pin(17,Pin.OUT)
echo = Pin(16,Pin.IN)
#Declaramos un led que nos servira para avisar que un objeto esta a menos de 10 cm
led = Pin(19, Pin.OUT)
#Declaramos un buzzer pasivo que empezara a sonar
buzzer = Pin(20,Pin.OUT)
#Hacemos que el trigger valga 0
trigger.value(0)

while True:
    #Lanzamos la onda sonora
    trigger.value(1)
    utime.sleep_us(10) #Retardo de 10 micro segundos
    trigger.value(0)
    #Calcular el tiempo
    t1 = utime.ticks_us()
    while echo.value() == 0:
        t1= utime.ticks_us()
    while echo.value() == 1:
        t2= utime.ticks_us()
    #Calcular el tiempo
    t = t2-t1
    d = 17*t/1000
    utime.sleep_ms(500)
    #Empezamos a escribir los valores y el texto
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Distancia:")
    lcd.move_to(0,1)
    lcd.putstr(str(d)+" cm")
    if d <=10:
    #Si la distancia es menor a 10 cm, se prendera un led y empezara a sonar un buzzer pasivo
        led.on()
        for i in range(20):
            buzzer.on()
            utime.sleep_ms(5)
            buzzer.off()
            utime.sleep_ms(5)
    else:
        led.off()
            
            
            
        

            
