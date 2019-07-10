#!/usr/bin/python3
# A simple python3 script to create a 2D reservoir geometry
# including a fault around the center
# switable to work with cfMesh's cartesian2D workflow

# Works but:
# Config files should allow for arbitrary number of patches

### Important imports
import numpy as np
import stl
import configparser
import json
import argparse

### The (cubic) bezier curve function
def bezier(p1, p2, p3, p4, t):
    # Use numpy arrays with this ...
    return p1*(1-t)**3 + 3*t*(1-t)**2 *p2 + 3*(1-t)*t**2 *p3 + p4*t**3

### A function to triangulate curve film
def sTri(ps, depth):
    # Takes in lower points and the depth of extrusion
    # Return triangles and their normals
    pZ = ps + np.array([0,0,depth])
    triangles = [[] for i in range(2*len(ps)-2)]
    for i in range(len(ps)-1):
        triangles[2*i] = [ps[i], pZ[i], pZ[i+1]]
        triangles[2*i+1] = [ps[i], pZ[i+1], ps[i+1]]
    
    normals = [np.cross(v[1]-v[0], v[2]-v[0]) for v in triangles]
    return [normals, triangles]

### Main program

### Parse Configuration file
config = configparser.ConfigParser()
cs = open("createFault.cfg", mode='r+')
print("Processing configuration file: ", cs.name, "...")
config.read_file(cs)
# Reservoir
filename = json.loads(config.get("Reservoir", "STL-file"))
minBox = json.loads(config.get("Reservoir", "min-Planes"))
maxBox = json.loads(config.get("Reservoir", "max-Planes"))
bBox = [minBox, maxBox]
depth = bBox[1][2] - bBox[0][2]
# Fault
Cres = json.loads(config.get("Fault", "resolution"))
p1 = np.array(json.loads(config.get("Fault","p1")))
p2 = np.array(json.loads(config.get("Fault","p2")))
p3 = np.array(json.loads(config.get("Fault","p3")))
p4 = np.array(json.loads(config.get("Fault","p4")))
p5 = np.array(json.loads(config.get("Fault","p5")))
p6 = np.array(json.loads(config.get("Fault","p6")))
# BoundaryPatch names
top = json.loads(config.get("PatchNames", "top"))   
right = json.loads(config.get("PatchNames", "right"))   
bottom = json.loads(config.get("PatchNames", "bottom"))   
left = json.loads(config.get("PatchNames", "left"))   
fault = json.loads(config.get("PatchNames", "fault"))   

### Parse Cmd arguments
parser = argparse.ArgumentParser(description="Generate STL geometry for 2D reservoir with\
        faults to use with cartisan2DMesh")
parser.add_argument("--p1",default=p1,type=float,nargs=3,help="First point in Fault curve")
parser.add_argument("--p2",default=p2,type=float,nargs=3,help="First control point in first Fault curve")
parser.add_argument("--p3",default=p3,type=float,nargs=3,help="Second control point in first Fault curve")
parser.add_argument("--p4",default=p4,type=float,nargs=3,help="End point in Fault curve")
parser.add_argument("--p5",default=p5,type=float,nargs=3,help="First control point in second Fault curve")
parser.add_argument("--p6",default=p6,type=float,nargs=3,help="First control point in second Fault curve")
parser.add_argument("--output","-o",default=filename,help="Output file name")
parser.add_argument("--curve-resolution","-r",default=Cres,type=int,help="Fault curve resolution")
args = parser.parse_args()

p1 = np.array(args.p1)
p2 = np.array(args.p2)
p3 = np.array(args.p3)
p4 = np.array(args.p4)
p5 = np.array(args.p5)
p6 = np.array(args.p6)
filename = args.output

### Fault Points as python lists
fstCurve = [bezier(p1,p2,p3,p4,t) for t in np.linspace(0,1-1/Cres,Cres)]
scdCurve = [bezier(p4,p5,p6,p1,t) for t in np.linspace(0,1,Cres)]

# Assemble fault points and extrude in Z-direction
points  = fstCurve + scdCurve
points.reverse()
[normals, triangles]  = sTri(points, depth)

## Create STL facets with normals inwarding
faces = [stl.Facet(normals[i], triangles[i]) for i in range(len(normals))]

## Create fault solid
fault = stl.Solid(fault, faces)
fs = open(filename, mode='w+')
fault.write_ascii(fs)

## Create Outer Boundary patches
# Top patch
tp = np.array([ [bBox[0][0], bBox[1][1], bBox[0][2]],\
     [bBox[1][0],bBox[1][1],bBox[0][2]] ])
[tn, tt] = sTri(tp, depth)
tf = [stl.Facet(tn[i], tt[i]) for i in range(len(tt))]
top = stl.Solid(top, tf)
top.write_ascii(fs)
# Right patch
tp = np.array([ [bBox[1][0], bBox[1][1], bBox[0][2]],\
     [bBox[1][0],bBox[0][1],bBox[0][2]] ])
[tn, tt] = sTri(tp, depth)
tf = [stl.Facet(tn[i], tt[i]) for i in range(len(tt))]
right = stl.Solid(right, tf)
right.write_ascii(fs)
# Bottom patch
tp = np.array([ [bBox[1][0], bBox[0][1], bBox[0][2]],\
     [bBox[0][0],bBox[0][1],bBox[0][2]] ])
[tn, tt] = sTri(tp, depth)
tf = [stl.Facet(tn[i], tt[i]) for i in range(len(tt))]
bottom = stl.Solid(bottom, tf)
bottom.write_ascii(fs)
# Left patch
tp = np.array([ [bBox[0][0], bBox[0][1], bBox[0][2]],\
     [bBox[0][0],bBox[1][1],bBox[0][2]] ])
[tn, tt] = sTri(tp, depth)
tf = [stl.Facet(tn[i], tt[i]) for i in range(len(tt))]
left = stl.Solid(left, tf)
left.write_ascii(fs)

## Debug
#print(points)
#plt.scatter([i[0] for i in points], [i[1] for i in points])
#plt.scatter([i[0] for i in scdCurve], [i[1] for i in scdCurve])
#plt.show()
print("Done writing surface to", fs.name)
