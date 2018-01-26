
# Sample Python/Pygame Programs                                                       #Semi-finished?
# Simpson College Computer Science
# http://cs.simpson.edu
import pygame,random
# Define some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)
pygame.init()
# Set the width and height of the screen [width,height]
size=[300,100]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Trippy trips.  333")
#Loop until the user clicks the close button.
done=False
# Used to manage how fast the screen updates
clock=pygame.time.Clock()

#Loading images below.


List=[] #Instances.
lisT=[] #Stepx'es. and Y?? 's.
deadlisT=[] #Used for holding the propper direction.
y=0 #Overarching WHY?
stepx=0 #Yeah.
s=10  #Value for shotspeed?
t=40#Value for FPS.
ranonce=0 #So it doesn't error with deadlisT
rand=int() #Apparently the most important thing. J/k used for - or + directions.
# -------- Main Program Loop -----------
while done==False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
     for event in pygame.event.get(): # User did something
         if event.type == pygame.QUIT: # If user clicked close
             done=True
         if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_DOWN and s>0:  #Shospd+
                   s-=1 #Possible number of directions is smaller.
                   deadlisT=lisT #Get all the + and - directions.
                   lisT=[] #New slate, new beggings.
                   #No fucking idea.
                   y=0 #Revamp of the y's.
                   
                   
              elif event.key == pygame.K_UP: #Shotspd-
                   s+=1
                   deadlisT=lisT
                   lisT=[]
                   
                   y=0
                   
              elif event.key == pygame.K_LEFT and t>10: #FPS-
                   t-=10
              elif event.key == pygame.K_RIGHT:  #FPS+
                   t+=10
              elif event.key == pygame.K_RETURN: #Reverse.
                    for i in range(len(lisT)):
                         

                         lisT[i]=-lisT[i]
                    print "Pendulum swing. Reverse the flow of fate!"
                         
                   # Flag that we are done so we exit this loop
     # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
     # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
     # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
     # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
     # First, clear the screen to white. Don't put other drawing commands
     # above this, or they will be erased with this command.
     screen.fill(black)
     while len(List)<size[1]:
         x=random.randint(0,size[0])
         
         
         List.append([x,y])
         
         y+=1
      
     if len(lisT)<size[1]:
          
          for i in range(len(List)):

               
              if s>-1:
                   drpstepx=random.randint(0,s)
              if s>0:
                   drpstepx=random.randint(1,s)
              rand=random.randint(0,1)
              if rand>0:
                  drpstepx=-drpstepx 
              if ranonce==1:
                   if deadlisT[i]<0:
                        if drpstepx>0:
                             drpstepx=-drpstepx
                   if deadlisT[i]>0:
                       if drpstepx<0:
                            drpstepx=-drpstepx
                                
              
              lisT.append(drpstepx)
              deadlisT.append(drpstepx)
          ranonce=1   

     for i in range(len(List)): #BLITTER.
          
         screen.set_at((List[i]),(255,255,255))
         
     for i in range(len(List)):
         List[i][0]+=lisT[i]                                                     #SUGOI. BOUNCE+ACCELERATION.
         if List[i][0]>size[0]:
              lisT[i]=-lisT[i]
         if List[i][0]<0:
              lisT[i]=-lisT[i]                     #NYEH /(^o^)\
              

          
   
     print s,t 

     # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
     # Go ahead and update the screen with what we've drawn.
     pygame.display.flip()
     # Limit to 20 frames per second
     clock.tick(t)
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
