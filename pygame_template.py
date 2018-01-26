
import pygame
import random

black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)
pygame.init()
# Set the width and height of the screen [width,height]
size=[700,500]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Fox fucks up.")
#Loop until the user clicks the close button.
done=False
# Used to manage how fast the screen updates
clock=pygame.time.Clock()
FPS=60
#Loading images below.
r=random.randint(1,100)
colour=white
width=random.randint(0,50)


kirlist=[]
foolist=[]

# -------- Main Program Loop -----------
while done==False:

     for event in pygame.event.get(): # User did something
         if event.type == pygame.QUIT: 
             done=True
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_UP:
                 colour = red
                 
             if event.key ==   pygame.K_LEFT:
                 colour = green
             if event.key == pygame.K_DOWN:
                 colour = white
             if event.key == pygame.K_RIGHT:
                 colour = black
             if event.key == pygame.K_1 and width < r :
                  width+=1
             if event.key == pygame.K_2 and width < r and width > 0:
                  width-=1
         if event.type == pygame.MOUSEBUTTONDOWN:  
                   


               
          
                   if event.button == 4 :
                      r+=1
                      
                   if event.button == 5 and width <> 0 and r > width:
                      r-=1
                   if event.button == 1:
                       
                       kirlist.append([r,width,colour,pygame.mouse.get_pos()])
                       
                       lolcol=random.randint(1 ,3)
                       if lolcol == 1:
                            colour = red
                       if lolcol == 2:
                            colour = green
                       if lolcol == 3:
                            colour = white

                        
              
     
         

     
     while width > r:
         width = random.randint(0,4)
     
     # above this, or they will be erased with this command.
     screen.fill(black)
     for i in range(len(kirlist)):
                    
                    if  kirlist[i][0]>kirlist[i][1] :
                         kirlist[i][0]-=random.randint(0,1)
                         

                         pygame.draw.circle(screen, kirlist[i][2],kirlist[i][3],kirlist[i][0],kirlist[i][1])
                         while kirlist[i][1] > kirlist[i][0]:
                              kirlist[i][1] = random.randint(0,4)
                    else:
                           foolist=[x for x in kirlist if x in [kirlist[i]]]
                           
                         
                    

                    
                    
                    
     pygame.draw.circle(screen, colour, pygame.mouse.get_pos(), r, width)
     
     kirlist=[x for x in kirlist if x not in foolist]
     pygame.display.flip()
     clock.tick(FPS)
     

pygame.quit ()
