message='STAGE '+str(stage+1)
message_color=[255,255,255]
message_time=60
moves=0

click=False
click_tick=False
click_box=-1
click_dir=-1
click_cord=[-1,-1]

press=False
press_tick=False
press_box=-1
press_dir=-1

tick=0

while True:
    message_time=message_time-1
    tick=tick+1
    
    RETURN=Rect(0,0,200,100)
    RETURN.center=(1615,440)
    RESET=Rect(0,0,200,100)
    RESET.center=(1615,640)

    cleared=True
    for i in range(len(target)):
        if cube[i]!=target[i]:
            cleared=False
    if cleared:
        message='CLEAR!'
        message_color=(0,255,0)
        message_time=1

        if save[current_world*15+stage]==0 or moves<save[current_world*15+stage]:
            save[current_world*15+stage]=moves
        
        draw(cube,target)
        if moves==perfect[current_world*15+stage]:
            write('PERFECT',50,(304,930),(0,0,255))
            save[current_world*15+stage]=moves
        py.display.update()
        time.sleep(1)
        py.event.get()
        break

    for event in py.event.get():
        if event.type==MOUSEBUTTONDOWN:
            click_tick=False
            if RETURN.collidepoint(event.pos):
                exit_world=True
            elif RESET.collidepoint(event.pos):
                cube=[cube_initial[i].copy() for i in range(len(cube_initial))]
                message='STAGE '+str(stage+1)
                message_color=[255,255,255]
                message_time=60
                moves=0
            for i in range(len(cube)):
                if BOX[i].collidepoint(event.pos):
                    click=True
                    click_box=i
                    click_cord=event.pos
                    click_tick=True
                    for j in range(4):
                        if CON[i][j].collidepoint(event.pos):
                            click_dir=j
        if event.type==KEYDOWN:
            press_tick=False
            for i in range(len(cube)):
                if BOX[i].collidepoint(py.mouse.get_pos()):
                    if event.key==K_DOWN or event.key==K_s:
                        press=True
                        press_tick=True
                        press_box=i
                        press_dir=3
                    if event.key==K_UP or event.key==K_w:
                        press=True
                        press_tick=True
                        press_box=i
                        press_dir=1
                    if event.key==K_RIGHT or event.key==K_d:
                        press=True
                        press_tick=True
                        press_box=i
                        press_dir=0
                    if event.key==K_LEFT or event.key==K_a:
                        press=True
                        press_tick=True
                        press_box=i
                        press_dir=2
        else:
            press_tick=False

        i=-1
        j=-1
        
        if click_tick==False:
            click=False
            click_box=-1
            click_cord=[-1,-1]
            click_dir=-1
        if press_tick==False:
            press=False
            press_box=-1
            press_dir=-1
        else:
            i=press_box
            j=press_dir
            
        if event.type==MOUSEBUTTONUP:
            if click:
                click_arrow=False
                if click_dir>-1:
                    if CON[click_box][click_dir].collidepoint(event.pos):
                        click_arrow=True
                        i=click_box
                        j=click_dir
                if click_arrow==False:
                    click_cord2=event.pos
                    dif_x=click_cord2[0]-click_cord[0]
                    dif_y=click_cord2[1]-click_cord[1]
                    i=click_box
                    j=-1
                    if dif_x>5 and math.fabs(dif_y)<math.fabs(dif_x):
                        j=0
                    if dif_x<-5 and math.fabs(dif_y)<math.fabs(dif_x):
                        j=2
                    if dif_y>5 and math.fabs(dif_x)<math.fabs(dif_y):
                        j=3
                    if dif_y<-5 and math.fabs(dif_x)<math.fabs(dif_y):
                        j=1
        if j>-1:
            if j not in absent[i]:
                moves=moves+1
                while True:
                    if j not in absent[i] and cube[i][0]+direction[j][0] in range(7) and cube[i][1]+direction[j][1] in range(7) and [cube[i][0]+direction[j][0],cube[i][1]+direction[j][1]] not in cube:
                        cube[i][0]=cube[i][0]+direction[j][0]
                        cube[i][1]=cube[i][1]+direction[j][1]
                        draw(cube,target)
                        time.sleep(0.02)
                        if special[i]==1:
                            break
                    else:
                        break

    draw(cube,target)
    py.display.update()
    FPS.tick(60)

    if exit_world:
        break
