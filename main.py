# Import modules
import pygame as py
from pygame.locals import *
import sys, os, time, ctypes.wintypes, csv, math
def path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

# Initialize pygame
py.mixer.pre_init(44100,16,2,4096)
py.init()
py.mixer.init()
flags = py.SCALED | py.RESIZABLE | py.FULLSCREEN
win=py.display.set_mode((1920,1080),flags)
py.display.set_caption("Square's Journey")
icon = py.image.load(path('logo.png'))
py.display.set_icon(icon)
FPS=py.time.Clock()

# Load data
key1=list(csv.reader(open(path('resource/key1.csv'))))[0]
key1=[int(key1[i]) for i in range(10000)]
key2=list(csv.reader(open(path('resource/key2.csv'))))[0]
key2=[int(key2[i]) for i in range(10000)]
def encrypt(savefile):
    save2=[0 for i in range(10000)]
    for i in range(10000):
        save2[key2[i]]=savefile[i]+key1[i]
    return(save2)
def decrypt(savefile):
    save2=[0 for i in range(10000)]
    for i in range(10000):
        save2[key2.index(i)]=savefile[i]-key1[key2.index(i)]
    return(save2)
    
buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, buf)
savepath=buf.value
if 'H-Games' in os.listdir(savepath):
    if 'cube.csv' in os.listdir(savepath+'/H-Games'):
        save=list(csv.reader(open(savepath+'/H-Games/cube.csv')))[0]
        save=[int(save[i]) for i in range(10000)]
        save=decrypt(save)
    else:
        save=[0 for i in range(10000)]
else:
    os.mkdir(savepath+'/H-Games')
    save=[0 for i in range(10000)]
        
# Functions
def write(string,size,location,color):
    font=py.font.Font(path('resource/font.ttf'),size)
    text=font.render(string,False,color)
    text_rect=text.get_rect(center=location)
    win.blit(text,text_rect)
def draw(cube,target):
    win.fill((0,0,0))
    if message_time>0:
        write(message,100,(305,540),message_color)
    write('MOVES: '+str(moves),50,(304,810),(255,255,255))
    if save[current_world*15+stage]>0:
        write('BEST: '+str(save[current_world*15+stage]),50,(304,870),(255,255,255))
    if stage==0 and current_world==0:
        write('Click arrow button or swipe to move the box.',50,(960,95),(255,255,255))
    if message_time<0 or message!=('STAGE '+str(stage+1)):
        write('STAGE '+str(stage+1),50,(960,985),(255,255,255))
    
    # Grid
    global CON, BOX
    CON=[[] for i in range(len(cube))]
    BOX=[]
    for i in range(len(cube)):
        for j in range(4):
            R=Rect(0,0,shape[j][0],shape[j][1])
            R.center=(660+cor[j][0]+cube[i][0]*100,240+cor[j][1]+cube[i][1]*100)
            CON[i].append(R)
    for i in range(8):
        py.draw.line(win,(255,255,255),(610,190+100*i),(1310,190+100*i),2)
        py.draw.line(win,(255,255,255),(610+100*i,190),(610+100*i,890),2)

    if stage==0 and current_world==0:
        py.draw.line(win,(255,255,0),(660+1*100,240+3*100),(660+(1+4*(tick%120)/120)*100,240+3*100),5)
        k=660+(1+4*(tick%120)/120)*100
        py.draw.polygon(win,(255,255,0),((k+25,540),(k-12.5,540+21.7),(k-12.5,540-21.7)))

    for i in range(len(cube)):
        R=Rect(0,0,80,80)
        R.center=(660+cube[i][0]*100,240+cube[i][1]*100)
        BOX.append(R)
        if i<len(target):
            py.draw.rect(win,target_color[i],R)
        else:
            py.draw.rect(win,(255,255,255),R)
        for j in range(4):
            if j not in absent[i]:
                if special[i]==0:
                    py.draw.rect(win,(0,0,220),CON[i][j])
                elif special[i]==1:
                    py.draw.rect(win,(0,220,0),CON[i][j])
                write(symbol[j],20,CON[i][j].center,(0,170,170))
    for i in range(len(target)):
        py.draw.circle(win,target_color[i],(660+target[i][0]*100,240+target[i][1]*100),20)

    # Button
    py.draw.rect(win,(255,0,0),RETURN)
    write('RETURN',50,RETURN.center,(255,255,255))
    py.draw.rect(win,(0,255,0),RESET)
    write('RESET',50,RESET.center,(255,255,255))

    # Draw
    py.display.update()
    
# Constants
target_color=[[255,255,0],[0,255,255],[255,0,255],[255,0,0],[0,255,0],[0,0,255]]
cor=[[30,0],[0,-30],[-30,0],[0,30]]
shape=[[20,35],[35,20],[20,35],[35,20]]
direction=[[1,0],[0,-1],[-1,0],[0,1]]
symbol=['▶','▲','◀','▼']
nworld=1

