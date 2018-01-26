#!/usr/bin/env python

import pygame,random,sys,math

syi=0
tki=''
n=1
black	 = (   0,	0,	 0)
white	 = ( 255, 255, 255)
green	 = (   0, 255,	 0, 255)
red		 = ( 255,	0,	 0, 255)
blue	 = (   0,	0, 255)
skyblue	 = ( 96, 164, 208)

pygame.init()
  
size = [630,600]
screen = pygame.display.set_mode(size,pygame.NOFRAME)
 
pygame.display.set_caption("S K Y F A L L")

FPS=60

pygame.mixer.init()

done = False
 
clock = pygame.time.Clock()
time_counter = pygame.time.Clock()


music=1
sfx=1.5



# Image load!

player_img = pygame.image.load("Player.png").convert()

player_img.set_colorkey(white)

time_player_img=pygame.image.load("Time_Player.png").convert()
time_player_img.set_colorkey(white)
testah = pygame.image.load("blank.png")
nostah = pygame.image.load("fake.png").convert()
trap = pygame.image.load("trap.png").convert()
trap.set_colorkey(white)

grass_img=pygame.image.load("Grass.png").convert()
grass2_img=pygame.image.load("Grass2.png").convert()
walk_img=pygame.image.load("walk.png").convert()
run_img=pygame.image.load("run.png").convert()
weak_img=pygame.image.load("weak.png").convert()
strong_img=pygame.image.load("STRONG.PNG").convert()

global gw,gh
gw = grass_img.get_width()
gh = grass_img.get_height()

skullfront_img=pygame.image.load("skullfront.png").convert()
skullfront_img.set_colorkey(black)
skullback_img=pygame.image.load("skullback.png").convert()
skullback_img.set_colorkey(black)
skullleft_img=pygame.image.load("skullleft.png").convert()
skullleft_img.set_colorkey(black)
skullright_img=pygame.image.load("skullright.png").convert()
skullright_img.set_colorkey(black)
golemfront=pygame.image.load("golemfront.png").convert()
golemfront.set_colorkey(green)
golemback=pygame.image.load("golemback.png").convert()
golemback.set_colorkey(green)
golemright=pygame.image.load("golemright.png").convert()
golemright.set_colorkey(green)
golemleft=pygame.image.load("golemleft.png").convert()
golemleft.set_colorkey(green)

defines=[]
for n in range(4):
	definer_img=pygame.image.load("definer"+str(n+1)+".png").convert()
	definer_img.set_colorkey(green)
	defines.append(definer_img)
	
static_definer_img=defines[0]
	
skill_select_img=pygame.image.load("selector.png").convert()
skill_select_img.set_colorkey(white)
definer_img=pygame.image.load("definer"+str(n)+".png").convert()
definer_img.set_colorkey(green)
hp_img=pygame.image.load("hp.png").convert()
hp_img.set_colorkey(white)
nohp_img=pygame.image.load("nohp.png").convert()
nohp_img.set_colorkey(white)
dexbuff_img=pygame.image.load("dexbuff.png").convert()
dexbuff_img.set_colorkey(white)
hpbuff_img=pygame.image.load("hpbuff.png").convert()
hpbuff_img.set_colorkey(white)
attackbuff_img=pygame.image.load("attackbuff.png").convert()
attackbuff_img.set_colorkey(white)
speedbuff_img=pygame.image.load("speedbuff.png").convert()
speedbuff_img.set_colorkey(white)

weak2=pygame.image.load("weak2.png").convert()
weak2.set_colorkey(green)
strong2=pygame.image.load("strong2.png").convert()
strong2.set_colorkey(green)
walk2=pygame.image.load("walk2.png").convert()
walk2.set_colorkey(green)
run2=pygame.image.load("run2.png").convert()
run2.set_colorkey(green)
strup=pygame.image.load("strup.png").convert()
strup.set_colorkey(green)
hpup=pygame.image.load("hpup.png").convert()
hpup.set_colorkey(green)
spdup=pygame.image.load("spdup.png").convert()
spdup.set_colorkey(green)
dexup=pygame.image.load("dexup.png").convert()
dexup.set_colorkey(green)


arrowr=pygame.image.load("arrowr.png").convert()
arrowr.set_colorkey(black)
arrowl=pygame.image.load("arrowl.png").convert()
arrowl.set_colorkey(black)
arrowu=pygame.image.load("arrowu.png").convert()
arrowu.set_colorkey(black)
arrowd=pygame.image.load("arrowd.png").convert()
arrowd.set_colorkey(black)
playerl=pygame.image.load("charmodelleftx.png").convert()
playerl.set_colorkey(black)
playerr=pygame.image.load("charmodelrightx.png").convert()
playerr.set_colorkey(black)
playeru=pygame.image.load("charmodelbackx.png").convert()
playeru.set_colorkey(black)
playerd=pygame.image.load("charmodelfrontx.png").convert()
playerd.set_colorkey(black)


cloud1=pygame.image.load("cloud1.png").convert()
cloud2=pygame.image.load("cloud2.png").convert()
cloud3=pygame.image.load("cloud3.png").convert()
cloud4=pygame.image.load("cloud4.png").convert()
cloud5=pygame.image.load("cloud5.png").convert()
cloud6=pygame.image.load("cloud6.png").convert()
cloud1.set_colorkey(black)
cloud2.set_colorkey(black)
cloud3.set_colorkey(black)
cloud4.set_colorkey(black)
cloud5.set_colorkey(black)
cloud6.set_colorkey(black)

grass_img=pygame.image.load("Grass.png").convert()
obstacle_img=pygame.image.load("obstacle.png").convert()
obstacle_img.set_colorkey(red)
blank=pygame.image.load("blank_tile.png").convert()
blank.set_colorkey( (94,188,244))


grasslone=pygame.image.load("grasslone.png").convert()
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

infected={0:blank,1:grass_img,2:obstacle_img,3:grasst,4:grassd,5:grasslt,6:grassrt,7:grassld,8:grassrd,9:grassl,10:grassr,11:nclu,12:ncld,13:ncru,14:ncrd,16:grasslone}

bomb=pygame.image.load("bomb.png").convert()
bomb.set_colorkey(white)

hp_img.set_alpha(150)

walkable_tiles_list=['grass']

active_creatures_list=['Time_Player']
active_creatures_time={}

cloud_list=[]

enemy_list=[]
projectile_list=[]
buff_list=[]

skill_names=['walk','run','weak','strong']
images={'walk':walk2,'run':run2,'weak':weak2,'strong':strong2}
skill_delay={'walk':0,'run':0,'weak':0,'strong':0}
skill_supposed_delay={'walk':400,'weak':900}

trap_stats={'HP':1,'MP':1,'A':0,'CD':0}
golem_stats={'HP':800,'MP':1,'A':3,'1':1000,'2':1200,'3':2400,'ATT':150}
skull_stats={'HP':200,'MP':30,'A':2,'1':650,'2':1000,'ATT':100}
arrow_stats={'HP':1,'MP':1,'A':1,'CD':0,'1':30,'ATT':100}
bomb_stats={'HP':1,'MP':1,'A':1,'CD':0,'1':2100,'ATT':300}
decoy_stats={'HP':1,'MP':1,'A':0,'CD':0}
Time_Player_stats={'HP':700,'MP':500,'ATT':40}
poison_stats={'HP':25,'MP':1,'A':0,'CD':0,'1':500}
locked_stats={'HP':500,'MP':1,'A':0,'CD':0,'1':500}
burned_stats={'HP':1,'MP':1,'A':0,'CD':0,'1':500}
skull_stats['MAXHP']=skull_stats['HP']
golem_stats['MAXHP']=golem_stats['HP']
bomb_stats['MAXHP']=bomb_stats['HP']
Time_Player_stats['INITHP']=Time_Player_stats['HP']
data={'skull':skull_stats,'Time_Player':Time_Player_stats,'arrow':arrow_stats,'bomb':bomb_stats,'decoy':decoy_stats,'poisoned':poison_stats,'locked':locked_stats,'trap':trap_stats}
data2={'burned':burned_stats,'golem':golem_stats}

data.update(data2)

sky=pygame.image.load("skyneo.png").convert()
obstacle_img=pygame.image.load("obstacle.png").convert()
obstacle_img.set_colorkey(red)

skyblue=sky.get_at((0,sky.get_height()-1))
skill_clocks={}

unwalkable_projectiles=['arrow','decoy','trap']
skill_selector='walk'
enemy_types={'skull':'normal','golem':'miniboss'}
fly_order=[]

open_map=open('maps/map2.txt','r')
the_map=eval(open_map.read())
open_map.close()

blinking={}

global floatY,blink_duration

blink_duration=50
floatY = 0
maxFloat = 3
floatStep = 0.05
floatyFloatY = 0

def stats_update():
	Time_Player_stats['SATT']=Time_Player_stats['ATT']*2+Time_Player_stats['ATT']/2
	Time_Player_stats['MAXHP']=Time_Player_stats['HP']
	skill_supposed_delay['run']=skill_supposed_delay['walk']*3
	skill_supposed_delay['strong']=skill_supposed_delay['weak']*3
	
stats_update()

def change_speed(by):
	
	for i in range(data['skull']['A']):
		data['skull'][str(i+1)]=data['skull'][str(i+1)]/by
	for i in range(data['golem']['A']):
		data['golem'][str(i+1)]=data['golem'][str(i+1)]/by
	

	
