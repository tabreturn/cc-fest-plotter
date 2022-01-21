# foo.py
import bpy
from mathutils import Vector
import random

bpy.ops.mesh.primitive_cone_add(location=(-3, 0, 0))
output = '/home/nuc/Desktop/render.png'

origin=(0, 0, 0)
n=30
r0=3
r1=1.25

metaball = bpy.data.metaballs.new('MetaBall')
obj = bpy.data.objects.new('MetaBallObject', metaball)
bpy.context.collection.objects.link(obj)
metaball.resolution = 0.1
metaball.render_resolution = 0.1
for i in range(n):
    location = Vector(origin) + Vector(random.uniform(-r0, r0) for i in range(3))
    element = metaball.elements.new()
    element.co = location
    element.radius = r1


bpy.context.scene.render.filepath = output
bpy.ops.render.render(write_still=True)





import os

def vpype_it():
    os.system('vpype read render.png0001.svg filter -m 50 write done.svg')

# Will be executed once when the whole rendering process is completed
bpy.app.handlers.render_post.append(vpype_it)

bpy.ops.render.render('INVOKE_DEFAULT', write_still = True) 




#from subprocess import call
#call(['blender','-b','untitled.blend','-P','bpy.py'])

#linemerge

# vpype read input.svg filter -m 50 write output.svg
# https://vpype.readthedocs.io/en/stable/reference.html#filter

#~/Apps/blender/blender -b untitled.blend -P bpy.py

#
