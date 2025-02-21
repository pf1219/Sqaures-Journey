# Stages
stage_cube=[]
stage_target=[]
stage_absent=[]
stage_special=[]

stage_cube.append([[0,2],[0,4]])
stage_target.append([[6,2],[6,4]])
stage_absent.append([[],[]])
stage_special.append([0,0])

stage_cube.append([[1,6],[4,2]])
stage_target.append([[3,0],[4,6]])
stage_absent.append([[],[]])
stage_special.append([0,0])

stage_cube.append([[0,3],[2,6]])
stage_target.append([[0,6],[5,6]])
stage_absent.append([[],[]])
stage_special.append([0,0])

stage_cube.append([[3,5],[6,1],[2,1]])
stage_target.append([[3,2],[5,6]])
stage_absent.append([[],[],[1,3]])
stage_special.append([0,0,1])

# Gameplay
for stage in range(start_stage,len(stage_cube)):
    cube_initial=[stage_cube[stage][i].copy() for i in range(len(stage_cube[stage]))]
    cube=[cube_initial[i].copy() for i in range(len(cube_initial))]
    target=stage_target[stage].copy()
    absent=[stage_absent[stage][i].copy() for i in range(len(stage_absent[stage]))]
    special=stage_special[stage].copy()

    exit_world=False
    exec(open(path('resource/stage.py')).read())
    
    if exit_world:
        break
