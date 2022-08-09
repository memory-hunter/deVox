import argparse as ap

parser = ap.ArgumentParser(description='Convert a voxel file to an obj file.')
parser.add_argument('input', help='Input voxel file.')
args = parser.parse_args()

voxelFile = args.input

print('Converting voxel file to obj file...')

with open(voxelFile, 'r') as f:
    lines = f.readlines()

    # Get the dimensions of the voxel file
    dims = lines[0].split()
    dims = [int(x) for x in dims]
    print("There are {} vertices and {} faces in the voxel file.".format(dims[0], dims[1]))

    # Get the voxel data
    voxelData = lines[1:]

# Parse the vertices and faces

i = 0
objLines = []

print('Parsing voxel data...')

while(i <= 2*dims[0]-1):
    line1 = voxelData[i].split()
    line2 = voxelData[i+1].split()

    #print("Vertex {}: ".format(line1[0]), end="")

    line1 = [float(x.strip()) for x in line1]
    line1 = [line1[1], line1[2]]
    line2 = [float(x.strip()) for x in line2]

    #print("x: {}, y: {}, z: {}".format(line1[0], line1[1], line2[0]))

    objLines.append("v {} {} {}\n".format(line1[0], line1[1], line2[0]))

    i += 2

voxelData = voxelData[2*dims[0]:]
i = 0

while(i <= 2*dims[1]-1):
    line1 = voxelData[i].split()
    line2 = voxelData[i+1].split()

    #print("Cube {}: ".format(line1[0]), end="")

    line1 = line1[3:]
    line1 = [int(x.strip()) for x in line1]
    line2 = [int(x.strip()) for x in line2]

    #print("{} {} {} {} {} {} {} {}".format(line1[0], line1[1], line1[2], line1[3], line2[0], line2[1], line2[2], line2[3]))

    objLines.append("f {} {} {} {}\n".format(line1[0], line2[0], line2[2], line1[2]))
    objLines.append("f {} {} {} {}\n".format(line1[3], line1[2], line2[2], line2[3]))
    objLines.append("f {} {} {} {}\n".format(line2[3], line2[2], line2[0], line2[1]))
    objLines.append("f {} {} {} {}\n".format(line2[1], line1[1], line1[3], line2[3]))
    objLines.append("f {} {} {} {}\n".format(line1[1], line1[0], line1[2], line1[3]))
    objLines.append("f {} {} {} {}\n".format(line2[1], line2[0], line1[0], line1[1]))

    i += 2
    pass

print("\nWriting obj file...")

with open('voxel.obj', 'w') as f:
    f.writelines(objLines)

print("Done!")