import random
from tkinter import *
from tkinter.colorchooser import *
from tkinter import filedialog
import time
global canvas_width, canvas_height
canvas_width = 400
canvas_height = 400
b1,b2 = 'up','up'
colour1 = ''
colour2 = ''
xold, yold = None, None
lastEventx = None
lastEventy = None
SWheel = 0
class DrawPaint():
    def b1down(event):
        global b1,xold,yold
        b1 = "down"           
        if xold is None and yold is None:
            xold = event.x
            yold = event.y
        if toolVar.get() == 'Get':
            drawing_area.create_image(event.x, event.y, image = importImage, tags = 'pasted') 
    def b1up(event):
        global b1, xold, yold,c,r
        b1 = "up"
        xold = None          
        yold = None
        drawing_area.itemconfig(c, tags = random.random()*random.random())
        drawing_area.itemconfig(r, tags = random.random()*random.random())
    def b2down(event):
        global b2,xold,yold
        b2 = "down"           
        if xold is None and yold is None:
            xold = event.x
            yold = event.y
    def b2up(event):
        global b2, xold, yold
        b2 = "up"
        xold = None           
        yold = None
        drawing_area.itemconfig(c, tags = random.random()*random.random())
        drawing_area.itemconfig(r, tags = random.random()*random.random())
    def lineWidth(event):
        SWheel.set(SWheel.get() + 1*((-1)*int((event.delta/120)*-1)))
        if SWheel.get() > 20:
            SWheel.set(20)
        elif SWheel.get() < 1:
            SWheel.set(1)
    def motion(event):
        global colour1,colour2,c,r
        if colour1 == "":
            colour_name = "black"
            colour_inname = 'white'
        else:
            colour_name = colour1[1]
        if colour2 == "":
            colour_inname = "white"
        else:
            colour_inname = colour2[1]       
        if toolVar.get() == "Pencil":
            print('gg')
            global xold, yold
            if xold is not None and yold is not None:
                if b1 == "down":
                    for i in range(SWheel.get()+1):
                        event.widget.create_line(xold,yold,event.x,event.y,width = SWheel.get(),fill=colour_name)                        
                elif b2 == 'down':
                    for i in range(SWheel.get()+1):
                        event.widget.create_line(xold,yold, event.x,event.y,width = SWheel.get(),fill=colour_inname)
                xold = event.x
                yold = event.y     
        elif toolVar.get() == "Circle":
            print('gg')
            global xold, yold
            if xold is not None and yold is not None:
                    event.widget.delete('myCircle')
                    if b1 == "down":
                        c = event.widget.create_oval(xold,yold, event.x,event.y,width = 0,fill=colour_name, tags = 'myCircle') 
                    elif b2 == "down":
                        c = event.widget.create_oval(xold,yold, event.x,event.y,width = 0,fill=colour_inname, tags = 'myCircle') 
        elif toolVar.get() == "Rectangle":
            global xold, yold
            if xold is not None and yold is not None:
                event.widget.delete('myRectangle')
                if b1 == "down":
                    r = event.widget.create_rectangle(xold,yold, event.x,event.y,width = 0,fill=colour_name,tags = 'myRectangle') 
                elif b2 == "down":
                    r = event.widget.create_rectangle(xold,yold, event.x,event.y,width = 0,fill=colour_inname,tags = 'myRectangle') 
        elif toolVar.get() == "Spray":
            global xold, yold, counter
            if xold is not None and yold is not None:
                if b1 == "down":
                    event.widget.create_oval(event.x - 1, event.y+5 - 1, event.x + 1, event.y+5 + 1, fill = colour_name)
                    event.widget.create_oval(event.x-5 - 1, event.y-5 - 1, event.x-5 + 1, event.y-5 + 1, fill = colour_name)
                    event.widget.create_oval(event.x+5 - 1, event.y-5 - 1, event.x+5 + 1, event.y-5 + 1, fill = colour_name)
                    event.widget.create_oval(event.x - 1, event.y-5 - 1, event.x + 1, event.y-5 + 1, fill = colour_name)
                elif b2 == "down":
                    event.widget.create_oval(event.x - 1, event.y+5 - 1, event.x + 1, event.y+5 + 1, fill = colour_inname)
                    event.widget.create_oval(event.x-5 - 1, event.y-5 - 1, event.x-5 + 1, event.y-5 + 1, fill = colour_inname)
                    event.widget.create_oval(event.x+5 - 1, event.y-5 - 1, event.x+5 + 1, event.y-5 + 1, fill = colour_inname)
                    event.widget.create_oval(event.x - 1, event.y-5 - 1, event.x + 1, event.y-5 + 1, fill = colour_inname)
        elif toolVar.get() == "Fill":
            global xold, yold
            if xold is not None and yold is not None:
                closest = drawing_area.find_closest(event.x, event.y)
                tagFill = drawing_area.gettags(closest)
                if b1 == "down":
                    if tagFill == ():
                        drawing_area.config(bg = colour_name)
                    for tagers in tagFill:
                        print(tagers)
                        drawing_area.itemconfig(tagers, fill = colour_name)
                elif b2 == "down":
                    if tagFill == ():
                        drawing_area.config(bg = colour_inname)
                    for tagers in tagFill:
                        print(tagers)
                        drawing_area.itemconfig(tagers, fill = colour_inname)
        elif toolVar.get() == "Bubble":
            print(toolVar.get())
            global xold, yold
            if xold is not None and yold is not None:
                if b1 == "down":
                    event.widget.create_oval(event.x - SWheel.get(), event.y - SWheel.get(), event.x + SWheel.get(), event.y + SWheel.get(), fill = colour_name)
                elif b2 == "down":
                    event.widget.create_oval(event.x - SWheel.get(), event.y - SWheel.get(), event.x + SWheel.get(), event.y + SWheel.get(), fill = colour_inname)
        elif toolVar.get() == 'Firework':
            global xold, yold
            if xold is not None and yold is not None:
                if b1 == "down":
                    event.widget.create_line(xold,yold,event.x,event.y,width = SWheel.get(),fill=colour_name)
                elif b2 == "down":
                    event.widget.create_line(xold,yold,event.x,event.y,width = SWheel.get(),fill=colour_inname)
        elif toolVar.get() == 'Erase':
                closest = drawing_area.find_closest(event.x, event.y)
                tagErase = drawing_area.gettags(closest)
                if b1 == "up":
                    drawing_area.delete('current')
