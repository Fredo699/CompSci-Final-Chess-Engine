#! /usr/bin/python

import time, os, shutil, sys, random, math, termbox

class FTF:
    current = None
    frames = None

    path = None
    out = None

    name = None
    frameCount = None
    frameHeight = None
    frameWidth = None
    delay = None
    

    def __init__(self, path, out):
        self.path = path
        self.out = out

        doc = open(path, "r")
        file = doc.read()
        doc.close()

        lines = file.split("\n")[:]
        meta = lines.pop(0).split(":")

        self.name = meta[0].split("--")[0]
        self.frameCount = int(meta[1])
        self.frameHeight = int(meta[2])
        self.frameWidth = int(meta[3])
        self.delay = float(meta[4])

        self.current = 0
        self.frames = []
        for i in range(self.frameCount):
            frame = []
            for l in range(self.frameHeight):
                line = lines.pop(0)
                while len(line) < self.frameWidth:
                    line += " "

                while len(line) > self.frameWidth:
                    line = line[:-1]
            
                frame.append(line)
            self.frames.append(frame)

    def switch(self, index):
        self.current = index
        self.out(self.frames[index])

    def animateYield(self,repeat=-1):
        while repeat is not 0:
            last = time.time()
            while time.time() - last < self.delay:
                yield

            self.switch((self.current + 1)%self.frameCount)
           
            if repeat is not -1:
                repeat -= 1;

    def animateProcess(self):
        pass

    def animateDelay():
        pass


class Graphic:
    posx = 0
    posy = 0
    maxx = 0
    maxy = 0

    window = None
    path = None
    ftf = None

    autoRefresh_flg = True

    def __init__(self, path, window, posx=0, posy=0, maxx=0, maxy=0):
        self.posx = posx
        self.posy = posy
        self.maxx = maxx
        self.maxy = maxy
        self.window = window
        self.path = path

        self.ftf = FTF(path, out=self.print_frame)

    def resizeToFTF(self,x,y):
        if x > 0 :
            self.posx = x - 1
            self.maxx = self.posx + self.ftf.frameWidth
        elif x < 0:
            self.maxx = self.window.width() + x + 1
            self.posx = self.maxx - self.ftf.frameWidth
        else:
            self.posx = math.floor(self.window.width()/2 - self.ftf.frameWidth/2)
            self.maxx = self.posx + self.ftf.frameWidth

        if y > 0 :
            self.posy = y - 1
            self.maxy = self.posy + self.ftf.frameHeight
        elif y < 0:
            self.maxy = self.window.height() + y + 1
            self.posy = self.maxy - self.ftf.frameHeight
        else:
            self.posy = math.floor(self.window.height()/2 - self.ftf.frameHeight/2)
            self.maxy = self.posy + self.ftf.frameHeight

    def moveToLimit(self, x ,y):
        if(x>0): 
            if(self.posx<x):
                delta = x-self.posx
                self.posx+=delta
                self.maxx+=delta
        if(y>0):
            if(self.posy<y):
                delta = y-self.posy
                self.posy+=delta
                self.maxy+=delta
        if(x<0): 
            x *= -1
            if(self.maxx>x):
                delta = x-self.posx
                self.posx+=delta
                self.maxx+=delta
        if(y<0):
            y *= -1
            if(self.maxy>y):
                delta = self.maxy-y
                self.posy-=delta
                self.maxy-=delta
        
    def print_char(self, x, y, char, fg, bg, update=None):
        gx = x+self.posx
        gy = y+self.posy
        
        self.window.change_cell(gx, gy, ord(char), fg, bg)

        if (update is None and self.autoRefresh_flg) or update:
            self.flush()
    
    def print_frame(self, frame, fg , bg,  update=None):
        for y in range(len(frame)):
            line = frame[y]
            for x in range(len(line)):
                char = line[x]
                self.print_char(x, y, char,fg, bg, update=False )
        
        if (update is None and self.autoRefresh_flg) or update:
            self.flush()

    def print_string(self, x, y, line, fg=termbox.DEFAULT, update=None):
        for i in range(len(line)):
            char = line[i]
            self.print_char(x+i, y, char, fg, termbox.DEFAULT, update=False )

        if (update is None and self.autoRefresh_flg) or update:
            self.flush()

    def flush(self):
        self.window.present()

    def set_state(self, state):
        self.ftf.switch(state)

    def set_state_adv(self, state, fg , bg):
        self.print_frame(self.ftf.frames[state], fg , bg, update=False)

    def clear(self, char=" ", update=None):
        for x in range(self.width()):
            for y in range(self.height()):
                self.print_char(x, y, char, termbox.DEFAULT, termbox.DEFAULT, update=False )
        
        if (update is None and self.autoRefresh_flg) or update:
            self.flush()

    def width(self):
        return self.maxx - self.posx

    def height(self):
        return self.maxy - self.posy

    def border(self, color, update=None):
        for x in range(self.maxx - self.posx):
            for y in range(self.maxy - self.posy):
                if x == 0 or y == 0 or x == self.width() - 1  or y == self.height() - 1:
                    self.print_char(x,y," ", color, color,update=False)
                    
        if (update is None and self.autoRefresh_flg) or update:
            self.flush()

    def maximise(self):
        self.posx = 0
        self.posy = 0
        self.maxx = self.window.width()
        self.maxy = self.window.height()

    def centerPrint(self, y, text, color):
        x = math.floor(self.width()/2 -len(text)/2)
        self.print_string(x, y, text, fg=color)

