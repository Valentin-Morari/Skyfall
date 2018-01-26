 
import pygame
import random


black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 128, 255, 0)
red = ( 255, 0, 0)                                     #  rosu,oranj,galben,verde,albastru,violet.
blue= ( 0 , 0 , 255)
colour=(255,128,0) #orange
coloUr=(255,255,0) #yello
color=(127,0,255) #violent

pygame.init()
# Set the width and height of the screen [width,height]
size=[700,500]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Kuubicks")
#Loop until the user clicks the close button.
done=False
# Used to manage how fast the screen updates

first=0
last=0
second=0
third=0
fourth=0
fifth=0
#Loading images below. The points.
turnx=0 
turny=0
hngh=0 #button press. 1 up, 2 down, 3 left, 4 right, 5 UP, 6 DOWN, 7 LEFT, 8 RIGHT. 9 RUP, 10 ROWN, 11 REFT, 12 ROITE.
lathua=70

sx=size[0]/2
sy=size[1]/2

hsize=[sx,sy]

vallist={'FRONT':2,'UP':0,'DOWN':0,'LEFT':0,'RIGHT':0,'BACK':0}                        #FRONT,UP,DOWN,LEFT,RIGHT,BACK.

xlist=[2,0,0,0]
ylist=[2,0,0,0]

fixed=0
ftime=0


ex=0
ey=0

p1 = hsize
p2 = [hsize[0]+lathua,hsize[1]]
p3= [hsize[0]+lathua,hsize[1]+lathua]
p4=[hsize[0],hsize[1]+lathua]
p5=[hsize[0]+turnx, hsize[1] + turny]
p6=[hsize[0]+lathua+turnx,hsize[1]+turny]
p7=[hsize[0]+lathua+turnx,hsize[1]+lathua+turny]
p8=[hsize[0]+turnx,hsize[1]+turny+lathua]
# -------- Main Program Loop -----------
while done==False:

     for event in pygame.event.get(): # User did something
         if event.type == pygame.QUIT: 
             done=True
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_DOWN:
                  hngh = 2
             if event.key == pygame.K_UP:
                  
                  hngh = 1
             if event.key == pygame.K_LEFT:
                  hngh = 3
             if event.key == pygame.K_RIGHT:
                  hngh = 4
#NEIGH
             if event.key == pygame.K_KP8:
                  hngh = 5
             if event.key == pygame.K_KP2:
                  hngh = 6
             if event.key == pygame.K_KP4:
                  hngh = 7
             if event.key == pygame.K_KP6:
                  hngh = 8
             if event.key == pygame.K_KP5:
                  hngh= -1
                  

#MJAO     
             if event.key == pygame.K_w:
                  hngh = 9
             if event.key == pygame.K_s:
                  hngh = 10
             if event.key == pygame.K_a:
                  hngh = 11
             if event.key == pygame.K_d:
                  hngh = 12

                  
          
#      L 0 G I C       #
     ''' just spin.'''
     if hngh == -1:
          turnx,turny=[0,0]
          p1 = hsize
          p2 = [hsize[0]+lathua,hsize[1]]
          p3= [hsize[0]+lathua,hsize[1]+lathua]
          p4=[hsize[0],hsize[1]+lathua]

          p5=[hsize[0]+turnx, hsize[1] + turny]
          p6=[hsize[0]+lathua+turnx,hsize[1]+turny]
          p7=[hsize[0]+lathua+turnx,hsize[1]+lathua+turny]
          p8=[hsize[0]+turnx,hsize[1]+turny+lathua]

          fixed = 0

          vallist['UP']=1
          vallist['RIGHT']=1
          
     if hngh <> 0 and event.type <> pygame.KEYDOWN:
          hngh=0
          
     if hngh==1 and -turny <=lathua/4 and fixed == 0:                                #     vallist=[2,1,0,0,1,0]                             #FRONT,UP,DOWN,LEFT,RIGHT,BACK.

          
          turny-=1
          p5=[hsize[0]+turnx, hsize[1] + turny]
          p6=[hsize[0]+lathua+turnx,hsize[1]+turny]
          p7=[hsize[0]+lathua+turnx,hsize[1]+lathua+turny]
          p8=[hsize[0]+turnx,hsize[1]+turny+lathua]

          #key so, get the current front's points, verify if it's above or under it and.. yeah. what.
          if p1[1] > p5[1] and p2[1] > p6[1]:
              vallist['UP']=1
              vallist['DOWN']=0
               
          
                
          

     elif hngh==2 and turny<=lathua/4 and fixed == 0:
          turny+=1

          p5=[hsize[0]+turnx, hsize[1] + turny]
          p6=[hsize[0]+lathua+turnx,hsize[1]+turny]
          p7=[hsize[0]+lathua+turnx,hsize[1]+lathua+turny]
          p8=[hsize[0]+turnx,hsize[1]+turny+lathua]
          

          if p4[1] < p8[1] and p3[1] < p7[1]:
              vallist['UP']=0 
              vallist['DOWN']=1
              
     elif hngh==3 and -turnx <= lathua/4 and fixed == 0:
          turnx-=1
          p5=[hsize[0]+turnx, hsize[1] + turny]
          p6=[hsize[0]+lathua+turnx,hsize[1]+turny]
          p7=[hsize[0]+lathua+turnx,hsize[1]+lathua+turny]
          p8=[hsize[0]+turnx,hsize[1]+turny+lathua]

          if p5[0]<p1[0] and p8[0]<p4[0]:
              vallist['LEFT']=1
              vallist['RIGHT']=0

          
               
     elif hngh==4 and turnx <= lathua/4 and fixed == 0:
          
          turnx+=1          
          p5=[p1[0]+turnx,p1[1]+turny]
          p6=[p1[0]+lathua+turnx,p1[1]+turny]
          p7=[p1[0]+lathua+turnx,p1[1]+lathua+turny]
          p8=[p1[0]+turnx,p1[1]+turny+lathua]

          if p6[0] > p2[0] and p7[0] > p3[0]:
              vallist['LEFT']=0
              vallist['RIGHT']=1


          


