import mcschematic
d=open("F:/pythonProject/scim/out.py","r")
data=[]
a=d.read()
d.close()
d=open("out.py","w")
d.writelines(a)
c=['']
exec(a)
print(c)
schem = mcschematic.MCSchematic()
size=30
for x in range(size):
    for y in range(16):
        print(x,y)
        if x <len(c):
            print()
            if c[x][y]=="1":
                schem.setBlock(  (-3*x-1, y*2, 1), "minecraft:barrel{Items:[{Slot:0b, Count:1b, id:\"minecraft:redstone\"}]}"  )
            else:
                schem.setBlock((-3 * x - 1, y * 2, 1),
                            "minecraft:stone")
        else:
            schem.setBlock((-3 * x - 1, y * 2, 1),
                           "minecraft:stone")
schem.save( "schematics", "code1", mcschematic.Version.JE_1_18_2)