def clicked(x,y,where,what=''):
	global d,h,s,a,leveled,switch
	
	if where=="buff":
		
		if pygame.Rect(h,hpup.get_size()).collidepoint(x,y):
			what='hp'
			
		if pygame.Rect(a,strup.get_size()).collidepoint(x,y):
			what='att'
			
		if pygame.Rect(d,dexup.get_size()).collidepoint(x,y):
			what='dex'
			
		if pygame.Rect(s,spdup.get_size()).collidepoint(x,y):
			what='spd'
			
			
		if what=='hp':
			Time_Player_stats['MAXHP']+=Time_Player_stats['INITHP']/2
			Time_Player_stats['HP']=Time_Player_stats['MAXHP']
			
			leveled=False
			switch=True
		elif what=='att':
			Time_Player_stats['ATT']+=Time_Player_stats['ATT']/4
			Time_Player_stats['SATT']=Time_Player_stats['ATT']*2+Time_Player_stats['ATT']/2

			leveled=False
			switch=True
		elif what=='dex':
			skill_supposed_delay['weak']-=skill_supposed_delay['weak']/3
			skill_supposed_delay['strong']-=skill_supposed_delay['strong']/3

			leveled=False
			switch=True
		elif what=='spd':
			skill_supposed_delay['walk']-=skill_supposed_delay['walk']/5
			skill_supposed_delay['run']-=skill_supposed_delay['run']/5
				
			leveled=False
			switch=True
			
		
			  
def topontop():
	a=False
	c=0
	
	for i in range(len(enemy_list)):
		for j in range(len(enemy_list)):
			
			if (enemy_list[j].tilex==enemy_list[i].tilex and enemy_list[j].tiley==enemy_list[i].tiley) and j<>i: #matters whether tile, tile=tilepos, x,y=blitpos
				a=True
				
	for i in range(len(tile_list)):
		for j in range(len(enemy_list)):
			if (enemy_list[j].tilex==tile_list[i].x and enemy_list[j].tiley==tile_list[i].y) and (tile_list[i].type not in walkable_tiles_list):
			   a=True
			   
	return a
	
	

		
	
	
def check_pos():	
	for i in range(len(enemy_list)):
		while topontop() or (enemy_list[i].tilex==time_player.tilex and enemy_list[i].tiley==time_player.tiley):
			
			enemy_list[i].reposition()
			
			if not(topontop()) or (enemy_list[i].x<>time_player.x and enemy_list[i].y<>time_player.y):
				break
			
def levelUP():
	global switch,Time_Player_stats,level,leveled,d,h,s,a
	if level<>1 and leveled:
		x=size[0]/4
		y=size[1]/2-dexup.get_height()/2
		
		switch=False
		
		d=x,y
		x+=size[0]/50+dexup.get_width()
		h=x,y
		x+=size[0]/50+dexup.get_width()
		s=x,y
		x+=size[0]/50+dexup.get_width()
		a=x,y
		x+=size[0]/50+dexup.get_width()
		
		screen.blit(dexup,(d))
		screen.blit(hpup,(h))
		screen.blit(spdup,(s))
		screen.blit(strup,(a))
		

def delay_motherfucker(name):
	
	skill_clocks[name]=pygame.time.Clock()
	
def no_cooldown(name):
	if name in skill_clocks:
		return True
	else:
		return False
		
def final_countdown():	  
		global tempus,turn
		for i in range(len(skill_names)):

			if skill_names[i] in skill_clocks and turn=='Time_Player':
				
				skill_delay[skill_names[i]]+=tempus
				
				
				if skill_delay[skill_names[i]]>skill_supposed_delay[skill_names[i]]:

					del skill_clocks[skill_names[i]]
					skill_delay[skill_names[i]]=0
			
		
		for i in range(len(skill_names)):
			if skill_names[i] in images:
				if skill_names[i] in skill_clocks:
					images[skill_names[i]].set_alpha(75)
				elif skill_names[i] not in skill_clocks:
					images[skill_names[i]].set_alpha(255)
					
def recolour(image,replace,new):
	newimage=image.copy()
	for x in range(image.get_width()):
		for y in range(image.get_height()):
			if image.get_at((x,y))==replace:
				newimage.set_at((x,y),new)
	return newimage
	
class Buff:
	def __init__(self,name,parent,target,duration,when,allbut):
		
		self.name=name
		self.parent=parent
		self.parent_name=self.parent.name
		self.target=target
		
		if self.name not in self.target.afflicted:
			self.target.afflicted+=self.name
			
		self.data=data[self.name].copy()
		self.lifespan=self.data['1']*duration
		self.dead=False
		
		
		if when=='parent':
			self.when=self.parent_name
		elif when=='target':
			try: 
				self.when=self.target.surname
			except:
				self.when=self.target.name
			
		self.allbut=allbut
		
		if self.name=='burned':
			self.target.data['ATT']=self.target.data['ATT']/2
			
		if self.name=='locked':
				if self.target.name<>'Time_Player':
					self.target.CD['1']+=self.data['HP']*duration
					
				else:
					for skill in skill_names:
						if skill=='run' or skill == 'walk':
							delay_motherfucker(skill)
							skill_delay[skill]-=self.data['HP']*duration
					
	def count_time(self):
		
		global turn,tempus

		
		if not(self.dead):
			time='not prime'
			
			if self.allbut:
				if turn<>self.when:
					time='prime'
			else:
				if turn==self.when:		 
					time='prime'
					
			
			if time=='prime':
				
				if self.data['CD']>0:
						
					self.data['CD']-=tempus
						
					if self.lifespan>0:
							
						self.lifespan-=tempus
							
					else:
							
						self.dead=True
							
						if self.name=='burned':
								
							self.target.data['ATT']=self.target.data['ATT']*2
							
					 
	def move(self):
			if not(self.dead):
				time='not prime'
				if self.allbut:
					if turn<>self.when:
						time='prime'
				else:
					if turn==self.when:
						time='prime'
						
				if time=='prime':		 
					
					if self.data['CD']<=0:
						self.data['CD']=self.data['1']
							
						if self.name=='poisoned':
							self.target.HP-=self.parent.data['ATT']/2+self.parent.data['ATT']/6
							blinkify(self.target)
								
						
				
def r_calc_tile(target):
			target.x=target.tilex+gw/2-target.image.get_width()/2
			target.y=target.tiley+gh/2-target.image.get_height()
			
							
					   

			
class Projectile:
	def __init__(self,name,x,y,direction,parent,extra):
		self.name=name
		self.direction=direction
		self.image=image(self.direction,self.name,self)
		self.x=x+gw/2-self.image.get_width()/2
		self.y=y+gh/2-self.image.get_height()
		self.parent=parent
		self.dead=False
		self.extra=extra
		self.data=data[self.name].copy()
		self.parent_name=self.parent.name
		self.tilex=self.x-gw/2+self.image.get_width()/2
		self.tiley=self.y-gh/2+self.image.get_height()
		
		for i in range(len(enemy_list)):
				if enemy_list[i].tilex==self.tilex and enemy_list[i].tiley==self.tiley:
						self.dead=True
			
		try:
			self.data['CD']=self.data['1']
			
		except:
			pass
		
		if self.name=='bomb':
			self.data['CD']+=self.extra
		
		
		self.tilex=self.x-gw/2+self.image.get_width()/2
		self.tiley=self.y-gh/2+self.image.get_height()
		
		
		#don't stack arrows 
		
		#for projectile in projectile_list:
			#if projectile.tilex==self.tilex and projectile.tiley==self.tiley and projectile<>self and self.name == 'arrow':
				#self.dead=True
				
		#don't trap+arrow
		
		for projectile in projectile_list:
			if projectile.tilex==self.tilex and projectile.tiley==self.tiley and projectile <> self and (self.name=='trap' or projectile.name=='trap'):
				self.dead=True
				
	def calc_tile(self):
		self.tilex=self.x-gw/2+self.image.get_width()/2
		self.tiley=self.y-gh/2+self.image.get_height()
		
	
	def hpbar(self):
		try:
			
			
			screen.blit(pygame.transform.smoothscale(nohp_img,(nohp_img.get_width()/4,nohp_img.get_height()/2)),(self.x+self.image.get_width()/2-nohp_img.get_width()/8-camX,self.y-nohp_img.get_height()/2-nohp_img.get_height()/4+floatY-camY))	 #Protip: it's the smaller version, the image isn't this small originally
			screen.blit(pygame.transform.smoothscale(recolour(recolour(hp_img,(69,160,46),(0,110,255)),(0,63,2),(18,49,80)),((self.data['CD']*hp_img.get_width()/4)/self.data['1'],hp_img.get_height()/2)),(self.x+self.image.get_width()/2-nohp_img.get_width()/8-camX,self.y-nohp_img.get_height()/2-nohp_img.get_height()/4+floatY-camY))
		except:
			pass
			
	
	def definer(self,definer):
		if not(self.dead):
			screen.blit(recolour(definer,red,blue),(self.tilex-camX,self.tiley+floatY-camY))	  
		
	def blit(self):
		r_calc_tile(self)
		if not(self.dead):
			self.image=image(self.direction,self.name,self)
			screen.blit(self.image,(self.x-camX,self.y+floatY-camY))
			
	def count_time(self):
		global turn,tempus
		
		if self.data['CD']>0:
			
			if turn<>self.parent_name:
			   self.data['CD']-=tempus
	def dommage(self,x,y):
		
		nineway=((x-gw,y),(x,y-gh),(x+gw,y),(x,y+gh),(x,y))
		
		for i in range(len(enemy_list)):
				if (enemy_list[i].tilex,enemy_list[i].tiley) in nineway:
					
					enemy_list[i].HP-=data[self.parent_name]['SATT']
					
					
					blinkify(enemy_list[i])
					
					a=Buff('burned',self.parent,enemy_list[i],4,'target',False)
					buff_list.append(a)
					
	def kaboom(self):
		if not(self.dead):
			self.dommage(self.tilex,self.tiley)
			
			for projectile in projectile_list:
				
				if (projectile.tilex,projectile.tiley) in fway(self.tilex,self.tiley) or (projectile.tilex==self.tilex and projectile.tiley==self.tiley and projectile<>self):
					if projectile.name == 'bomb':
						
						self.dommage(projectile.tilex,projectile.tiley)
						projectile.dead=True
						
			self.dead=True				 
			
			if self.name<>"decoy":
				sound("bomb.wav")
	
	def move(self):
		global turn
		
		if turn<>self.parent_name and self.data['CD']<=0:
			if self.name == 'trap':
				for enemy in enemy_list:
					if enemy.tilex==self.tilex and enemy.tiley==self.tiley:
						blinkify(enemy)
						a=Buff('locked',self.parent,enemy,1,'target',False)
						sound("trap.wav")
						buff_list.append(a)
						enemy.HP-=self.parent.data['ATT']
						self.dead=True
						
			

						
							
			if not(self.dead):
				
				if self.name=='arrow' and self==fly_order[0]:
					if self.direction=='right':
						self.x+=gw
					elif self.direction=='left':
						self.x-=gw
					elif self.direction=='up':
						self.y-=gh
					elif self.direction=='down':
						self.y+=gh
						
					self.calc_tile()
				elif self.name=='bomb':
					self.kaboom()
					pass
					
			if self.name=='arrow':
				for i in range(len(enemy_list)):
					if enemy_list[i].tilex==self.tilex and enemy_list[i].tiley==self.tiley:
						enemy_list[i].HP-=data[self.parent_name]['ATT']
						blinkify(enemy_list[i])
						self.dead=True
						sound("arrow.wav")
						
						if self.extra=='locking':
							a=Buff('locked',self.parent,enemy_list[i],1,'target',False)
							buff_list.append(a)
				



					
			if self.name<>'decoy' and self.name<>'trap':
				self.data['CD']=self.data['1']
		
			
		if (self.x<0-gw or self.x>size[0]+gw) or (self.y<0-gh or self.y>size[1]+gh):
			self.dead=True
			

			

