import tkinter as tk
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

red = 2
green = 10
blue = 21


GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

root= tk.Tk()
root.title("Three LED blink GUI")

def TurnOff():
    GPIO.output(red,GPIO.LOW)
    GPIO.output(green,GPIO.LOW)
    GPIO.output(blue,GPIO.LOW)
    
def TurnOn():
    TurnOff()
    GPIO.output(var.get(),GPIO.HIGH)

var= tk.IntVar()

led1 = tk.Radiobutton(root, text ="red",bg="red", variable=var,value=2, command=TurnOn).pack()
led2 = tk.Radiobutton(root, text ="green",bg="blue", variable=var,value =10, command=TurnOn).pack()
led3 = tk.Radiobutton(root, text ="blue",bg="green", variable=var,value =21, command=TurnOn).pack()
tk.Exitbutton = tk.Button(root, text="Exit",bg="yellow", command=root.destroy).pack()


root.mainloop()

GPIO.cleanup()