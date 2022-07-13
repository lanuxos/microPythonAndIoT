# ep.8
import time
from tkinter import *
from PIL import Image, ImageTk
from threading import Thread
import time

gui = Tk()
gui.geometry('1366x768')
gui.title('MicroPython Dash Board')
gui.state('zoomed') # full screen

canvas = Canvas(gui, width=1366, height=768)
# canvas.place(x=230, y=130)
canvas.place(x=0, y=0)

background = ImageTk.PhotoImage(Image.open('smartfarm.png'))
canvas.create_image(0, 0, anchor=NW, image=background)

canvas.create_polygon([695,410,695,400,705,407,707,416], fill='red', width=1, outline=None, tags='d')
# canvas.create_polygon([701,427], fill='red', width=1, outline=None)

canvas.create_text(500, 500, text="The door's state", fill='white', font=('Times New Roman', 30, 'bold'), tags='d')

canvas.create_line(374, 524, 647, 524, 700, 412, fill='grey', width=3, tags='d')

# canvas.delete('d')

doorState = True
def Door(event):
    global doorState
    doorState = not doorState
    canvas.delete('d1')
    if doorState == True:
        canvas.create_polygon([695, 410, 695, 400, 705, 407, 707, 416], fill='green', width=1, outline=None, tags='d')
        canvas.create_text(500, 500, text="The door's state", fill='green', font=('Times New Roman', 30, 'bold'), tags='d')
        canvas.create_line(374, 524, 647, 524, 700, 412, fill='grey', width=3, tags='d')
    else:
        canvas.create_polygon([695, 410, 695, 400, 705, 407, 707, 416], fill='red', width=1, outline=None, tags='d')
        canvas.create_text(500, 500, text="The door's state", fill='red', font=(
            'Times New Roman', 30, 'bold'), tags='d')
        canvas.create_line(374, 524, 647, 524, 700, 412, fill='grey', width=3, tags='d')


fan = ImageTk.PhotoImage(Image.open('fan.png'))
canvas.create_image(416, 310, image=fan, tags='img3')

angle = 0

def run_fan(event=None):
	# fan = ImageTk.PhotoImage(resize_image('fan-icon.png',100))
	global angle
	while True:
		if angle != 0:
			canvas.delete('img3')
			fan = ImageTk.PhotoImage(image=Image.open('fan.png').rotate(angle))
			canvas.create_image(416, 310, image=fan, tags='img3')
		angle += 45
		if angle >= 360:
			angle = 0
		time.sleep(0.1)

task = Thread(target=run_fan)
task.start()

gui.bind('<Return>', Door)

gui.mainloop()