class Enemy:
	def __init__(self,name,x,y,str_apon,hpbar_show,definer_show,direction):
		self.type=enemy_types[name]
		self.afflicted=''
		self.hpbar_show=hpbar_show
		self.definer_show=definer_show
		self.name=name
		self.surname=name+str_apon
		self.data=data[self.name].copy()		
		self.HP=self.data['HP']
		self.MP=self.data['MP']
		self.MAXHP=self.data['MAXHP']
		self.dead=False
		self.direction=direction
		self.action=1
		self.image=image(self.direction,self.name,self)
		self.x=x/gw*gw+gw/2-self.image.get_width()/2
		self.y=y/gh*gh-self.image.get_height()+gh/2
		self.tilex=self.x-gw/2+self.image.get_width()/2
		self.tiley=self.y+self.image.get_height()-gh/2
		self.CD={}
		for i in range(self.data['A']):
			self.CD[str(i+1)]=0
		self.path = []
		self.target=()
		
		self.floatY = 0
		self.maxFloat = 2
		self.floatStep = 0.05
		self.floatyFloatY = 0

		if self.name == 'skull':
			self.floatY = round(random.uniform(-self.maxFloat,self.maxFloat))

	def reposition(self):
		print self.tilex,self.tiley,time_player.tilex,time_player.tiley
		potential_tiles=[]
	
		for tile in tile_list:
			if tile.type in walkable_tiles_list:
				potential_tiles.append(tile)
				
		which_tile=random.randint(0,len(potential_tiles)-1)
		self.tilex=potential_tiles[which_tile].x
		self.tiley=potential_tiles[which_tile].y
		
		r_calc_tile(self)
		
	def blit(self):
	
		if not(self.dead):
			self.image=image(self.direction,self.name,self)
			
			
			if self.name == 'skull':
				
				if abs(self.floatY) >= self.maxFloat:
					self.floatStep = - self.floatStep
				
				self.floatyFloatY += self.floatStep
			
				self.floatY = round(self.floatyFloatY)
			
			screen.blit(self.image,(self.x-camX,self.y+floatY+self.floatY-camY))		  
			
	def define(self,definer):
		if not(self.dead) and self.definer_show:
			screen.blit(definer,(self.x-gw/2+self.image.get_width()/2-camX,self.y+self.image.get_height()-gh/2+floatY-camY))	  
			   
	def hpbar(self):
		
		try:
			if not(self.dead) and self.hpbar_show:
				if self.type=='normal':
					screen.blit(pygame.transform.smoothscale(nohp_img,(nohp_img.get_width()/4,nohp_img.get_height()/2)),(self.x+self.image.get_width()/2-nohp_img.get_width()/8-camX,self.y-nohp_img.get_height()/2-nohp_img.get_height()/4+floatY+self.floatY-camY))
					screen.blit(pygame.transform.smoothscale(recolour(recolour(hp_img,(69,160,46),(224,49,49)),(0,63,2),(81,18,19)),((self.HP*hp_img.get_width()/4)/self.MAXHP,hp_img.get_height()/2)),(self.x+self.image.get_width()/2-nohp_img.get_width()/8-camX,self.y-nohp_img.get_height()/2-nohp_img.get_height()/4+floatY+self.floatY-camY))
				elif self.type=='miniboss':
					screen.blit(pygame.transform.smoothscale(nohp_img,(nohp_img.get_width()/2,nohp_img.get_height()/2)),(self.x+self.image.get_width()/2-nohp_img.get_width()/4-camX,self.y-nohp_img.get_height()/2-nohp_img.get_height()/4+floatY+self.floatY-camY))
					screen.blit(pygame.transform.smoothscale(recolour(recolour(hp_img,(69,160,46),(173,0,197)),(0,63,2),(138,0,156)),((self.HP*hp_img.get_width()/2)/self.MAXHP,hp_img.get_height()/2)),(self.x+self.image.get_width()/2-nohp_img.get_width()/4-camX,self.y-nohp_img.get_height()/2-nohp_img.get_height()/4+floatY+self.floatY-camY))


		except:
			pass
	
		
										
	def calc_tile(self):
		self.tilex=self.x-gw/2+self.image.get_width()/2
		self.tiley=self.y+self.image.get_height()-gh/2
		
		
	def behavior(self): #The big glossary of shit monstas can do to ya!
		
		global turn,buff_list
		
		if turn==self.surname:
			wherex=time_player.tilex
			wherey=time_player.tiley
			
			
			for i in range(len(projectile_list)):
				if projectile_list[i].name=='decoy':
						wherex=projectile_list[i].tilex
						wherey=projectile_list[i].tiley
			
			if len(self.path) == 0 and (wherex,wherey) not in fway(self.tilex,self.tiley):
				self.path=finalfind(self.tilex,self.tiley,wherex,wherey,gw,gh)
				
										
			
		
			if self.CD['1']<=0: #Chase you			  
				
				
				if len(self.target) > 0:
					
				
								oldx=self.x
								oldy=self.y
								self.tilex=self.target[0]
								self.tiley=self.target[1]
								
								if oldy>self.y:
									self.direction='up'
								elif oldy<self.y:
									self.direction='down'
								if oldx>self.x:
									self.direction='left'
								elif oldx<self.x:
									self.direction='right'
								
								self.CD['1']=self.data['1']
								r_calc_tile(self)
								self.target = ()
								self.path=finalfind(self.tilex,self.tiley,wherex,wherey,gw,gh)

							
								
							
			if self.CD['1']<=0: #Chase you
						
						
						DONE=False
						
						
						
						
						self.path=finalfind(self.tilex,self.tiley,wherex,wherey,gw,gh)
								
						if not((wherex,wherey) in fway(self.tilex,self.tiley)):
									
									oldx=self.x
									oldy=self.y
									
									self.x=self.path[0][0]/gw*gw+gw/2-self.image.get_width()/2
									self.y=self.path[0][1]/gh*gh-self.image.get_height()+gh/2
									self.path.pop(0)
									
									if oldy>self.y:
										self.direction='up'
									elif oldy<self.y:
										self.direction='down'
									if oldx>self.x:
										self.direction='left'
									elif oldx<self.x:
										self.direction='right'
									
									self.CD['1']=self.data['1']
									self.calc_tile()

						
									
						   

			if self.CD['2']<=0: #Basic attack
								if (self.tilex==wherex and (self.tiley==wherey+gh or self.tiley==wherey-gh)) or (self.tiley==wherey and (self.tilex==wherex+gw or self.tilex==wherex-gw)):
									if time_player.tilex<>wherex or time_player.tiley<>wherey:
										for i in range(len(projectile_list)):
											if projectile_list[i].name=='decoy':
												projectile_list[i].data['HP']-=self.data['ATT']
												blinkify(projectile_list[i])
												
												
									else:
										data['Time_Player']['HP']-=self.data['ATT'] 
										blinkify(time_player)
									
									if self.tilex<wherex:
										self.direction='right'
									elif self.tilex>wherex:
										self.direction='left'
										
									if self.tiley<wherey:
										self.direction='down'
									elif self.tiley>wherey:
										self.direction='up'
									
										
									self.CD['2']=self.data['2']			   
									
			if self.name=='golem':
				
				if self.CD['3'] <= 0 and (wherex,wherey) not in fway(self.tilex,self.tiley):  #Pull target towards self ALSO a check whether it's necessary
					if time_player.tilex == wherex and time_player.tiley == wherey:
					#Check if pullable
						pull = Pull(self,time_player,3)
						if pull:
							if pull[0]:
								time_player.tilex = self.tilex + gw*pull[0]
								
							else:
								time_player.tiley = self.tiley + gh*pull[1]
								
								
							self.CD["3"] = self.data['3']
							r_calc_tile(time_player)
						
						
					else:
						for p in projectile_list:
							if p.name == 'decoy':
								pull = Pull(self,p,3)
								if pull:
									if pull[0]:
										p.tilex = self.tilex + gw*pull[0]
										
									else:
										p.tiley = self.tiley + gh*pull[1]
										
									self.CD["3"] = self.data['3']
									r_calc_tile(p)
									
					
					original = (self.tilex,self.tiley)
					self.target = ()
					
					#Check if a step in any direction would make pullable
				
					for coord in fway(self.tilex,self.tiley):
						for tile in tile_list:
							if tile.x == coord[0] and tile.y == coord[1] and tile.type in walkable_tiles_list:
								self.tilex = coord[0]
								self.tiley = coord[1]
								
								if time_player.tilex == wherex and time_player.tiley == wherey:
									pull = Pull(self,time_player,3)
									if pull:
										
											self.target = coord
											self.tilex,self.tiley = original
											break
								else:
									for p in projectile_list:
										if p.tilex == wherex and p.tiley == wherey:
											pull = Pull(self,p,3)
											if pull:
										
												self.target = coord
												self.tilex,self.tiley = original
												break
											break
								break
									
					
						
			
	def count_time(self):
		global turn,tempus
		if turn==self.surname:
			for i in range(self.data['A']):
				if self.CD[str(i+1)]>0:
					self.CD[str(i+1)]-=tempus
			
