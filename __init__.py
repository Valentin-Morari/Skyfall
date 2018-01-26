
import pygame


black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)

pygame.init()


size=[700,500]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Tile Editor")

done=False


# -------- Main Program Loop -----------
while done==False:

     for event in pygame.event.get(): # User did something
         if event.type == pygame.QUIT: 
             done=True
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_F1:
                done=True                
                
                
                
                
                
                
                
                
     pygame.display.flip()
     
     

pygame.quit ()
