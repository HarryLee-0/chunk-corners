import math
xcoords=int(input("Input X:"))
zcoords=int(input("Input Z:"))


chunkidx=math.floor(xcoords/16)+1
chunkidz=math.floor(zcoords/16)+1

print("")

print("Chunk Corners:")
print((chunkidx*16-1,0,chunkidz*16-1))
print((chunkidx*16-1,0,chunkidz*16-16))
print((chunkidx*16-16,0,chunkidz*16-16))
print((chunkidx*16-16,0,chunkidz*16-1))