def restart():
	global switch,time_player,player,walkable_tiles_list,active_creatures_list,active_creatures_time,enemy_list,skill_names,images,skill_delay
	global skill_supposed_delay, skull_stats,Time_Player_stats,data,skill_clocks,skill_selector,skull,buffs,fly_order,consty
	global tile_list,find,switch,second_counter,default_time,turn,find_time,skill_number,target_tick,level,leveled,h,d,s,a,foes,projectile_list,tempus,cloud_list
	
	player.x=time_player.x
	player.y=time_player.y	   
	player.direction=time_player.direction
	leveled=False
	level+=1
	target_tick=0
	second_counter=0
	switch=True
	find=True
	find_time=True
	tock=0
	default_time=4
	turn='Time_Player'
	skill_number=1
	space_toggled=False

	d=size[0]/60,size[1]/40
	h=size[0]-(dexup.get_width()),size[1]/40
	s=size[0]/60,size[1]-(spdup.get_height())
	a=size[0]-dexup.get_width(),size[1]-spdup.get_height()
	
	
	
	
	Time_Player_stats['HP']=Time_Player_stats['MAXHP']
	time_player.dead=False
	walkable_tiles_list=['grass']



	active_creatures_list=['Time_Player']
	active_creatures_time={}

	enemy_list=[]
	projectile_list=[]
	fly_order=[]
	
	
	skill_clocks={}

	skill_selector='walk'
	howmanyclouds=18
	
	if len(cloud_list)<>howmanyclouds:
		for i in range(howmanyclouds):
			
			x=random.randint(size[0],int(size[0]+size[0]/3))
			consty=random.randint(0+sky.get_height()/2+sky.get_height()/4,size[1]-cloud2.get_height())
			stepx=random.randint(1,3)
			which=random.randint(1,3)
						
			if which==1:
				which=cloud1
			elif which==2:
				which=cloud2
			elif which==3:
				which=cloud3
			elif which==4:
				which=cloud4
			elif which==5:
				which=cloud5
			elif which==6:
				which=cloud6
							
				
			cloud_list.append([x,consty,stepx,which])
	level_barrier=3
	potential_tiles=[]
	for i in range(level):
		for tile in tile_list:
			if tile.type in walkable_tiles_list:
				potential_tiles.append(tile)
				
		which_tile=random.randint(0,len(potential_tiles)-1)
		enemyx=potential_tiles[which_tile].x
		enemyy=potential_tiles[which_tile].y
		
		if level==level_barrier or level==level_barrier*2 or level==level_barrier*3:
			
			for j in range(level_barrier):

				if level==level_barrier*(j+1):
					
					for x in range(j+1):
						
						golem=Enemy('golem',enemyx,enemyy,str(x),True,True,'down')
						enemy_list.append(golem)
						active_creatures_list.append(golem.surname)
						
					break
			break
				
			
					
					
		else:
			skull=Enemy('skull',enemyx,enemyy,str(i),True,True,'down')
			enemy_list.append(skull)
			active_creatures_list.append(skull.surname)

	stats_update()
	
camX,camY=0,0

class Tile:
	def __init__(self,type,x,y,id):
		self.type=type
		self.x=x
		self.y=y
		self.blitx=x
		self.blity=y
		self.id=id
		self.image=image('any',id,'world')
		
		self.camx=0
		self.camy=0
		if self.image.get_height()>gh:
			self.blity-=self.image.get_height()-gh
			
	def blit(self):
		if self.type <> 'empty':
			
			# self.camx=time_player.x - screen.get_width()/4
			# self.camy=screen.get_height()/2 - time_player.tiley/2
			
			screen.blit(self.image, (self.blitx-camX,self.blity+floatY-camY))
			
def Pull(initiator,target,maxDistance):

	directionx=0
	directiony=0
	distance=0
	coords = []
	X = initiator.tiley == target.tiley
	Y = initiator.tilex == target.tilex
	
	
	
	if X:
		if initiator.tilex < target.tilex :
			directionx = 1
		else:
			directionx = -1
	elif Y:
		if initiator.tiley < target.tiley :
			directiony = 1
		else:
			directiony = -1
	
	if directionx:
		distance = abs(initiator.tilex - target.tilex)/gw
	elif directiony:
		distance = abs(initiator.tiley - target.tiley)/gh
		
	if distance > maxDistance:
		distance = 0
	
	for i in range(distance):
		if directionx:
			coords.append(( ((initiator.tilex + (gw * (i+1))*directionx)),initiator.tiley ))
		elif directiony:
			coords.append((initiator.tilex, (initiator.tiley + (gh * (i+1) )*directiony) ))
	
	RED_FLAG = (directionx,directiony)
	
	if distance > 0:
		for tile in tile_list:
			if (tile.x,tile.y) in coords and tile.type not in walkable_tiles_list:
				RED_FLAG = False
		
		for enemy in enemy_list:
			if (enemy.tilex,enemy.tiley) in coords:
				RED_FLAG = False
		if (time_player.tilex,time_player.tiley) in coords:
			RED_FLAG = False
		
	else:
		RED_FLAG = False
		
		
		
	return RED_FLAG



def image(direction,who,author=None):
	global infected
	
	if (who=='Player') or (who=='Time_Player'):
		
		if direction=='up':
			img=playeru
		elif direction=='down':
			img=playerd
		elif direction=='left':
			img=playerl
		elif direction=='right':
			img=playerr
			
	elif who=='skull':
		
		if direction=='up':
			img=skullback_img
		elif direction=='down':
			img=skullfront_img
		elif direction=='left':
			img=skullleft_img
		elif direction=='right':
			img=skullright_img
			
	elif who=='arrow':
		if direction=='left':
			img=arrowl
		elif direction=='right':
			img=arrowr
		elif direction=='down':
			img=arrowd
		elif direction=='up':
			img=arrowu
			
	elif who=='bomb':
		if direction=='down' or direction=='left' or direction=='right' or direction=='up':
			img=bomb
			
	elif who=='decoy':
		if direction=='down':
			img=playerd
		elif direction=='up':
			img=playeru
		elif direction=='left':
			img=playerl
		elif direction=='right':
			img=playerr
			
	
		img=img.copy()
		img.set_alpha(150)
		
	elif who=='golem':
		if direction=='down':
			img=golemfront
		elif direction=='up':
			img=golemback
		elif direction=='left':
			img=golemleft
		elif direction=='right':
			img=golemright
	
	elif who in infected.keys():
		img=infected[who]
	
	elif who=='trap':
		img=trap
	
	img=img.copy()		  
	iw=img.get_width()
	ih=img.get_height()

		
	
	
		
	try:
		
		#if 'poisoned' in author.afflicted:
			#tint(img,'green',100)
		#elif 'burned' in author.afflicted:
			#tint(img,'red',75)
		#elif 'locked' in author.afflicted:
			#tint(img,'blue',100)
		pass
	except:
		pass	
		
	return img
	
def tint(source,how,how_much):
	iw=source.get_width()
	ih=source.get_height()
	for i in range(iw):
			for j in range(ih):
				current_color=source.get_at((i,j))
				if current_color<>source.get_colorkey():
					target=how_much
					var=0
					if how=='blue' or how=='green':
						while var<target and current_color[0]>0:
							var+=1
							current_color[0]-=1
					var=0
					if how == 'red' or how=='blue':
						while var<target and current_color[1]>0:
							var+=1
							current_color[1]-=1
					if how == 'green' or how=='red':
						while var<target and current_color[2]>0:
							var+=1
							current_color[2]-=1
							
					
					
					source.set_at((i,j),current_color)
	return source