##        elif toolVar.get() == "Dropper":
##                closest = drawing_area.find_closest(event.x, event.y)
##                tagDrop = drawing_area.gettags(closest)
##                print(tagDrop)
##                if b1 == "down":
##                    print('wkl')
##                    if tagDrop == ():
##                        colour_name = drawing_area['bg']
##                    for tagers in tagDrop:
##                        print(drawing_area.itemcget('currect','fill'))
##                        colour_name = drawing_area.itemcget('currect','fill')
##                        print(colour_name)
##                elif b2 == "down":
##                    if tagDrop == ():
##                        colour_inname = drawing_area['bg']
##                    for tagers in tagDrop:
##                        colour_inname = tagers
        elif toolVar.get() == 'Get':
            if b1 == 'up':
                if b1 != 'down':
                    drawing_area.delete('myPicture')
                picture = drawing_area.create_image(event.x,event.y,image = importImage, tags = 'myPicture')
def main():
    global drawing_area, root, xVar, yVar
    root = Tk()
    root.title("Paint Program By Tair Nuriev")
    drawing_area = Canvas(root, width =canvas_width, height = canvas_height,bg = 'white')
    drawing_area.pack()
    drawing_area.bind("<Motion>", DrawPaint.motion)
    drawing_area.bind("<ButtonPress-1>", DrawPaint.b1down)
    drawing_area.bind("<ButtonRelease-1>", DrawPaint.b1up)
    drawing_area.bind("<ButtonPress-3>", DrawPaint.b2down)
    drawing_area.bind("<ButtonRelease-3>", DrawPaint.b2up)
    drawing_area.bind("<MouseWheel>", DrawPaint.lineWidth)
    toolFrame = Frame(root)
    toolFrame.pack()
    frame1 = Frame(root)
    frame1.pack()
    Label(frame1, text = "Tools").grid(row = 0, column = 0, sticky = W)
    b1 = Button(toolFrame,command = pencil,relief = RIDGE)
    photoPencil = PhotoImage(file = "pencilTool.gif")
    b1.config(image=photoPencil,width = '20', height = '20')
    b1.pack(side = LEFT)
    b2 = Button(toolFrame,command = bubble,relief = RIDGE)
    photoBubble = PhotoImage(file = "bubbleTool.gif")
    b2.config(image=photoBubble,width = '20', height = '20')
    b2.pack(side = LEFT)
    b3 = Button(toolFrame,command = fill,relief = RIDGE)
    photoFill = PhotoImage(file = "fillTool.gif")
    b3.config(image=photoFill,width = '20', height = '20')
    b3.pack(side = LEFT)
    b4 = Button(toolFrame,command = spray,relief = RIDGE)
    photoSpray = PhotoImage(file = "sprayTool.gif")
    b4.config(image=photoSpray,width = '20', height = '20')
    b4.pack(side = LEFT)
    b5 = Button(toolFrame,command = circle,relief = RIDGE)
    photoCircle = PhotoImage(file = "circleTool.gif")
    b5.config(image=photoCircle,width = '20', height = '20')
    b5.pack(side = LEFT)
    b6 = Button(toolFrame,command = rectangle,relief = RIDGE)
    photoRectangle = PhotoImage(file = "rectangleTool.gif")
    b6.config(image=photoRectangle,width = '20', height = '20')
    b6.pack(side = LEFT)
    b8 = Button(toolFrame,command = firework,relief = RIDGE)
    photoFirework = PhotoImage(file = "fireworkTool.gif")
    b8.config(image=photoFirework,width = '20', height = '20')
    b8.pack(side = LEFT)
    b11 = Button(toolFrame,command = erase,relief = RIDGE)
    photoErase = PhotoImage(file = "eraseTool.gif")
    b11.config(image=photoErase,width = '20', height = '20')
    b11.pack(side = LEFT)
