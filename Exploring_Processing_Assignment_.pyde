x = 0
a = 4
keyboard = 0 
y = 0
b = 3
press = 0

def setup():
    global sat_img
    global back_img
    
    size(729, 425)
    sat_img = loadImage("nemo.png") #nemo
    back_img = loadImage("ocean.jpg") #background
    

def draw():
    background (back_img)
    
    #nemo bouncing off 
    global x
    global a
    global keyboard
    
    if keyboard == 1:
        if x > 600 or x < 0: 
            a = a*(-1) 
        x += a 
    
    image(sat_img, x, 275, 140, 80)
   
    #sun moving
    global y 
    global b
    global press 
    
    if press == 1:         
        if  y > 168 or y < 0: 
            b = b*(-1)
        y += b
        
    fill(255, 225, 0)
    ellipse(600, y, 80, 80)
   
    #sun 
    fill(255, 99, 71)
    triangle(580, 130, 620, 130, 600, 160)
    triangle(620, 130, 656, 134, 645, 100)
    triangle(645, 100, 635, 60, 668, 70)
    triangle(600, 49, 635, 60, 627, 30)
    triangle(572, 30, 565, 60, 600, 49)
    triangle(565, 60, 530, 70, 555, 100)
    triangle(555, 100, 545, 134, 580, 130)
    fill(0, 0, 0)
    arc(580, 80, 40, 40, 0, PI, CHORD)
    arc(620, 80, 40, 40, 0, PI, CHORD) 

    
    #text
    textSize(32)
    fill(255, 255, 255)
    text("Summer!!", 50, 50)
    
    
def keyPressed():  
    global keyboard
    keyboard += 1
    if keyboard == 2:
        keyboard = 0
        
def mousePressed():
    global press 
    press += 1
    if press == 2: 
        press = 0 
    