class Gui:
    box = None    
    display = None
    board = None
    source = [8,8]
    target = [8,8]
    cursor = [8,8]
    screen = None
    ftf = "piece.txt"

    def initGui(self):

        self.box = termbox.Termbox()
        self.box.hide_cursor()
        self.box.clear()
        self.box.present()
        self.display = []

        try:
            f = FTF(self.ftf, None)
            w = f.frameWidth
            h = f.frameHeight
            offset = math.floor(self.box.width()/2 - (4*w))

        except:
            print("invalid ftf file: " + self.ftf)
            self.closeGui()
            raise


        self.screen = Graphic(self.ftf, self.box)
        self.screen.maximise()
        self.screen.centerPrint(h*8 + 4,"arrow keys to move cursor, 'a' to select piece, 's' to select target, ENTER to make move",termbox.MAGENTA)

        for x in range(8):
            column = []
            for y in range(8):
                g = Graphic(self.ftf, self.box)
                g.autoRefresh_flg = False

                g.posx = x * w + offset
                g.posy = y * h + 3
                g.maxx = g.posx + w
                g.maxy = g.posy + h

                if random.randrange(1,3) == 1:
                    fg = termbox.BLACK
                    bg = termbox.WHITE
                else:
                    fg = termbox.WHITE
                    bg = termbox.BLACK

                g.set_state_adv(random.randrange(0,7),fg,bg)

                g.flush()
                column.append(g)

                
            self.display.append(column)

    def closeGui(self):
        self.box.close()

    def updateGuiList(self, game):
        board = game.current_board
        self.board = board
        for x in range(len(board)):
            for y in range(len(board)):
                piece = board[x][y]

                if (x+y)%2==0:
                    bg = termbox.BLACK
                else:
                    bg = termbox.WHITE   


                bg += termbox.BOLD
                if x == self.cursor[0] and y == self.cursor[1]:
                    bg = termbox.GREEN + termbox.BOLD

                
                index = self.get_state(piece.piece_type)
                if piece.color == "black":
                    fg = termbox.BLUE
                else:
                    fg = termbox.RED
                
                self.display[x][y].set_state_adv(index, fg , bg)
                
                if x == self.source[0] and y == self.source[1]:
                    self.display[x][y].border(termbox.MAGENTA)

                if x == self.target[0] and y == self.target[1]:
                    self.display[x][y].border(termbox.YELLOW)

                self.display[x][y].flush()

    def get_state(self, piece):
        if piece == "pawn":
            return 1
        elif piece == "rook":
            return 2
        elif piece == "knight":
            return 3
        elif piece == "bishop":
            return 5
        elif piece == "queen":
            return 4
        elif piece == "king":
            return 6
        else:
            return 0

    def readInput(self,game):
        event = self.box.peek_event(timeout=30)
        if event:
            (typee, char, key, mod, width, height, mousex, mousey) = event
            
            if typee == termbox.EVENT_KEY and char == "a":
                
                if pEquals(self.source, self.cursor):
                    self.resetSelection()
                elif game.isSelectValid(self.cursor):
                    self.resetSelection()
                    self.source[0]=self.cursor[0]
                    self.source[1]=self.cursor[1]
                else:
                    self.error(self.display[ self.cursor[0] ][ self.cursor[1] ])

            if typee == termbox.EVENT_KEY and char == "s":

                if not ( pEquals(self.source, [8,8]) or pEquals(self.source, self.cursor )) and game.isMoveValid(self.source, self.cursor):
                    self.target[0]=self.cursor[0]
                    self.target[1]=self.cursor[1]
                else:
                    self.error(self.display[ self.cursor[0] ][ self.cursor[1] ])


            if typee == termbox.EVENT_KEY and char == "d":
                self.resetSelection()

            if typee == termbox.EVENT_KEY and key == termbox.KEY_ENTER:
                game.move(self.source, self.target)
                self.resetSelection()

            if typee ==  termbox.EVENT_KEY and key == termbox.KEY_ESC:
                self.closeGui()
                sys.exit()

            if typee == termbox.EVENT_KEY and key == termbox.KEY_ARROW_UP:
                self.cursor[1] -= 1
                self.moveCursor(self.cursor)

            if typee == termbox.EVENT_KEY and key == termbox.KEY_ARROW_DOWN:
                self.cursor[1] += 1
                self.moveCursor(self.cursor)

            if typee == termbox.EVENT_KEY and key == termbox.KEY_ARROW_LEFT:
                self.cursor[0] -= 1
                self.moveCursor(self.cursor)

            if typee == termbox.EVENT_KEY and key == termbox.KEY_ARROW_RIGHT:
                self.cursor[0] += 1
                self.moveCursor(self.cursor)

    def moveCursor(self, c):
        self.cursor[0] = c[0]
        self.cursor[1] = c[1]
        
        self.cursor[1] = 0 if self.cursor[1] < 0 else self.cursor[1]
        self.cursor[1] = 7 if self.cursor[1] > 7 else self.cursor[1]
        self.cursor[0] = 0 if self.cursor[0] < 0 else self.cursor[0]
        self.cursor[0] = 7 if self.cursor[0] > 7 else self.cursor[0]
    
    def resetSelection(self):
        self.source = [8,8]
        self.target = [8,8]
    
    def set_turn(self, player):
        if player == "black":
            color = termbox.BLUE
            text = "blue player's turn"
        else:
            color = termbox.RED
            text = "red player's turn"

        self.screen.border(color)
        self.screen.centerPrint(1, text, termbox.GREEN)
        self.screen.flush()


    def error(self, target):
        target.border(termbox.RED)
        target.flush()
        time.sleep(.1)
        target.border(termbox.DEFAULT)
        target.flush()

def pEquals(p1,p2):
    return p1[0]==p2[0] and p1[1]==p2[1]
                                                       
                 
