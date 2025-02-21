# Stages
stage_cube=[]
stage_target=[]
stage_absent=[]
stage_special=[]

stage_cube.append([[0,3]])
stage_target.append([[6,3]])
stage_absent.append([[]])
stage_special.append([0])

stage_cube.append([[5,4],[1,4]])
stage_target.append([[2,6]])
stage_absent.append([[],[]])
stage_special.append([0,0])

stage_cube.append([[3,0],[3,3],[3,4]])
stage_target.append([[3,6]])
stage_absent.append([[],[1,3],[1,3]])
stage_special.append([0,0,0])

stage_cube.append([[0,6],[6,6],[3,3],[6,3]])
stage_target.append([[5,4]])
stage_absent.append([[],[0,2],[],[0,1,2,3]])
stage_special.append([0,0,0,0])

stage_cube.append([[6,5],[5,5],[1,6],[1,3]])
stage_target.append([[3,0]])
stage_absent.append([[],[],[0,1,2,3],[]])
stage_special.append([0,0,0,0])

stage_cube.append([[1,4],[5,3],[0,6]])
stage_target.append([[3,6]])
stage_absent.append([[],[],[]])
stage_special.append([0,0,0])

stage_cube.append([[1,6],[6,2],[0,6]])
stage_target.append([[4,6]])
stage_absent.append([[],[],[]])
stage_special.append([0,0,0])

stage_cube.append([[5,3],[6,2],[0,4],[1,4],[0,1]])
stage_target.append([[1,6]])
stage_absent.append([[],[0,3],[3],[1,3],[0,1,2,3]])
stage_special.append([0,0,0,0,0])

stage_cube.append([[6,0],[6,1]])
stage_target.append([[6,3]])
stage_absent.append([[],[]])
stage_special.append([0,0])

stage_cube.append([[3,4],[0,0],[0,6]])
stage_target.append([[5,5]])
stage_absent.append([[],[],[]])
stage_special.append([0,0,0])

stage_cube.append([[0,3],[3,3],[3,6],[6,3],[6,6]])
stage_target.append([[4,5]])
stage_absent.append([[],[0,1,3],[],[0,1,2,3],[]])
stage_special.append([0,0,0,0,0])

stage_cube.append([[4,3],[4,5],[0,4],[4,1]])
stage_target.append([[5,3]])
stage_absent.append([[],[3],[],[3]])
stage_special.append([0,0,0,0])

stage_cube.append([[4,2],[0,6]])
stage_target.append([[2,6]])
stage_absent.append([[1],[2]])
stage_special.append([0,0])

stage_cube.append([[5,3],[1,3],[4,3],[5,1]])
stage_target.append([[2,2]])
stage_absent.append([[],[1],[],[]])
stage_special.append([0,0,0,0])

stage_cube.append([[1,2], [6,4], [3,2]])
stage_target.append([[4,4]])
stage_absent.append([[], [], [0,1]])
stage_special.append([0,0,0])

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