class Player:
	
	def __init__(self,x,y):
		
		self.direction='down'
		self.afflicted=''
		self.image=image(self.direction,"Player",self)
		
		self.x=x/gw*gw+gw/2-self.image.get_width()/2
		self.y=y/gh*gh-self.image.get_height()+gh/2
				
	def blit(self):
		global camX,camY
		self.image=image(self.direction,"Player",self)
		screen.blit(self.image,(self.x-camX,self.y+floatY-camY))
		
	def walk(self,flag):
		
		if flag=='up':
			flagx=0
			flagy=-gh
		elif flag=='down':
			flagx=0
			flagy=gh
		elif flag=='left':
			flagy=0
			flagx=-gw
		elif flag=='right':
			flagy=0
			flagx=gw
			
		for i in tile_list:
				if (self.tilex+flagx)==i.x and (self.tiley+flagy)==i.y and i.type in walkable_tiles_list:
					self.y+=flagy
					self.x+=flagx
					self.direction=flag
					self.calc_tile(True)
					break
		
	def calc_tile(self,found):
		global find
		if found==True:
			self.tilex=self.x-gw/2+self.image.get_width()/2
			self.tiley=self.y+self.image.get_height()-gh/2
			
			for i in range (len(tile_list)):
				if (self.tilex==tile_list[i].x) and (self.tiley==tile_list[i].y):
					
					find=False

def sound(path):
	global sfx,music
	s=pygame.mixer.Sound(path)
	s.set_volume(sfx)
	s.play()
	
class Time_Player:
	def __init__(self,x,y):
		self.direction='down'
		self.afflicted=''
		self.name='Time_Player'
		self.image=image(self.direction,"Time_Player",self)
		self.tilex=x/gw*gw
		self.tiley=y/gh*gh
		self.x=x/gw*gw+gw/2-self.image.get_width()/2
		self.y=y/gh*gh-self.image.get_height()+gh/2
		self.dead=False
		self.job='warrior'
		self.class_change('default','warrior')
		self.data=data[self.name].copy()
		
	def blit(self):
		self.image=image(self.direction,"Time_Player",self)
		screen.blit(self.image,(self.x-camX,self.y+floatY-camY))
		
	def status_check(self,status):
		if status in self.afflicted:
			return True
		else:
			return False
	def class_change(self,old,new):
		if old=='rogue':
			Time_Player_stats['HP']=Time_Player_stats['HP']*2
			Time_Player_stats['ATT']=Time_Player_stats['ATT']*2
			skill_supposed_delay['walk']=skill_supposed_delay['walk']*2
			skill_supposed_delay['weak']=skill_supposed_delay['weak']*2
			
		elif old=='warrior':
			Time_Player_stats['HP']=Time_Player_stats['HP']/2
			skill_supposed_delay['walk']=skill_supposed_delay['walk']/3
			skill_supposed_delay['weak']=skill_supposed_delay['weak']/2
			

		elif old=='archer':
			skill_supposed_delay['weak']=skill_supposed_delay['weak']*2
			Time_Player_stats['HP']=Time_Player_stats['HP']*2
			Time_Player_stats['ATT']=Time_Player_stats['ATT']
			
		elif old=='mage':
			Time_Player_stats['ATT']=Time_Player_stats['ATT']
			skill_supposed_delay['weak']=skill_supposed_delay['weak']/3
			skill_supposed_delay['walk']=skill_supposed_delay['walk']
			
		if new=='warrior':
			Time_Player_stats['HP']=Time_Player_stats['HP']*2
			skill_supposed_delay['walk']=skill_supposed_delay['walk']*3
			skill_supposed_delay['weak']=skill_supposed_delay['weak']*2
			
		elif new=='rogue':
			Time_Player_stats['HP']=Time_Player_stats['HP']/2
			Time_Player_stats['ATT']=Time_Player_stats['ATT']/2
			skill_supposed_delay['weak']=skill_supposed_delay['weak']/2
			skill_supposed_delay['walk']=skill_supposed_delay['walk']/2
			
		elif new=='archer':
			Time_Player_stats['HP']=Time_Player_stats['HP']/2
			Time_Player_stats['ATT']=Time_Player_stats['ATT']
			skill_supposed_delay['weak']=skill_supposed_delay['weak']/2
			
		elif new=='mage':
			Time_Player_stats['ATT']=Time_Player_stats['ATT']
			skill_supposed_delay['weak']=skill_supposed_delay['weak']*3
			skill_supposed_delay['walk']=skill_supposed_delay['walk']
			
		
		stats_update()
		
		
		
	def turns(self):
		global turn,second_counter
		
		
		
		if active_creatures_time[turn]==second_counter:
			if turn <> 'Time_Player':
				for enemy in enemy_list:
					if enemy.surname == turn :
						enemy.path = []
				
			if active_creatures_list.index(turn)+1==len(active_creatures_list):
				turn=active_creatures_list[0]
			else:
				turn=active_creatures_list[active_creatures_list.index(turn)+1]
			second_counter=1
			
	def calc_tile(self,found_time):
		global find_time
		if found_time:
			self.tilex=self.x-gw/2+self.image.get_width()/2
			self.tiley=self.y+self.image.get_height()-gh/2
			
			for i in range (len(tile_list)):
				if (self.tilex==tile_list[i].x) and (self.tiley==tile_list[i].y):
					find_time=False
					
	def walk_check(self,x,y):
	
		allowed=True
					
		for i in range(len(enemy_list)):
			if self.tilex+x==enemy_list[i].tilex and self.tiley+y==enemy_list[i].tiley:
				allowed=False
				break
				
		for i in range(len(projectile_list)):
			if projectile_list[i].name in  unwalkable_projectiles:
				if self.tilex+x==projectile_list[i].tilex and self.tiley+y==projectile_list[i].tiley:
					allowed=False
					break
					
		return allowed
				
	def walk(self,flag,name):			 
		
		if name not in skill_clocks and turn=='Time_Player':
			#flagx=flag[0]
			#flagy=flag[1]
				
			if flag=='up':
				flagx=0
				flagy=-gh
			elif flag=='down':
				flagx=0
				flagy=gh
			elif flag=='left':
				flagy=0
				flagx=-gw
			elif flag=='right':
				flagy=0
				flagx=gw
				
			if name=='walk' :  
				delay_motherfucker(name)
				if self.walk_check(flagx,flagy):
					for i in tile_list:
							if (i.x==self.tilex+flagx and i.y==(self.tiley+flagy)) and i.type in walkable_tiles_list:
								self.y+=flagy
								self.x+=flagx
								sound("grasstep.wav")
								self.calc_tile(True)
								break
					
				self.direction=flag
				
				
				
				
				
			elif name=='run' :
				
				delay_motherfucker(name)
				if self.walk_check(flagx*2,flagy*2):
						
						for i in tile_list:
								if i.x==self.tilex+flagx*2 and i.y==(self.tiley+flagy*2) and i.type in walkable_tiles_list:
									self.y+=flagy*2
									self.x+=flagx*2
									sound("grassrun.wav")
									self.calc_tile(True)
									break
				
									
				self.direction=flag
				
					
			elif name=='weak' and (self.job=='warrior' or self.job=='rogue'):
				delay_motherfucker(name)
				for i in range(len(enemy_list)):
						if enemy_list[i].tilex==self.tilex+flagx and enemy_list[i].tiley==self.tiley+flagy:
							enemy_list[i].HP-=data['Time_Player']['ATT']
							blinkify(enemy_list[i])
				
									
							self.direction=flag
							
							if self.job=='rogue':
								sound("cut.wav")
							else:
								sound("lsword.wav")
					
					
			elif name=='strong' and self.job=='rogue':
				delay_motherfucker(name)
				no = False
				
				for i in range(len(enemy_list)):
						if enemy_list[i].tilex==self.tilex+flagx and enemy_list[i].tiley==self.tiley+flagy:
							a=Buff('poisoned',self,enemy_list[i],4,'parent',True)
							buff_list.append(a)
							enemy_list[i].HP-=data['Time_Player']['ATT']/2
							blinkify(enemy_list[i])
							sound("scut.wav")
							for tile in tile_list:
								if (self.tilex+flagx*2,self.tiley+flagy*2) == (tile.x,tile.y) and tile.type in walkable_tiles_list:
									for enemy in enemy_list:
										if (self.tilex+flagx*2,self.tiley+flagy*2) == (enemy.tilex,enemy.tiley):
											no=True
											
									if not no:
										self.tilex = self.tilex+flagx*2
										self.tiley = self.tiley+flagy*2
									r_calc_tile(self)
									break
							
				
				self.direction=flag
						
							
			elif name=='strong' and self.job=='warrior':
					delay_motherfucker(name)
					blocked=False
					hit=False
					minusx,minusy=0,0
					
					for i in range(5):
						for j in range(len(enemy_list)):
							if self.tilex+flagx*i==enemy_list[j].tilex and self.tiley+flagy*i==enemy_list[j].tiley:
								
								if flagy<>0:
									minusy=-flagy
								if flagx<>0:
									minusx=-flagx
									
								for l in tile_list:
									if l.x==self.tilex+flagx*i+minusx and l.y==(self.tiley+flagy*i+minusy) and l.type in walkable_tiles_list:
												for k in range(i-1):
													for tile in tile_list:
														
														if tile.x==self.tilex+flagx*(k+1)+minusx and tile.y==self.tiley+flagy*(k+1)+minusy and tile.type not in walkable_tiles_list:
															blocked=True
															break
															
												if not(blocked):
													self.y+=flagy*i+minusy
													self.x+=flagx*i+minusx
													
													
													self.calc_tile(True)
													enemy_list[j].HP-=data['Time_Player']['SATT']
													blinkify(enemy_list[j])
													
													a=Buff('locked',self,enemy_list[j],1,'target',False)
													buff_list.append(a)
													hit=True
									
													break
												
								self.direction=flag
									
								break
								
						if hit:
							sound("sword.wav")
							break
				
			elif name=='weak' and self.job=='archer':
					delay_motherfucker(name)
				
					a=Projectile('arrow',time_player.tilex+flagx,time_player.tiley+flagy,flag,self,False)
					self.direction=flag
					
					if not a.dead:
						sound("arrowput.wav")
					
					
					
					fly_order.append(a)
					projectile_list.append(a)
				
			elif name=='strong' and self.job=='archer':
					delay_motherfucker(name)
				
					a=Projectile('trap',time_player.tilex+flagx,time_player.tiley+flagy,flag,self,False)
					self.direction=flag
					triggered=False
					
					for tile in tile_list:
						if tile.type not in walkable_tiles_list and (a.tilex==tile.x and a.tiley==tile.y):
							triggered=True
	
					
					
					
					
					if not(triggered):
						projectile_list.append(a)
						sound("trapset.wav")
					
			elif name=='weak' and self.job=='mage':
					delay_motherfucker(name)
					triggered=False
				
					a=Projectile('bomb',time_player.tilex+flagx,time_player.tiley+flagy,flag,self,tock+1000*(second_counter-1))
					self.direction=flag
						
						
					for i in range(len(enemy_list)):
						if enemy_list[i].tilex==a.tilex and enemy_list[i].tiley==a.tiley:
								triggered=True
								
							
	
					
					for tile in tile_list:
						if tile.type not in walkable_tiles_list and (a.tilex==tile.x and a.tiley==tile.y):
							triggered=True
							
					for decoy in projectile_list:
						if decoy.name=='decoy':
							if decoy.tilex==a.tilex and decoy.tiley==a.tiley:
								triggered=True
					
					if not(triggered):
						projectile_list.append(a)		 
						sound("bombset.wav")
			
			elif name=='strong' and self.job=='mage':
					delay_motherfucker(name)
					triggered=False
				
					a=Projectile('decoy',time_player.tilex+flagx,time_player.tiley+flagy,flag,self,False)
					self.direction=flag
						
					for i in range(len(enemy_list)):
						if enemy_list[i].tilex==a.tilex and enemy_list[i].tiley==a.tiley:
								triggered=True
							

					
					for tile in tile_list:
						if tile.type not in walkable_tiles_list and (a.tilex==tile.x and a.tiley==tile.y):
							triggered=True
							
					for bomb in projectile_list:
						if bomb.name=='bomb':
							if bomb.tilex==a.tilex and bomb.tiley==a.tiley:
								triggered=True
								
					if not(triggered):
						projectile_list.append(a)		 
						sound("decoyappear.wav")