##    b13 = Button(toolFrame,command = dropper,relief = RIDGE)
##    photoDrop = PhotoImage(file = "drop.gif")
##    b13.config(image=photoDrop,width = '20', height = '20')
##    b13.pack(side = LEFT)
    b7 = Button(toolFrame,command = getPrimeColour,relief = RIDGE)
    photoColour = PhotoImage(file = "colourTool.gif")
    b7.config(image=photoColour,width = '20', height = '20')
    b7.pack(side = LEFT)
    b9 = Button(toolFrame,command = getSecondColour,relief = RIDGE)
    photoColourIn = PhotoImage(file = "colourInTool.gif")
    b9.config(image=photoColourIn,width = '20', height = '20')
    b9.pack(side = LEFT)
    b10 = Button(toolFrame,command = saveImage,relief = RIDGE)
    photoSave = PhotoImage(file = "save.gif")
    b10.config(image=photoSave,width = '20', height = '20')
    b10.pack(side = LEFT)
    b12 = Button(toolFrame,command = openImage,relief = RIDGE)
    photoOpen = PhotoImage(file = "open.gif")
    b12.config(image=photoOpen,width = '20', height = '20')
    b12.pack(side = LEFT)
    b14 = Button(toolFrame,command = clear,relief = RIDGE)
    photoClear = PhotoImage(file = "new.gif")
    b14.config(image=photoClear,width = '20', height = '20')
    b14.pack(side = LEFT)
    b15 = Button(toolFrame,command = setcoords,relief = RIDGE,text ='Stamp')
    b15.config(width = '8', height = '1')
    b15.pack(side = LEFT)
    b16 = Button(toolFrame,command = intro,relief = RIDGE,text ='HELP!!!')
    b16.config(width = '8', height = '1')
    b16.pack(side = LEFT)
    xVar = StringVar()
    yVar = StringVar()
    frame2 = Frame(root)
    frame2.pack()
    Label(frame2, text = "Window Size").grid(row = 0, column = 0, sticky = W)
    a = Entry(frame2, textvariable = xVar).grid(row = 0, column = 1)
    b = Entry(frame2,  textvariable = yVar).grid(row = 0, column = 2)
    frame3 = Frame(root)
    frame3.pack()
    bR = Button(frame3,command = resize,relief = RIDGE)
    photoWin = PhotoImage(file = "resize.gif")
    bR.config(image=photoWin,width = '20', height = '20')
    bR.pack(side = LEFT)
    global toolVar,SWheel
    toolVar = StringVar()
    SWheel = IntVar()
    root.mainloop()   
def pencil():
    toolVar.set("Pencil")
    drawing_area.config(cursor = 'pencil')
def circle():
    toolVar.set("Circle")
    drawing_area.config(cursor = 'dot')
def bubble():
    toolVar.set("Bubble")
    drawing_area.config(cursor = 'circle')
def fill():
    toolVar.set('Fill')
    drawing_area.config(cursor = 'coffee_mug')
def spray():
    toolVar.set('Spray')
    drawing_area.config(cursor = 'spraycan')
def rectangle():
    toolVar.set('Rectangle')
    drawing_area.config(cursor = 'dotbox')
def firework():
    toolVar.set('Firework')
    drawing_area.config(cursor = 'spider')
def erase():
    toolVar.set('Erase')
    drawing_area.config(cursor = 'icon')
def setcoords():
    toolVar.set('Get')
def getPrimeColour():
    global colour1
    colour1 = askcolor()    
def getSecondColour():
    global colour2
    colour2 = askcolor()
