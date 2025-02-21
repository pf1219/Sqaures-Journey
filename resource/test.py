import random
direction=[[1,0],[0,-1],[-1,0],[0,1]]
symbol=['▶','▲','◀','▼']

while True:
    cube=[[random.randint(0,6),random.randint(0,6)] for i in range(4)]
    special=[int(random.random()<0.4) for i in range(4)]
    absent=[]
    for i in range(len(cube)):
        if special[i]==0:
            absent.append([i for i in range(4) if random.random()<0.3])
        else:
            absent.append([i for i in range(4) if random.random()<0.6])
    valid=True
    for i in range(len(cube)):
        if cube.count(cube[i])>1:
            valid=False
    if valid and special.count(1)>0 and special[0]==0:
        break

if 1==1:
    cube=[[0,3],[2,6]]
    absent=[[],[]]
    special=[0,0]
set_target=[[0,6],[5,6]]
ntarget=len(set_target)

tree=[[cube[i].copy() for i in range(len(cube))]]
moves=[0]
moves_list=[[]]
target=[[cube[i].copy() for i in range(ntarget)]]
target_moves=[0]
target_moves_list=[[]]

print(tree[0])
print(absent)
print(special)

while True:
    added=0
    tree2=[[tree[i][j].copy() for j in range(len(tree[i]))] for i in range(len(tree))]
    moves2=moves.copy()

    max_moves=max(moves)
    target_list=[i for i in range(len(tree)) if moves[i]==max_moves]
    for k in target_list:
        for i in range(len(cube)):
            for j in range(4):
                cube=[tree[k][k2].copy() for k2 in range(len(tree[k]))]
                while True:
                    if j not in absent[i] and cube[i][0]+direction[j][0] in range(7) and cube[i][1]+direction[j][1] in range(7) and [cube[i][0]+direction[j][0],cube[i][1]+direction[j][1]] not in cube:
                        cube[i][0]=cube[i][0]+direction[j][0]
                        cube[i][1]=cube[i][1]+direction[j][1]
                        if special[i]==1:
                            break
                    else:
                        break
                if cube not in tree2:
                    added=added+1
                    tree2.append([cube[i2].copy() for i2 in range(len(cube))])
                    moves2.append(moves[k]+1)
                    moves_list.append(moves_list[k]+[[i,j]])
                    if [cube[i].copy() for i in range(ntarget)] not in target:
                        target.append([cube[i].copy() for i in range(ntarget)])
                        target_moves.append(moves[k]+1)
                        target_moves_list.append(moves_list[-1])
                        
    tree=[[tree2[i][j].copy() for j in range(len(tree2[i]))] for i in range(len(tree2))]
    moves=moves2.copy()

    if added>0:
        print(moves[-1])
        print(len(moves))

    if added==0 or set_target in target or len(tree)>100000:
        break
print('')

print(tree[0])
print(absent)
print(special)
print('')
if set_target[0]==[-1,-1]:
    t=[]
    sampled=[]
    while True:
        i=random.sample(range(len(target)),k=1,counts=[2**target_moves[j] for j in range(len(target))])[0]
        sampled.append(i)
        
        valid=False
        if i not in t:
            valid=True
            k=[target_moves_list[i][j][0] for j in range(target_moves[i])]
            for j in range(len(cube)):
                if target_moves[i]<3 or (k.count(j)>2 and target_moves[i]-k.count(j)<2):
                    valid=False

        if valid:
            t.append(i)
            print(target[i])
            print(target_moves[i])
            k=[target_moves_list[i][j].copy() for j in range(target_moves[i])]
            for i in range(target_moves[i]):
                k[i][1]=symbol[k[i][1]]
            print(k)
            print('')

        if len(t)==10 or len(sampled)==len(target):
            break
else:
    i=target.index(set_target)
    print(target[i])
    print(target_moves[i])
    k=[target_moves_list[i][j].copy() for j in range(target_moves[i])]
    for i in range(target_moves[i]):
        k[i][1]=symbol[k[i][1]]
    print(k)
