
import pygame
import random

from skyfall import *

black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)
skyblue	 = ( 94, 188, 244)

pygame.init()

filename='map3'

try:
	open_map = open('maps/'+filename+'.txt', 'r+')
except:
	open_map = open('maps/'+filename+'.txt', 'w+')

	

goalcamX,goalcamY,camX,camY=0,0,0,0

grass_img=pygame.image.load("Grass.png").convert()
obstacle_img=pygame.image.load("obstacle.png").convert()
obstacle_img.set_colorkey(red)
blank=pygame.image.load("blank_tile.png").convert()
blank.set_colorkey(white)

w=blank.get_width()
h=blank.get_height()
grass2_img=pygame.image.load("Grass2.png").convert()
grasshole=pygame.image.load('grasshole.png').convert()
grasshole.set_colorkey(white)
grasslone=pygame.image.load('grasslone.png').convert()
grasslone.set_colorkey(white)
grasst=pygame.image.load("Grasstop.png").convert()
grasst.set_colorkey(white)
grassd=pygame.image.load("Grassdo.png").convert()
grassd.set_colorkey(white)
grasslt=pygame.image.load("Grasslt.png").convert()
grasslt.set_colorkey(white)
grassrt=pygame.transform.flip(grasslt,True,False)
grassld=pygame.transform.flip(grasslt,False,True)
grassrd=pygame.transform.flip(grassrt,False,True)
grassl=pygame.image.load("Grassl.png").convert()
grassl.set_colorkey(white)
grassr=pygame.transform.flip(grassl,True,False)
nclu=pygame.image.load("nocornerl2.png").convert()
nclu.set_colorkey(white)
ncru=pygame.transform.flip(nclu,True,False)
ncld=pygame.transform.flip(nclu,False,True)
ncrd=pygame.transform.flip(nclu,True,True)
grass3_img=pygame.image.load("Grass3.png").convert()
selector=grass_img
playerspawn=pygame.image.load("playerspawn.png").convert()
blocked=pygame.image.load("blocked.png").convert()
infected={0:blank,1:grass_img,2:obstacle_img,3:grasst,4:grassd,5:grasslt,6:grassrt,7:grassld,8:grassrd,9:grassl,10:grassr,11:nclu,12:ncld,13:ncru,14:ncrd,15:grasshole,16:grasslone,17:grass2_img,18:grass3_img,-1:playerspawn,-2:blocked,-3:foxf}
uniques=[playerspawn,foxf]

matrix1 = [[0]*(size[0]/w*2) for i in range(size[1]/h*2)]

def tween():
	global goalcamX,goalcamY,camX,camY
	if (goalcamX,goalcamY) <> (camX,camY):
		locked=False
	else:
		locked=True
		
	if not locked:
		camX += (goalcamX - camX) * 0.05
		camY += (goalcamY - camY) * 0.05
		
def become(number):
	global selector
	for key in infected.keys():
		if key==number:
			return infected[key]
				
def printrix():
	for y in range(len(matrix1)):
		 print matrix1[y]
	print '~ end ~'

def screenfull(matrix):
	global camX,camY
	blitlist=[]
	for y in range(len(matrix)):
		
		for x in range(len(matrix[y])):
			
			if become(matrix[y][x]).get_height()>h:
				
				blitlist.append([become(matrix[y][x]),x*w,y*h])
			else:
				screen.blit( become(matrix [y] [x]) ,(x*w-camX,y*h-camY))
			
				
	for blit in blitlist:
		screen.blit(blit[0],(blit[1]-camX,blit[2]-blit[0].get_height()+h-camY))


def getnum():
	global infected,selector
	for a,b in infected.items():
			if selector==b:
				wixoss=a
	return wixoss
	
def unique_tiles(which,where):
	for y in range(len(where)):
		for x in range(len(where[y])):
			if where[y][x]==which and (become(which) in uniques):
				where[y][x]=0
				break
	
	
	 
juxtapose=False
matrix2=[[0]*len(matrix1[0]) for i in range(len(matrix1))]

try:
	matrix1=eval(open_map.readline())
except:
	print 'something went wrong opening the map in the map section'
try:
	matrix2=eval(open_map.readline())
except:
	print 'something went wrong opening the map in the data section'
	
scroll_speed = 0.75