class Text:
	def __init__(self,x,y,font,size,words,AA,colour):
		self.x=x
		self.y=y
		self.font=font
		self.size=size
		self.words=words
		self.AA=AA
		self.colour=colour
	def create(self):
		self.Font = pygame.font.SysFont(self.font, self.size)
		self.text =self.Font.render(self.words, self.AA, self.colour)
	def blit(self):
		screen.blit(self.text, (self.x, self.y))

x=0
y=size[1]-gh*6

global tile_list,find,switch,second_counter,default_time,turn,find_time,skill_number,target_tick,level,leveled,h,d,s,a
d=size[0]/60,size[1]/40
h=size[0]-(dexup.get_width()),size[1]/40
s=size[0]/60,size[1]-(spdup.get_height())
a=size[0]-dexup.get_width(),size[1]-spdup.get_height()	  
leveled=False
level=0
target_tick=0
tile_list=[]
second_counter=1
switch=True
find=True
find_time=True
tock=0
default_time=4
turn='Time_Player'
skill_number=1
space_toggled=False
by=1

time_player=Time_Player(350,450)
player=Player(300,500)


for y in range(len(the_map)):
	for x in range(len(the_map[y])):
						
				if the_map[y][x]==1:					
					tile=Tile('grass',x*gw,y*gh,the_map[y][x])
					tile_list.append(tile)
					
				elif the_map[y][x]==0:
					
					tile=Tile('empty',x*gw,y*gh,the_map[y][x])
					tile_list.append(tile)
					
				elif the_map[y][x]==3 or the_map[y][x]==4 or the_map[y][x]==9 or the_map[y][x]==10 or the_map[y][x]==16:
					tile=Tile('grass',x*gw,y*gh,the_map[y][x])
					tile_list.append(tile)
				
				else:
					tile=Tile('obstacle',x*gw,y*gh,the_map[y][x])
					tile_list.append(tile)
#for i in range(1000):
	#random_obst=random.randint(0,100)
	#if random_obst>90:
		#if x==time_player.tilex and y==time_player.tiley:
		   #pass
		#else:
			#tile=Tile('obstacle',x,y)
			#tile_list.append(tile)
	#if random_obst<=90 or (x==time_player.tilex and y==time_player.tiley):
		#tile=Tile('grass',x,y)
		#tile_list.append(tile)
	#x+=gw
	#if x>=size[0]:
		#x=0
		#y+=gh
		
	#if y>=size[1]:
		#break
		
def four_way(place):
	return [(place[0],place[1]-gh),(place[0],place[1]+gh),(place[0]-gw,place[1]),(place[0]+gw,place[1])]






def create_skill_bar():
	distance_x=size[0]-walk2.get_width()*len(skill_names)-size[0]/25
	distance_y=size[1]-walk2.get_height()

	for i in range(len(skill_names)):
		if skill_names[i] in images:
			screen.blit(images[skill_names[i]],(distance_x,distance_y))
			if skill_selector==skill_names[i]:
				#screen.blit(skill_select_img,(distance_x,distance_y))	  #thing responsible for the skill selector
				pass
			distance_x+=size[0]/100+walk2.get_width()
			
		
def allow_time():
	for i in range(len(active_creatures_list)):
		active_creatures_time[active_creatures_list[i]]=default_time

def blit_order():
	blitlist={}
	sorted_blits=[]

	for i in range(len(enemy_list)):
		if enemy_list[i].image.get_height()>gh:
			enemy_list[i].calc_tile()
			blitlist[enemy_list[i]]=[enemy_list[i].tiley,enemy_list[i].tilex]
		
	for i in range(len(projectile_list)):
		if projectile_list[i].image.get_height()>gh:
			projectile_list[i].calc_tile()
			blitlist[projectile_list[i]]=[projectile_list[i].tiley,projectile_list[i].tilex]
			
	
	
	time_player.calc_tile(True)
	blitlist[time_player]=[time_player.tiley,time_player.tilex]
	
	sorted_values=sorted(blitlist.values()) 
	
	
	
	for value in sorted_values:
		for a,b in blitlist.items():
			if value==b:
				sorted_blits.append(a)
	
	for blit in sorted_blits:
		blit.blit()
		

class Stalk:
	def __init__(self,x,y,x2,y2,w,h,walk):
		self.x=x
		self.y=y
		self.x2=x2
		self.y2=y2
		self.w = w
		self.h = h
		self.found = False
		self.temp_parent=int
		self.openlist=[((self.x,self.y),(self.x,self.y))]
		self.closedlist={}
		self.twodelete=[]
		self.pathlist=[]
		self.walk=walk
		self.done=False
		self.dead=False
		self.name='default'
		
		for enemy in enemy_list:
			if x==enemy.tilex and y==enemy.tiley:
				self.name=enemy.name
				
		
	def fway(self,a,b):
		return ((a,b-self.h),(a,b+self.h),(a+self.w,b),(a-self.w,b),(a,b))
		
	def find(self,a,b):
		
		for i in range(4):
			if (((self.fway(a,b)[i],self.fway(a,b)[4]) not in self.openlist) and (self.fway(a,b)[i] in self.walk)):
				
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
		previous=0
		current=0
		
		while not(self.found):
			previous=len(self.closedlist)
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
			current = len(self.closedlist)
			
			if previous == current :
				self.done=True
				self.pathlist=[]
				break
				
		if self.done and self.pathlist is not None:
			return self.pathlist
	
	def blit(self):
		for i in range(len(self.walk)):
			pygame.draw.rect(screen,(0,0,0),[self.walk[i][0],self.walk[i][1],self.w,self.h])
		for i in range(len(self.pathlist)):
			pygame.draw.rect(screen,(255,255,255),[self.pathlist[i][0],self.pathlist[i][1],self.w,self.h])
			
global camx,camy
def count_time():
	global tock,second_counter,by
	names=[]
	
	for i in range(len(enemy_list)):
		
		names.append(enemy_list[i].surname)
			
	if turn in names:
		tock+=time_counter.tick()*by
	else:
		tock+=time_counter.tick()
		
	if tock>=1000:
		tock=0
		second_counter+=1
	
	
	
def visual_counter():
	if second_counter<>default_time:
		text=Text(size[0]/2,size[1]/20,"Gautami",40,str(second_counter),True,white)
	else:
		text=Text(size[0]/2,size[1]/20,"Gautami",40,str(second_counter),False,white)
	text.create()
	text.blit()
	
	