#MOVE THE CUUB.
     elif hngh == 5:
          p1[1]-=4
          p2[1]-=4
          p3[1]-=4
          p4[1]-=4
          p5[1]-=4
          p6[1]-=4
          p7[1]-=4
          p8[1]-=4
     elif hngh == 6:
          p1[1]+=4
          p2[1]+=4
          p3[1]+=4
          p4[1]+=4
          p5[1]+=4
          p6[1]+=4
          p7[1]+=4
          p8[1]+=4
     elif hngh == 7:
          p1[0]-=4
          p2[0]-=4
          p3[0]-=4
          p4[0]-=4
          p5[0]-=4
          p6[0]-=4
          p7[0]-=4
          p8[0]-=4
     elif hngh == 8:
          p1[0]+=4
          p2[0]+=4
          p3[0]+=4
          p4[0]+=4
          p5[0]+=4
          p6[0]+=4
          p7[0]+=4
          p8[0]+=4


# OKAY R00T4T3:                    #     vallist=[2,1,0,0,1,0]                             #FRONT,UP,DOWN,LEFT,RIGHT,BACK.

     elif hngh == 11 and ftime==0:
            p1 = hsize
            p2 = [hsize[0]+lathua,hsize[1]]
            p3= [hsize[0]+lathua,hsize[1]+lathua]
            p4=[hsize[0],hsize[1]+lathua]
            p5=[hsize[0]+turnx, hsize[1] + turny]
            p6=[hsize[0]+lathua+turnx,hsize[1]+turny]
            p7=[hsize[0]+lathua+turnx,hsize[1]+lathua+turny]
            p8=[hsize[0]+turnx,hsize[1]+turny+lathua]

            oldp1=p1
            oldp4=p4
            
            p1=p5
            p4=p8
            p5=p6
            p8=p7
            p6=p2
            p7=p3
            p2=oldp1                                                                   #LEFT.
            p3=oldp4
            
            olleft=vallist['LEFT']
            olright=vallist['RIGHT']
            olfront=vallist['FRONT']
            olback=vallist['BACK']
            
            
            
            vallist['LEFT']=olback
            vallist['BACK']=olright
            vallist['RIGHT']=olfront
            vallist['FRONT']=olleft
            
            ''' but!  but in the put, goota do the x ex yo 2 is zero wtf '''

      #      for i in range(len(xlist)):
      #              if xlist[i]==2:
        #                    xlist[i]=0

        #                    nextup=[]
          #                  if i+1 == 6:
          #                      i=0
          #                  nextup.append(i+1)
                            
                   
               
            fixed = 1
            ftime=1   
            hngh=0
                
   #         for i in range(len(vallist)):
      #            vallist[nextup[0]]=2 

     elif hngh == 11 and ftime==1:

            oldp1=p1
            oldp4=p4

            p1=p5
            p4=p8
            p5=p6
            p8=p7
            p6=p2
            p7=p3
            p2=oldp1
            p3=oldp4

            fixed = 1
             
            hngh=0
     
     elif hngh ==9 and ftime == 0:
            p1 = hsize
            p2 = [hsize[0]+lathua,hsize[1]]
            p3= [hsize[0]+lathua,hsize[1]+lathua]
            p4=[hsize[0],hsize[1]+lathua]
            p5=[hsize[0]+turnx, hsize[1] + turny]
            p6=[hsize[0]+lathua+turnx,hsize[1]+turny]
            p7=[hsize[0]+lathua+turnx,hsize[1]+lathua+turny]
            p8=[hsize[0]+turnx,hsize[1]+turny+lathua]

            oldp1=p1
            oldp2=p2

            p1=p5
            p2=p6
            p5=p8
            p6=p7
            p8=p4
            p7=p3
            p4=oldp1
            p3=oldp2

            fixed = 1
            ftime = 1
            hngh = 0
     elif hngh ==9 and ftime == 1:                                         #UP.

           oldp1=p1
           oldp2=p2

           p1=p5
           p2=p6
           p5=p8
           p6=p7
           p8=p4
           p7=p3
           p4=oldp1
           p3=oldp2

           fixed = 1

           hngh = 0


     elif hngh == 10 and ftime == 0:                            # DOWN
          p1 = hsize
          p2 = [hsize[0]+lathua,hsize[1]]
          p3= [hsize[0]+lathua,hsize[1]+lathua]
          p4=[hsize[0],hsize[1]+lathua]
          p5=[hsize[0]+turnx, hsize[1] + turny]
          p6=[hsize[0]+lathua+turnx,hsize[1]+turny]
          p7=[hsize[0]+lathua+turnx,hsize[1]+lathua+turny]
          p8=[hsize[0]+turnx,hsize[1]+turny+lathua]

          oldp1=p1
          oldp2=p2

          p1=p4
          p2=p3
          p4=p8
          p3=p7
          p8=p5
          p7=p6
          p5=oldp1
          p6=oldp2

          fixed = 1
          ftime = 1
          hngh = 0
     elif hngh == 10 and ftime == 1:
          oldp1=p1
          oldp2=p2

          p1=p4
          p2=p3
          p4=p8
          p3=p7
          p8=p5
          p7=p6
          p5=oldp1
          p6=oldp2

          fixed = 1

          hngh = 0          
            
     elif hngh == 12 and ftime==0:
            p1 = hsize
            p2 = [hsize[0]+lathua,hsize[1]]
            p3= [hsize[0]+lathua,hsize[1]+lathua]
            p4=[hsize[0],hsize[1]+lathua]
            p5=[hsize[0]+turnx, hsize[1] + turny]
            p6=[hsize[0]+lathua+turnx,hsize[1]+turny]
            p7=[hsize[0]+lathua+turnx,hsize[1]+lathua+turny]
            p8=[hsize[0]+turnx,hsize[1]+turny+lathua]



            oldp1=p1
            oldp4=p4
            p1=p2
            p4=p3
            p2=p6
            p3=p7
            p6=p5
            p7=p8
            p5=oldp1
            p8=oldp4

            fixed = 1
            ftime=1   
            hngh=0

     elif hngh == 12 and ftime==1:                #RIGHT.


            
            oldp1=p1
            oldp4=p4
            p1=p2
            p4=p3
            p2=p6
            p3=p7
            p6=p5
            p7=p8
            p5=oldp1
            p8=oldp4

            fixed = 1
             
            hngh=0            

               
          
          
          
          
          

     
     ''' / spin '''

     """ just code """

     
     

     
     


     
     pointlist = [p1,p2,p3,p4]#FRONT   #KAW KAW -WISE.

     pointlist1 = [ p5,p6,p2,p1] #UP UP
     
     pointlist2= [ p5,p6,p7,p8]  #BACK

     pointlist3= [p8,p7,p3,p4]   #DOWN

     pointlist4 = [p1,p5,p8,p4  ]    #LEFT

     pointlist5 = [p2,p6,p7,p3 ]   #RIGHT
     
     # above this, or they will be erased with this command.
     screen.fill(black)

     

    # xlist, 0= front, 1 = right, 2 = back, 3 = left
