
 
import pygame
 

black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
blue     = (   0,   0, 255)
skyblue  = ( 135, 206, 250)
 
pygame.init()
  
size = [700,500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Fox does stuff")

FPS=60 

done = False



clock = pygame.time.Clock()



                
class Stalk:
    def __init__(self,x,y,x2,y2,w,h,nowalk):
        self.x = x/w*w
        self.y = y/h*h
        self.x2 = x2/w*w
        self.y2 = y2/h*h
        self.w = w
        self.h = h
        self.found = False
        self.temp_parent=int
        self.openlist=[((self.x,self.y),(self.x,self.y))]
        self.closedlist={}
        self.twodelete=[]
        self.pathlist=[]
        self.nowalk=nowalk
        self.nowalk.append((self.x2,self.y2))
        self.done=False
        self.dead=False
    def fway(self,a,b):
        return ((a,b-self.h),(a,b+self.h),(a+self.w,b),(a-self.w,b),(a,b))
        
    def find(self,a,b):
        
        for i in range(4):
            if ((self.fway(a,b)[i],self.fway(a,b)[4]) not in self.openlist) and (self.fway(a,b)[i] not in self.nowalk):
                self.openlist.append((self.fway(a,b)[i],self.fway(a,b)[4]))
            
        
        
            if self.fway(a,b)[i]==(self.x2,self.y2):
                    self.found = True
                    
                
                    if self.fway(a,b)[i] not in self.pathlist:
                        self.pathlist.append((self.fway(a,b)[i]))
                        if (a,b) not in self.pathlist:
                            self.pathlist.append((a,b))
                        self.temp_parent=(a,b)
                
    def chartpath(self,do):
        
        if do and not(self.done):
            while self.pathlist[-1]<>(self.x,self.y):
                self.makeme()
            self.pathlist=self.pathlist[::-1]
            
            self.done=True
            
    
    def makeme(self):
        for i in self.closedlist:
            if i==self.temp_parent:
                self.pathlist.append(self.closedlist[i])
                self.temp_parent=self.closedlist[i]
    def chart(self):
        if not(self.found):
            for i in range(len(self.openlist)):
                self.find(self.openlist[i][0][0],self.openlist[i][0][1])
                self.closedlist[(self.openlist[i][0][0],self.openlist[i][0][1])]=(self.openlist[i][1][0],self.openlist[i][1][1])
        for i in range(len(self.openlist)):
            if self.openlist[i][0] in self.closedlist:
                self.twodelete.append(self.openlist[i])
        for i in range(len(self.twodelete)):
            del self.openlist[self.openlist.index(self.twodelete[i])]

        self.twodelete=[]

        self.chartpath(self.found)
    
        for i in range(len(self.pathlist)):
            for j in range(len(self.pathlist)):
                if self.pathlist[i]==self.pathlist[j] and j<>i:
                    del self.pathlist[i]
                    break
            break
        for i in range(len(self.pathlist)):
            if self.pathlist[i]==(self.x,self.y):
                del self.pathlist[i]
                
                break
        if self.done and not (self.pathlist is None):
            return self.pathlist
    
    def blit(self):
        for i in range(len(self.nowalk)):
            pygame.draw.rect(screen,(0,0,0),[self.nowalk[i][0],self.nowalk[i][1],self.w,self.h])
        for i in range(len(self.pathlist)):
            pygame.draw.rect(screen,(255,255,255),[self.pathlist[i][0],self.pathlist[i][1],self.w,self.h])
            
def finalfind(x,y,x2,y2,w,h,nw):
    zero=Stalk(0,0,0,0,32,32,[])    
    current=1000
    for i in range(len(zero.fway(x2,y2))-1):
        one=Stalk(x,y,zero.fway(x2,y2)[i][0],zero.fway(x2,y2)[i][1],w,h,nw)
        while not(one.dead):
            print 'z'
            if not(one.chart() is None) and not(one.dead):
                if len(one.pathlist)<current:
                    current=len(one.pathlist)
                one.dead=True
    one.blit()
    return one.pathlist
    
# -------- Main Program Loop -----------
while done == False:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                done = True
            
    screen.fill(skyblue)

    finalfind(52,123,324,145,32,32,[(12,123)])
            

            
    
    pygame.display.flip()
 
    clock.tick(FPS)

pygame.quit()


#    pygame.draw.rect(screen,blue,[x,y,w,h])
#    for i in range(len(openlist)):
#        pygame.draw.rect(screen,green,[openlist[i][0][0],openlist[i][0][1],w,h])
#        pygame.display.flip()
        
        
#    for i in closedlist:
#        pygame.draw.rect(screen,black,[i[0],i[1],w,h])
#        pygame.display.flip()
    
#    for i in range(len(nowalk)):
#        pygame.draw.rect(screen,black,[nowalk[i][0],nowalk[i][1],w,h])
#    pygame.draw.rect(screen,red,[x2,y2,w,h])    
#    for i in range(len(pathlist)):
#        pygame.draw.rect(screen,white,[pathlist[i][0],pathlist[i][1],w,h])
#        pygame.display.flip()
#        wait()
    
#    if current<len(pathlist) and len(pathlist)<>0:
#        x,y=pathlist[current]
#        current+=1


##    if not(found):      
##        for i in range(len(openlist)):
##            find(openlist[i][0][0],openlist[i][0][1])
##            closedlist[(openlist[i][0][0],openlist[i][0][1])]=(openlist[i][1][0],openlist[i][1][1])
##    
##    for i in range(len(openlist)):
##        if openlist[i][0] in closedlist:
##            twodelete.append(openlist[i])
##            
##            
##    for i in range(len(twodelete)):
##        del openlist[openlist.index(twodelete[i])]
##       
##    twodelete=[]
##    
##    chartpath(found)
##    
##    for i in range(len(pathlist)):
##        for j in range(len(pathlist)):
##            if (pathlist[i]==pathlist[j] and j<>i):
##                del pathlist[i]
##                break
##        break
##    
##    for i in range(len(pathlist)):
##        if pathlist[i]==(x,y):
##            del pathlist[i]
##            break
        
##x,y=400,300
##x2,y2=600,100
##w,h=32,32
##x=x/w*w
##y=y/h*h
##x2=x2/w*w
##y2=y2/h*h
##nowalk=[(x2-w,y2+h),(x2-w*2,y2)]

##temp_parent=int
##openlist=[((x,y),(x,y))]
##closedlist={}
##twodelete=[]
##pathlist=[]
##
##def wait():
##    pygame.time.wait(50)#1/4
##def fway(x,y):
##    return ((x,y-h),(x,y+h),(x-w,y),(x+w,y),(x,y))
##    
##def find(x,y):
##    global x2,y2,openlist,closedlist,found,temp_parent,nowalk
##    for i in range(4):
##        if ((fway(x,y)[i],fway(x,y)[4]) not in openlist) and (fway(x,y)[i] not in nowalk):
##            openlist.append((fway(x,y)[i],fway(x,y)[4]))
##            
##    if fway(x,y)[i]==(x2,y2):
##            found=True
##            if (x,y) not in pathlist:
##                pathlist.append((x,y))
##            temp_parent=(x,y)
##            
##            
##    
##        
##def chartpath(do):
##    global pathlist,temp_parent,x,y,found
##    if do:
##         while pathlist[-1]<>(x,y):
##             makeme()
##         pathlist=pathlist[::-1]
##         found=False
##  
##def makeme():
##    global temp_parent
##    for i in closedlist:
##            if i==temp_parent:
##                pathlist.append(closedlist[i])
##                temp_parent=closedlist[i]
##                
##
##                
##x2=x2/w*w
##y2=y2/h*h
    
##nowalk=[(x2-w,y2+h),(x2-w*2,y2),(x2,y2)]                