def level_counter():
	
	lvl_counter=Text(0+gw,size[1]-gh*2,"Gautami",40,str(level),True,black)
	lvl_counter.create()
	lvl_counter.blit()
	
def HPBARS(coords):
	for i in range(len(projectile_list)):
		if projectile_list[i].name=='bomb':
			projectile_list[i].hpbar()
			pass
	for i in range(len(enemy_list)):
		enemy_list[i].hpbar()
	try:
		screen.blit(pygame.transform.smoothscale(nohp_img,((Time_Player_stats['MAXHP']*hp_img.get_width())/Time_Player_stats['MAXHP']/2,hp_img.get_height()/2)),coords)
		screen.blit(pygame.transform.smoothscale(hp_img,(Time_Player_stats['HP']*Time_Player_stats['MAXHP']*hp_img.get_width()/Time_Player_stats['MAXHP']/Time_Player_stats['MAXHP']/2,hp_img.get_height()/2)),coords)
	except:
		pass
	


def blinkify(whom,duration=None):
	global blink_duration,blinking
	if duration==None:
		duration=blink_duration
		
	blinking[whom]=duration
	
def definer_judge(condition,literally_who):
	
	cleaner=[]
	for n in blinking:
		blinking[n]-=1
		
	for k in blinking:
		if blinking[k]<=0:
			cleaner.append(k)
		
	for i in range(len(cleaner)):
		del blinking[cleaner[i]]
	
	
	if literally_who in blinking:
	
		if (blinking[literally_who] / 10 ) % 3 == 1:
	
			return blank
			
			
	if condition:
		return definer_img
	else:
		return static_definer_img
	
	
		
def define(whom):
	if whom=="enemy":
		for i in range(len(enemy_list)):
			which_definer = definer_judge( turn==enemy_list[i].surname ,enemy_list[i] )
			enemy_list[i].define(recolour(which_definer,red,white))
	elif whom=="time_player":
		which_definer = definer_judge( turn=='Time_Player' ,time_player )
		screen.blit(recolour(which_definer,red,black),(time_player.x-gw/2+time_player.image.get_width()/2-camX,time_player.y+time_player.image.get_height()-gh/2+floatY-camY))
	elif whom=='projectile':
		
		for i in range(len(projectile_list)):
			if projectile_list[i].name<>'arrow':
				which_definer = definer_judge( turn <> projectile_list[i].parent_name, projectile_list[i] )
				projectile_list[i].definer(which_definer)
			
def enemy_blits():
	death=[]
	dead=[]
	global turn,second_counter
	for i in range(len(enemy_list)):

		
		enemy_list[i].blit()
		enemy_list[i].behavior()
		enemy_list[i].count_time()
		enemy_list[i].calc_tile()
		
		if enemy_list[i].HP<=0:
			enemy_list[i].dead=True
			if enemy_list[i] not in dead:
				dead.append(enemy_list[i])
			if enemy_list[i] not in death:
				death.append(enemy_list[i])		   
			
	if len(death)<>0:
		for i in range(len(death)):
				
				
				if death[i].surname==turn:
					
					if active_creatures_list.index(turn)+1==len(active_creatures_list):
						
						turn=active_creatures_list[0]
						
						
						
					else:
						
						turn=active_creatures_list[active_creatures_list.index(turn)+1]
						
					
					second_counter=0

				
				del enemy_list[enemy_list.index(death[i])]
			
				
		
		death=[]
	
	if len(dead)<>0:
		
		for i in range(len(dead)):
			
		
			
			del active_creatures_list[active_creatures_list.index(dead[i].surname)]
			del active_creatures_time[dead[i].surname]

		dead=[]
	
def buff_blits():
	dead=[]

	for buff in buff_list:
		if buff.dead:
			
			buff.target.afflicted=buff.target.afflicted.replace(buff.name,'')
			dead.append(buff)

		else:
			buff.count_time()
			buff.move()

	for buff in dead:
		del buff_list[buff_list.index(buff)]



def projectile_blits():
	death=[]
	no_decoys=-1
	
	for i in range(len(projectile_list)):
			projectile_list[i].blit()
			projectile_list[i].move()
			projectile_list[i].count_time()
			projectile_list[i].calc_tile()
	
				
	for i in range(len(projectile_list)):
		if projectile_list[i].name=='decoy':
			
			if no_decoys<>-1:
				death.append(projectile_list[no_decoys])
			no_decoys=i
	
	for projectile in projectile_list:
		if projectile.name=='decoy':
			if projectile.data['HP']<=0:
				for projectile in projectile_list:
					if projectile.name<>'decoy':
						#projectile.kaboom()
						pass
						
	for projectile in projectile_list:
		if projectile.data['HP']<=0 or projectile.dead:
			if projectile.name=="decoy":
				sound("decoygone.wav")
			death.append(projectile)
	
		
		
			
	if len(death)<>0:
		for i in range(len(death)):
			
			try:
				del fly_order[fly_order.index(death[i])]
			except:
				pass
			try:
				del projectile_list[projectile_list.index(death[i])]
			except:
				pass
			
		death=[]



def life_check():
	global turn,second_counter
	death=[]
	dead=[]
	no_decoys=-1
	
	if data['Time_Player']['HP']<=0:
		time_player.dead=True

	if time_player.dead:
		world_restart()
		
		
	if len(enemy_list)==0:
		global leveled
		
		world_restart()
		leveled=True
		
	

	
	
	
	
def update_time_creatures():
	allow_time()

global goalcamX,goalcamY
goalcamX,goalcamY=0,0

def tween():
	global goalcamX,goalcamY,camX,camY
	if (goalcamX,goalcamY) <> (camX,camY):
		locked=False
	else:
		locked=True
		
	if not locked:
		camX += (goalcamX - camX) * 0.05
		camY += (goalcamY - camY) * 0.05
		
def background_blit():
	global music,rev
	arbitrary_list_of_big_tiles=[]
	screen.fill(skyblue)
	screen.blit(pygame.transform.smoothscale(sky,(size[0],sky.get_height())),(0,0))
	for cloud in cloud_list:
		screen.blit(cloud[3],(cloud[0],cloud[1]))
		cloud[0]-=cloud[2]

	
	
	for i in range(len(tile_list)):
		if tile_list[i].image.get_height()<=gh:
			tile_list[i].blit()
		else:
			arbitrary_list_of_big_tiles.append(tile_list[i])
	for tile in arbitrary_list_of_big_tiles:
		tile.blit()
		
	
	levelUP()
	
	
		
	for cloud in cloud_list:
		if cloud[0]+cloud[3].get_width()<=0:
			x=random.randint(size[0],int(size[0]+size[0]/3))
			consty=random.randint(0+sky.get_height()/2+sky.get_height()/4,size[1]-cloud2.get_height())
			stepx=random.randint(1,3)
			which=random.randint(1,3)

			if which==1:
				which=cloud1
			elif which==2:
				which=cloud2
			elif which==3:
				which=cloud3
			elif which==4:
				which=cloud4
			elif which==5:
				which=cloud5
			elif which==6:
				which=cloud6
			
				
			cloud[0]=x
			cloud[1]=consty
			cloud[2]=stepx
			cloud[3]=which
			
	channel=pygame.mixer.Channel(2)
	
	stop=False
	
	
	#for cloud in cloud_list:						   #reverse time_clouds (needs work)
	
		#if cloud[0]+cloud1.get_width()<=0 or cloud[0]-cloud1.get_width()*2>=size[0]:
			#if cloud[0]+cloud1.get_width()<=0:
					
				#x=random.randint(size[0],size[0]+cloud1.get_width())
				#consty=random.randint(0+sky.get_height()/2+sky.get_height()/4,size[1]/2+cloud2.get_height()*2-cloud2.get_height()/2)
				#stepx=random.randint(1,3)
				#which=random.randint(1,3)
			#elif cloud[0]-cloud1.get_width()>=0:
				#x=0-cloud1.get_width()+1
				#consty=random.randint(0+sky.get_height()/2+sky.get_height()/4,size[1]/2+cloud2.get_height()*2-cloud2.get_height()/2)
				#stepx=random.randint(1,3)
				#which=random.randint(1,3)
	
	
	
	#if turn=='Time_Player':										 #Alternate music on turns
		#if pygame.mixer.Channel(2).get_busy() and rev:
			#pygame.mixer.Channel(2).stop()
			
		#rev=False
		
	#else:
		#if pygame.mixer.Channel(2).get_busy() and not(rev):
			#pygame.mixer.Channel(2).stop()
			
		#rev=True
	
	if rev and not(pygame.mixer.Channel(2).get_busy()):
		
		s=pygame.mixer.Sound("songy.wav")
		pygame.mixer.Channel(2).play(s)
		pygame.mixer.Channel(2).set_volume(music)
		
		
	# elif not(rev) and not(pygame.mixer.Channel(2).get_busy()):
		# s=pygame.mixer.Sound("songfull.wav")
		# pygame.mixer.Channel(2).play(s)								   #Don't play music as sound k.
		# pygame.mixer.Channel(2).set_volume(music)
		

	#if not(pygame.mixer.Channel(2).get_busy()):
			#contr=random.randint(0,3)
			#if contr==0:
				#s=pygame.mixer.Sound("songa.wav")
				#pygame.mixer.Channel(2).play(s)					   #Random music
				
			#elif contr==1:
				#s=pygame.mixer.Sound("songb.wav")
				#pygame.mixer.Channel(2).play(s)
				
			#elif contr==2:
				#s=pygame.mixer.Sound("songx.wav")
				#pygame.mixer.Channel(2).play(s)
				
			#elif contr==3:
				#s=pygame.mixer.Sound("songy.wav")
				#pygame.mixer.Channel(2).play(s)
				
	if level<>0:
		level_counter()
	   