#     vallist[0]=xlist[0]
  #   vallist[3]=xlist[3]
  #   vallist[4]=xlist[1]
  #   vallist[5]=xlist[2]
     vally=[vallist['FRONT'],vallist['UP'],vallist['DOWN'],vallist['LEFT'],vallist['RIGHT'],vallist['BACK']]
     for i in range(len(vally)):

                    
                    if vally[i]==0:
                         
                         if i == 0:
                             pygame.draw.polygon(screen, blue, pointlist, 0)   #Draw where, color, closed?, list of points, width of line. #FRONT
                         if i == 1:
                             pygame.draw.polygon(screen, green,pointlist1, 0) #UP PUP
                         if i == 2:
                             pygame.draw.polygon(screen,colour,pointlist3,0)  # DOWN.
                         if i == 3:
                             pygame.draw.polygon(screen, coloUr,  pointlist4,0) #LEFT
                         if i == 4:
                             pygame.draw.polygon(screen, color, pointlist5, 0) #RIGHT
                         if i == 5:
                             pygame.draw.polygon(screen,red,pointlist2,0) #BACK
                             
     for i in range(len(vally)):           
                    if vally[i]==1:
                         
                         if i == 0:
                             pygame.draw.polygon(screen, blue, pointlist, 0)   #Draw where, color, closed?, list of points, width of line. #FRONT
                         if i == 1:
                             pygame.draw.polygon(screen, green,pointlist1, 0) #UP PUP
                         if i == 2:
                             pygame.draw.polygon(screen,colour,pointlist3,0)  # DOWN.
                         if i == 3:
                             pygame.draw.polygon(screen, coloUr,  pointlist4,0) #LEFT
                         if i == 4:
                             pygame.draw.polygon(screen, color, pointlist5, 0) #RIGHT
                         if i == 5:
                             pygame.draw.polygon(screen,red,pointlist2,0) #BACK
     for i in range(len(vally)):

                    if vally[i]==2:
                         
                         if i == 0:
                             pygame.draw.polygon(screen, blue, pointlist, 0)   #Draw where, color, closed?, list of points, width of line. #FRONT
                         if i == 1:
                             pygame.draw.polygon(screen, green,pointlist1, 0) #UP PUP
                         if i == 2:
                             pygame.draw.polygon(screen,colour,pointlist3,0)  # DOWN.
                         if i == 3:
                             pygame.draw.polygon(screen, coloUr,  pointlist4,0) #LEFT
                         if i == 4:
                             pygame.draw.polygon(screen, color, pointlist5, 0) #RIGHT
                         if i == 5:
                             pygame.draw.polygon(screen,red,pointlist2,0) #BACK
                             
                         


     #     vallist=[2,1,0,0,1,0]                             #FRONT,UP,DOWN,LEFT,RIGHT,BACK.

     ''' pygame.draw.polygon(screen,red,pointlist2,0) #BACK



     pygame.draw.polygon(screen  , coloUr,  pointlist4,0) #LEFT


     pygame.draw.polygon(screen,colour,pointlist3,0)  # DOWN.

     pygame.draw.polygon(screen, color, pointlist5, 0) #RIGHT
     pygame.draw.polygon(screen, green,pointlist1, 0) #UP PUP
     
     pygame.draw.polygon(screen, blue, pointlist, 0)   #Draw where, color, closed?, list of points, width of line. #FRONT

     '''


     
     


     
     
     
     print vallist
     pygame.display.flip()
     
     