world_name=['Inception','Exploration']
perfect=[1,2,3,3,4,4,5,5,10,5,7,6,6,7,16]
perfect=perfect+[3,3,5,6,7,7,9,9,12,8,10,10,11,11,14]
perfect=perfect+[2,3,6,5,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
world_color=[[255,255,0],[100,255,100],[100,100,255]]
world_BGM=['Eurorave Delirium by OcularNebula','Colors by Tobu']

# Sandbox

# Resource

# Mainscreen
current_world=0
start_stage=0
exit_menu=0
change_world=False
BGM=py.mixer.Sound(path('resource/'+str(current_world+1)+'.mp3'))
BGM.play(-1)
        
while True:
    win.fill((0,0,0))

    if change_world:
        BGM.stop()
        prev_volume=BGM.get_volume()
        BGM=py.mixer.Sound(path('resource/'+str(current_world+1)+'.mp3'))
        BGM.set_volume(prev_volume)
        BGM.play(-1)
        change_world=False

    write("SQUARE'S JOURNEY",100,(960,75),(255,255,255))

    QUIT=Rect(0,0,200,100)
    QUIT.center=(960,1020)
    py.draw.rect(win,(255,127,127),QUIT)
    write('QUIT',50,QUIT.center,(0,0,0))

    write('VERSION 1.1',30,(1440,1020),(255,255,255))
    write('BGM: '+world_BGM[current_world],30,(480,1020),(255,255,255))

    BG=Rect(0,0,1500,800)
    BG.center=(960,540)
    py.draw.rect(win,[int(world_color[current_world][i]*0.4) for i in range(3)],BG)

    RT=Rect(0,0,60,400)
    RT.center=(1780,540)
    if current_world<(len(world_name)-1):
        py.draw.rect(win,world_color[current_world],RT)
    else:
        py.draw.rect(win,(127,127,127),RT)
    write('>',125,RT.center,(0,0,0))
    
    LT=Rect(0,0,60,400)
    LT.center=(140,540)
    if current_world>0:
        py.draw.rect(win,world_color[current_world],LT)
    else:
        py.draw.rect(win,(127,127,127),LT)
    write('<',125,LT.center,(0,0,0))

    VOL=Rect(0,0,200,50)
    VOL.center=(1600,75)
    if BGM.get_volume()==1:
        py.draw.rect(win,(255,255,0),VOL)
        write('BGM: ON',40,VOL.center,(0,0,0))
    else:
        py.draw.rect(win,(127,127,127),VOL)
        write('BGM: OFF',40,VOL.center,(0,0,0))
    
    write('WORLD '+str(current_world+1)+': '+world_name[current_world],50,(940,190),(0,0,0))

    ST=[]
    count=[0,0,0]
    for i in range(15):
        x=i%5
        y=i//5
        R=Rect(0,0,150,150)
        R.center=(460+250*x,325+215*y)
        ST.append(R)
        if save[current_world*15+i]==perfect[current_world*15+i]:
            py.draw.rect(win,[int(world_color[current_world][i]) for i in range(3)],R)
            count[0]=count[0]+1
        elif save[current_world*15+i]>0:
            py.draw.rect(win,[int(world_color[current_world][i]*0.3+127*0.7) for i in range(3)],R)
            count[1]=count[1]+1
        else:
            py.draw.rect(win,(127,127,127),R)
            count[2]=count[2]+1
        write(str(i+1),100,R.center,(0,0,0))

    write('PERFECT: '+str(count[0]),40,(710,885),[int(world_color[current_world][i]) for i in range(3)])
    write('CLEARED: '+str(count[0]+count[1]),40,(1210,885),[int(world_color[current_world][i]*0.3+127*0.7) for i in range(3)])

    for event in py.event.get():
        if event.type==MOUSEBUTTONDOWN:
            if QUIT.collidepoint(event.pos):
                f=open(savepath+'/H-Games/cube.csv','w',newline='')
                wr=csv.writer(f)
                wr.writerow(encrypt(save))
                f.close()
                py.quit()
                sys.exit()
            if LT.collidepoint(event.pos) and current_world>0:
                current_world=current_world-1
                change_world=True
            if RT.collidepoint(event.pos) and current_world<(len(world_name)-1):
                current_world=current_world+1
                change_world=True
            if VOL.collidepoint(event.pos):
                BGM.set_volume(1-BGM.get_volume())
            for i in range(15):
                if ST[i].collidepoint(event.pos):
                    start_stage=i
                    exec(open(path('resource/'+str(current_world+1)+'.py')).read())
                    break

    py.display.update()
    FPS.tick(60)