def projectile_blit():
	for i in range(len(projectile_list)):
		projectile_list[i].blit()	 
	
		
def player_blits():
	player.calc_tile(find)
	player.blit()
	levelUP()

def different_blits():
	projectile_blits()
	enemy_blits()
	buff_blits()
	

def Time_Player_blits():
	count_time()
	time_player.calc_tile(find_time)
	define("time_player")	 
	define("enemy")
	define("projectile")
	update_time_creatures()
	time_player.turns()
	time_player.blit()
	HPBARS((time_player.x-gw/2+time_player.image.get_width()/2-camX,time_player.y-nohp_img.get_height()-nohp_img.get_height()/4+floatY-camY))
	different_blits()
	blit_order()
	create_skill_bar()
	visual_counter()
	final_countdown()
	life_check()





def SPACE(determinator):
	global skill_selector
	pygame.event.pump()
	key=pygame.key.get_pressed()
					
	if determinator=='move':
		if (key[pygame.K_SPACE]):
			skill_selector='run'
		elif not(key[pygame.K_SPACE]):
			skill_selector='walk'
	elif determinator=='attack':
		if (key[pygame.K_SPACE]):
			skill_selector='strong'
		elif not(key[pygame.K_SPACE]):
			skill_selector='weak'
			  



def world_restart():
	restart()
	
def finalfind(x,y,x2,y2,w,h):
	
	
	walkablelist=[]
	delete=[]
	current=1000
	
	for i in range(len(tile_list)):
		if not(tile_list[i].type not in walkable_tiles_list):
			walkablelist.append((tile_list[i].x,tile_list[i].y))
			
	for i in range(len(projectile_list)):
		if (projectile_list[i].tilex,projectile_list[i].tiley) in walkablelist and projectile_list[i].name=='arrow':
			delete.append((projectile_list[i].tilex,projectile_list[i].tiley))
			
		if projectile_list[i].name=='decoy':
			delete.append((time_player.tilex,time_player.tiley))
		
	for i in range(len(enemy_list)):
		if (enemy_list[i].tilex,enemy_list[i].tiley) in walkablelist:
			delete.append((enemy_list[i].tilex,enemy_list[i].tiley))
	
	delete.append((time_player.tilex,time_player.tiley))
	
	for i in range(len(delete)):
		if delete[i] in walkablelist:
			del walkablelist[walkablelist.index(delete[i])]
	
	
	ktar=0
	
	
	path=[]
	
	"""" test tiles """
	
	
		
	#screen.blit(nostah,(x2,y2))
	#pygame.display.flip()
	#pygame.time.wait(1000)
	
	

	one=Stalk(x,y,x2,y2,w,h,walkablelist)

	
	
	if one.chart() is not None :
					
					
					path=one.pathlist
					one.dead=True
					
		
		
	if len(path) == 0:
		path=[(x,y)]
	
	return path
def fway(x,y):
	
	
	return [(x+gw,y),(x,y+gh),(x-gw,y),(x,y-gh)]

	
by=2
change_speed(by)   
rev=False

z=pygame.time.Clock()

#hashtag #maps



def become(number):
	global selector
	for key in infected.keys():
		if key==number:
			return infected[key]



if __name__ == '__main__':

	# -------- Main Program Loop -----------
	while done == False:

			for event in pygame.event.get(): 
				if event.type == pygame.QUIT: 
					done = True
					 
				if not(switch):

					
					if event.type==pygame.MOUSEBUTTONDOWN:
						x,y= event.pos
						clicked(x,y,"buff")
						
				if event.type==pygame.KEYDOWN:
							
							if event.key==pygame.K_w:
								if not(switch):
									player.walk("up")
									find=True
									
								else:
									SPACE('move')
									time_player.walk("up",skill_selector)
									find_time=True						  
									
							elif event.key==pygame.K_s:
								if not(switch):
									player.walk("down")
									find=True
								else:
									SPACE('move')
									time_player.walk("down",skill_selector)
									find_time=True
									
							elif event.key==pygame.K_a:
								if not(switch):
									player.walk("left")
									find=True
								else:
									SPACE('move')
									time_player.walk("left",skill_selector)
									find_time=True
					
							elif event.key==pygame.K_d:
								if not(switch):
									player.walk("right")
									find=True
								else:
									SPACE('move')
									time_player.walk("right",skill_selector)
									find_time=True
									
				if switch:
					
								
					if event.type==pygame.KEYDOWN:
								
							if event.key==pygame.K_o:
								if by<2:
									by=2
									change_speed(by)

							elif event.key==pygame.K_p:
								if by>1:
									by=0.5
									change_speed(by)
									by=1
							elif event.key==pygame.K_1 and time_player.job<>'warrior':
								time_player.class_change(time_player.job,'warrior')
								time_player.job='warrior'
								print 'you is WARRIOR now'
							elif event.key==pygame.K_2 and time_player.job<>'rogue':
								time_player.class_change(time_player.job,'rogue')
								time_player.job='rogue'
								print 'you is ROGUE noa'
							elif event.key==pygame.K_3 and time_player.job<>'mage':
								time_player.class_change(time_player.job,'mage')
								time_player.job='mage'
								print 'now you a MAGE'
							elif event.key==pygame.K_4 and time_player.job<>'archer':
								time_player.class_change(time_player.job,'archer')
								time_player.job='archer'
								print 'ARCHER in da haus!'
								
							
									
							elif event.key==pygame.K_r:
								world_restart()
								leveled=True
								
							elif event.key==pygame.K_UP:
								SPACE('attack')
								time_player.walk("up",skill_selector)
								
							elif event.key==pygame.K_DOWN:
								SPACE('attack')
								time_player.walk("down",skill_selector)

							elif event.key==pygame.K_LEFT:
								SPACE('attack')
								time_player.walk("left",skill_selector)
								
							elif event.key==pygame.K_RIGHT:
								SPACE('attack')
								time_player.walk("right",skill_selector)
								
							elif event.key==pygame.K_q:
								#time_player.walk(0,'irony')
								pass
								
					elif event.type==pygame.MOUSEBUTTONDOWN:
						
						for i in range(len(tile_list)):
							if tile_list[i].x==pygame.mouse.get_pos()[0]/gw*gw and tile_list[i].y==pygame.mouse.get_pos()[1]/gh*gh:
		#						 print tile_list[i].x,tile_list[i].y
								
								 pass				
				
								
				if event.type==pygame.KEYDOWN:
						if not(switch) and leveled:
							if event.key==pygame.K_1:
								clicked(0,0,"buff",'dex')
							elif event.key==pygame.K_2:
								clicked(0,0,"buff",'hp')
							elif event.key==pygame.K_3:
								clicked(0,0,"buff",'spd')
							elif event.key==pygame.K_4:
								clicked(0,0,"buff",'att')
						if event.key==pygame.K_RETURN:
							 player.x=time_player.x
							 player.y=time_player.y		
							 player.direction=time_player.direction
							 switch=not(switch)
						elif event.key==pygame.K_g:
							 Time_Player_stats={'HP':70000000,'MP':500,'ATT':0,'SATT':0}
							 skill_supposed_delay['walk']=1
							 skill_supposed_delay['weak']=1
							 Time_Player_stats['INITHP']=Time_Player_stats['HP']
							 data['Time_Player']=Time_Player_stats
							 stats_update()
							 
						elif event.key==pygame.K_F1:
							 done=True

			
			
			background_blit()
			check_pos()
			
			mx=pygame.mouse.get_pos()[0]
			my=pygame.mouse.get_pos()[1]
			tx=mx/gw*gw-gw
			ty=my/gh*gh-gh
			
			global tempus
			tempus=z.tick()
			if abs(floatY) >= maxFloat:
				floatStep = - floatStep
				
			floatyFloatY += floatStep
			
			floatY = round(floatyFloatY)
			
			if turn=='Time_Player':
				camC=(time_player.x,time_player.y)
			else:
				for enemy in enemy_list:
					if enemy.surname == turn:
						camC=(enemy.x,enemy.y)
						break
			goalcamX,goalcamY=camC[0]-screen.get_width()/2,camC[1]-screen.get_height()/1.8
			tween()
			if not(switch):
				player_blits()
			else:
				Time_Player_blits()
			
			

			
			pygame.display.flip()
			
			# if syi<10 :
				# tki='00000'
			# elif syi<100:
				# tki='0000'
			# elif syi<1000:
				# tki='000'
			# elif syi<10000:
				# tki='00'
			# elif syi<100000:
				# tki='0'
			# elif syi<1000000:
				# tki=''
				
			# pygame.image.save(screen, 'stap/img'+tki+str(syi)+'.bmp')
			# syi += 1
			n=n+0.1
			if n>4:
				n=1
				
			
			definer_img=defines[math.trunc(n)-1]
			
			
			
			clock.tick(FPS)	 
			if not pygame.mixer.music.get_busy():
				pygame.mixer.music.load("light.mp3")
				pygame.mixer.music.set_volume(music)
			if not pygame.mixer.music.get_busy():
				try:
				   pygame.mixer.music.play()
				except:
				   pass
		

	pygame.quit()



	#Code 60x40.
	#flags= 1up,2down,3left,4right




























