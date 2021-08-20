#KNIGHT'S  MOVEMENTS
import turtle
import time
import sys
turtle.setup(700,700)
turtle.setworldcoordinates(-250,-250,250,250)
turtle.title("KNIGHT'S MOVEMENTS ")
def draw_square(x,y,size,color):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(0)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor(color)
    for i in range(4):
        turtle.fd(size)
        turtle.left(90)
    turtle.end_fill()      
def draw_board(src=(-2,-2),dest=(-2,-2), mlist=[]):
    turtle.pencolor("black")
    y = -200
    piecesize = 50
    startpiececolor = "black"
    for i in range(8):
        x = -200
        piececolor = startpiececolor
        for j in range(8):
            if (j+1,i+1)==src:
                draw_square(x,y,piecesize,'brown')
            elif (j+1,i+1)==dest:
                draw_square(x,y,piecesize,'red')
            elif (j+1,i+1) in mlist:
                draw_square(x,y,piecesize,'pink')                
            else:   
                draw_square(x,y,piecesize,piececolor)
            x += piecesize
            if piececolor == "black":
                piececolor = "silver"
            else:
                piececolor = "black"
        y += piecesize
        if startpiececolor == "black":
            startpiececolor = "silver"
        else:
            startpiececolor = "black"   
def draw_knight(pos):
    xpos = 50*(pos[0]-1) - 175
    ypos = 50*(pos[1]-1) - 195
    turtle.up()
    turtle.goto(xpos,ypos)
    turtle.write('\u265e',align='center',font=('Arial',45,'normal'))
class node:
    def __init__(self,val,nxt=None):
        self.value=val
        self.next=nxt
class LinkedList:
    def __init__(self,it=None):
        self.head = None
        self.tail = None
        self.length = 0
        if it is None: return
        for x in it:
            self.insert_at_tail(x)
    def insert_at_head(self,k):
        if self.head is None:
            self.head = node(k)
            self.tail = self.head
        else:
            p = node(k,self.head)
            self.head = p
        self.length += 1
    def insert_after(self,p,k):
        if self.length < p or p < 0:
            raise Exception('NOT POSSIBLE ! '+str(p))
        if p==0:
            self.insert_at_head(k)
            return
        q = self.head
        for _ in range(p-1):
            q = q.next
        q.next = node(k,q.next)
        
    def insert_at_tail(self,k):
        if self.tail is None:
            self.head = node(k)
            self.tail = self.head
        else:
            self.tail.next = node(k)
            self.tail = self.tail.next
        self.length += 1

    def __iter__(self):
        p = self.head
        while p is not None:
            yield p.value
            p = p.next
            
    def __len__(self):
        return self.length
    
    def __str__(self):
        s = ""
        p = self.head
        while p is not None:
            s += str(p.value) + '->'
            p = p.next
        s += 'None'
        return s

    def delete_from_head(self):
        if self.head is None: return
        self.length -= 1
        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def delete_from_tail(self):
        if self.head is None: return
        self.length -= 1
        if self.head == self.tail: self.head = self.tail = None
        p = self.head
        while p.next != self.tail:
            p = p.next
        p.next = None
        self.tail = p
class Queue:
    def __init__(self):
        self.ll = LinkedList()
        self.length = len(self.ll)

    def push(self,k):
        self.ll.insert_at_tail(k)

    def pop(self):
        if len(self.ll)==0:
            raise Exception('Queue is empty')
        self.ll.delete_from_head()

    def top(self):
        if len(self.ll)==0:
            raise Exception('Queue is empty')
        return self.ll.head.value;
        
    def empty(self):
        return len(self.ll)==0

    def __len__(self):
        return len(self.ll)

class position:
    def __init__(self,pos,dist,parent):
        self.pos = pos
        self.dist = dist
        self.parent = parent

moves = [ (1,2), (1,-2), (-1,2),(-1,-2), (2,-1), (2,1), (-2,1), (-2,-1) ]

def valid_position(pos):
    if pos[0] < 1 or pos[0] > 8 or pos[1] < 1 or pos[1] > 8: return False
    return True

def minimum_knight_move(src, dest):
    q = Queue()
    s = set()
    q.push(position(src,0,None))
    s.add(src)
    while not q.empty():
        current = q.top()
        pos = current.pos
        dist = current.dist
        q.pop()
        for m in moves:
            new_pos = (pos[0]+m[0],pos[1]+m[1])
            if valid_position(new_pos) and new_pos not in s:
                if new_pos == dest: return current
                s.add(new_pos)
                q.push(position(new_pos,dist+1,current))
    return -1    
if __name__=='__main__':
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(0)
    while True:
        turtle.clear()
        draw_board()
        src = (-1,-1)
        dest = (-1,-1)
        while src[0] < 0 or src[0] > 8 or src[1] < 0 or src[1] > 8:
            srctext=turtle.textinput("INITIAL POSITION","ENTER THE INITIAL POSITION :")
            if srctext is None: sys.exit(0)
            try:
                src = tuple(map(int,srctext.split()))
            except:
                src = (-1,-1)
        draw_board(src)
        draw_knight(src)
        while dest[0] < 0 or dest[0] > 8 or dest[1] < 0 or dest[1] > 8:
            desttext=turtle.textinput("DESIRED POSITION","ENTER THE DESIRED POSITION :")
            if desttext is None: sys.exit(0)
            try:
                dest = tuple(map(int,desttext.split()))
            except:
                dest = (-1,-1)
        draw_board(src,dest)
        draw_knight(dest)
        current = minimum_knight_move(src,dest)
        s = LinkedList()
        s.insert_at_head(dest)
        mlist = list()
        while current is not None:
            s.insert_at_head(current.pos)
            current = current.parent
        for pos in s:
            turtle.clear()
            mlist.append(pos)
            draw_board(src,dest,mlist)
            draw_knight(pos)
            time.sleep(2)
            turtle.update()