current_matrix=matrix1
if __name__=='__main__':
# -------- Main Program Loop -----------
	while done==False:
		 
		 for event in pygame.event.get(): 
			 if event.type == pygame.QUIT: 
				 done=True
			 if event.type == pygame.KEYDOWN:
				 if event.key == pygame.K_F1:
					open_map.close()
					done=True		   
				 elif event.key == pygame.K_1:
					 selector=become(0)
				 elif event.key == pygame.K_2:
					 selector=become(1)
				 elif event.key == pygame.K_3:
					 selector=become(2)
				 elif event.key == pygame.K_4:
					 selector=become(3)
				 elif event.key == pygame.K_5:
					 selector=become(4)
				 elif event.key == pygame.K_6:
					 selector=become(5)
				 elif event.key == pygame.K_7:
					 selector=become(6)
				 elif event.key == pygame.K_8:
					 selector=become(7)
				 elif event.key == pygame.K_9:
					 selector=become(8)
					 
				 elif event.key == pygame.K_q:
					 selector=become(9)
				 elif event.key == pygame.K_w:
					 selector=become(10)
				 elif event.key == pygame.K_e:
					 selector=become(11)
				 elif event.key == pygame.K_a:
					 selector=become(12)
				 elif event.key == pygame.K_s:
					 selector=become(13)
				 elif event.key == pygame.K_d:
					 selector=become(14)
				 elif event.key == pygame.K_z:
					 selector=become(15)
				 elif event.key == pygame.K_x:
					 selector=become(16)
				 elif event.key == pygame.K_c:
					selector=become(17)
				 elif event.key == pygame.K_v:
					selector=become(18)
				 elif event.key == pygame.K_l:
					selector=become(-1)
				 elif event.key == pygame.K_k:
					selector=become(-2)
				 elif event.key == pygame.K_m:
					selector=become(-3)
				 elif event.key == pygame.K_F2:
					current_matrix=matrix1
				 elif event.key == pygame.K_F3:
					current_matrix=matrix2
				 elif event.key == pygame.K_F4:
					juxtapose=not(juxtapose)
				 elif event.key == pygame.K_o:
					
					 try:
						 filename=raw_input('Open wat?')
						 open_map = open('maps/'+filename+'.txt', 'r+')
					 
						 matrix1=eval(open_map.readline())
						 open_map.close() 
						 
						 
					 except:
						 print 'error, no such map found, try again'
						 
				 elif event.key == pygame.K_p:
					 open_map = open('maps/'+filename+'.txt', 'r+')
					 open_map.write(str(matrix1))
					 open_map.write('\n')
					 open_map.write(str(matrix2))
					 open_map.close()
					 print 'saved'
					 
					 
				 elif event.key == pygame.K_BACKQUOTE:
					 matrix1 = [[0]*(size[0]/w) for i in range(size[1]/h)]
				 
			 if pygame.mouse.get_pressed()[0]: 
			 
				 for y in range(len(matrix1)):
					for x in range(len(matrix1[y])):
						
						if tx/w==x and ty/h==y:
							
							if getnum()<=0 and current_matrix==matrix2:
								unique_tiles(getnum(),matrix2)
								matrix2[y][x]=getnum()
							if getnum()>=0 and  current_matrix==matrix1:
								matrix1[y][x]=getnum()
							
			 elif pygame.mouse.get_pressed()[2]:
				 for y in range(len(matrix1)):
					for x in range(len(matrix1[y])):
						if ty/h==y:
							if getnum()<0 and current_matrix==matrix2:
								unique_tiles(getnum(),matrix2)
								matrix2[y][x]=getnum()
							elif getnum()>=0 and  current_matrix==matrix1:
								matrix1[y][x]=getnum()
							
			
				
						
		 
		 
		 mx,my=pygame.mouse.get_pos()[0]+camX,pygame.mouse.get_pos()[1]+camY
		 tx,ty=int(mx/w*w),int(my/h*h)
		 
		 smx,smy=pygame.mouse.get_pos()
		 stx,sty=smx*w/w,smy*h/h
		 
		 
		 if pygame.mouse.get_pressed()[1]:
			goalcamX,goalcamY=mx- ( len(matrix1[0])*w/(2*(len(matrix1)*h)/screen.get_height()) * scroll_speed ),my-( len(matrix1)*h/(2*(len(matrix1)*h)/screen.get_height()) * scroll_speed )
		 
		 tween()
		 
		 
		 screen.fill(skyblue)
		 screenfull(current_matrix) 
		 
		 if juxtapose:
			current_matrix=matrix1
			screenfull(current_matrix) 
			pygame.display.flip()
			current_matrix=matrix2
			screenfull(current_matrix) 
			pygame.display.flip()
			
		 
		 

		 
		 if selector.get_height()>h:
			screen.blit(selector,(stx,sty-selector.get_height()+h))
		 else:
			screen.blit(selector,(stx,sty))
		 
		 
		 
		 
		 
		 
		 
		 # printrix()
		 pygame.display.flip()
		 

	pygame.quit ()
