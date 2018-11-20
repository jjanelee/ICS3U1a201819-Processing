'''
Draw a cloud in the centre of the screen
'''
a = 150
b = 300
c = 450

def setup():
    size(640, 360)
    background(176, 196, 222)
    noStroke()
    
      
def draw():
    global a
    global b
    global c
    background(176, 196, 222)
    drawCloud(a, 200)
    drawCloud(b, 160)
    drawCloud(c, 120)
    
    
    if a >= 640:
        a = 0
    a += 3
    if b >= 640:
        b = 0
    b += 3
    if c >= 640:
        c = 0
    c += 3
        
    
def drawCloud(x, y):
    ellipse(x, y, 50, 50)
    ellipse(x+30, y, 50, 50)
    ellipse(x+10, y-25, 50, 50)
    

    