##def dropper():
##    toolVar.set('Dropper')
##    drawing_area.config(cursor = 'plus')
def saveImage():
    global filenm, save
    filenm = StringVar()
    root.title("Saving...")
    time.sleep(1)
    root.title("Almost done..")
    filenm = StringVar()
    filenm.set(filedialog.asksaveasfilename())
    drawing_area.postscript(file = (filenm.get() + '.eps'))
    root.title(filenm.get())
def openImage():
    global importImage
    filenm = StringVar()
    root.title("Opening...")
    time.sleep(1)
    root.title("Almost done..")
    filenm = StringVar()
    filenm.set(filedialog.askopenfilename(defaultextension = 'gif'))
    importImage = PhotoImage(file = filenm.get())
    label = Label(image=importImage)
    label.image = importImage # keep a reference!
    root.title('')
def clear():
    drawing_area.delete('all')
def resize():
    if  int(yVar.get()) >= 920:
        yVar.set('920')
    if  int(xVar.get()) >= 1920:
        xVar.set('1920')
    drawing_area.config(width = int(xVar.get()), height = int(yVar.get()))
def intro():
    global introwin
    introwin = Tk()
    introwin.title("Introduction and Instructions")
    inframe = Frame(introwin)
    inframe.pack()
    Label(inframe, text = 'Hello. This is a Paint Program designed and programmed by Tair Nuriev').grid(row = 0,column = 0, sticky = W)
    Label(inframe, text = 'Intructions (IN ORDER):').grid(row = 1,column = 0, sticky = W)
    Label(inframe, text = '    Pencil Tool:    Draws a line which the user can move with a mouse, Width of the line is controlled by the Scroll Wheel').grid(row = 2,column = 0, sticky = W)
    Label(inframe, text = '    Bubble Tool:    Draws bubbles when mouse is moved. Circle can be changed with Scroll Wheel').grid(row = 2,column = 0, sticky = W)
    Label(inframe, text = '    Fill Tool:      Changes the fill colour of a drawn object, everything drawn is treated as a seperate object').grid(row = 3,column = 0, sticky = W)
    Label(inframe, text = '    Spray Tool:     Spraycan like tool found in MS Paint, Size of the spray is controlled by the Scroll Wheel').grid(row = 4,column = 0, sticky = W)
    Label(inframe, text = '    Cicle Tool:     Draws a resizeable circle(only when mouse button is held)').grid(row = 5,column = 0, sticky = W)
    Label(inframe, text = '    Rectangle Tool: Draws a resizeable rectangle(only when mouse button is held)').grid(row = 6,column = 0, sticky = W)
    Label(inframe, text = '    SpiderWeb Tool: Draws spiderweb strands, Width of the line is controlled by the Scroll Wheel').grid(row = 7,column = 0, sticky = W)
    Label(inframe, text = '    Eraser Tool:    Erases objects when hovered over them(activated when mouse button is NOT pressed)').grid(row = 8,column = 0, sticky = W)
    #Label(inframe, text = '    ColourPippette Tool: When equipped, user can change primary colour when clicked on the drawn object').grid(row = 9,column = 0, sticky = W)
    Label(inframe, text = '    Primary Colour: User can select primary colour from the colour pallete(Primary colour is the fill colour of the tool when left mouse button is used to draw)').grid(row = 10,column = 0, sticky = W)
    Label(inframe, text = '    Secondary Colour: User can select secondary colour from the colour pallete(Secondary colour is the fill colour of the tool when right mouse button is used to draw)').grid(row = 11,column = 0, sticky = W)
    Label(inframe, text = '    Save Canvas: User can save canvas drawing in a user selected directory. The canvas can only be saved is .eps format(Using a free program like EPS Viewer, the user can convert it to .jpeg)').grid(row = 12,column = 0, sticky = W)
    Label(inframe, text = '    Stamp Image: User can select a .gif image to use it for stamp tool(Image has to be resized by user before use)').grid(row = 13,column = 0, sticky = W)
    Label(inframe, text = '    Clear Canvas: Clears the canvas').grid(row = 14,column = 0, sticky = W)
    Label(inframe, text = '    Stamp Tool: Using the image imported, User can place the image onto the canvas').grid(row = 15,column = 0, sticky = W)
    Label(inframe, text = '    Window Size: Changes the width and height of the canvas').grid(row = 16,column = 0, sticky = W)
    clframe = Frame(introwin)
    clframe.pack()
    Button(clframe, text = 'Close', command = callback).pack(side = LEFT)
def callback():
    introwin.destroy()


if __name__ == "__main__":
    main()
    