pygame.quit ()


''' Coolshit:

     pygame.draw.lines(screen,red,True,pointlist2,1) #BACK



     pygame.draw.lines(screen, coloUr, True, pointlist4,1) #LEFT
     pygame.draw.lines(screen, color, True, pointlist5, 1) #RIGHT

     pygame.draw.lines(screen,colour,True,pointlist3,1)  # DOWN.
     pygame.draw.lines(screen, green,True, pointlist1, 1) #UP PUP
     
     pygame.draw.lines(screen, blue,True, pointlist, 1)   #Draw where, color, closed?, list of points, width of line. #FRONT

--wub wub --

                         if i == 0:
                              pygame.draw.lines(screen, blue,True, pointlist, 1)   #Draw where, color, closed?, list of points, width of line. #FRONT
                         if i == 1:
                              pygame.draw.lines(screen, green,True, pointlist1, 1) #UP PUP
                         if i == 2:
                              pygame.draw.lines(screen,colour,True,pointlist3,1)  # DOWN.
                         if i == 3:
                              pygame.draw.polygon(screen, coloUr,  pointlist4,1) #LEFT
                         if i == 4:
                              pygame.draw.lines(screen, color, True, pointlist5, 1) #RIGHT
                         if i == 5:
                              pygame.draw.lines(screen,red,True,pointlist2,1) #BACK   

and maybe!:

     if i == 0:
          pygame.draw.polygon(screen, blue, pointlist, 0)   #Draw where, color, closed?, list of points, width of line. #FRONT
     if i == 1:
          pygame.draw.polygon(screen, green,pointlist1, 0) #UP PUP
     if i == 2:
          pygame.draw.polygon(screen,colour,pointlist3,0)  # DOWN.
     if i == 3:
          pygame.draw.polygon(screen, coloUr,  pointlist4,0) #LEFT
     if i == 4:
          pygame.draw.polygon(screen, color, pointlist5, 0) #RIGHT
     if i == 5:
          pygame.draw.polygon(screen,red,pointlist2,0) #BACK

'''
