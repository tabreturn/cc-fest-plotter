# SECTION 1: SETUP THE BLENDER FILE ===========================================

# 1. open blender and save the project as ~/<proj>/setup.blend
# 2. install freestyle (edit > preferences > add-ons > freestyle svg exporter)
# 3. properties panel > render properties > enable "freestyle svg export"
# 4. properties panel > render properties > enable "freestyle"
# 5. properties panel > output properties > output path of ~/<proj>/render.svg
# 6. test the render (render > render image)
# 7. delete the cube and save
# more freestyle options: properties panel > layer properties > freestyle ...)


# SECTION 2: A BLENDER SCRIPT =================================================

# you can use the internal blender code editor (scripting workspace) --
# but i'll go external, running blender 'headless' (using thonny and terminal)

# 1. in thonny, tools > manage packages > install "fake-bpy-module"

import bpy
from mathutils import Vector
import random
random.seed(123)

# 2. draw a cone (test automcomplete while writing this line)

bpy.ops.mesh.primitive_cone_add(location=(0, 0, 0))

# 3. render using the command line:
# /<blender_install>/blender -b setup.blend -P 03-blender_svg.py
# note that blender uses it's own python env (which does include pip)

bpy.context.scene.render.filepath = 'render'
bpy.ops.render.render()  # for a png, add arg write_still=True

# 4. add metaballs

metaball = bpy.data.metaballs.new('MetaBall')
obj = bpy.data.objects.new('MetaBallObject', metaball)
bpy.context.collection.objects.link(obj)
metaball.resolution = 0.1
metaball.render_resolution = 0.1
for i in range(30):
    location = Vector((0, 0, 0)) + Vector(
                                     random.uniform(-2, 2) for i in range(3))
    element = metaball.elements.new()
    element.co = location
    element.radius = 0.8

# 5. re-render (by moving the metaball code above the cone code)


# SECTION 3: CLEANING UP WITH VPYPE ===========================================

# from here, i might clean up the metaballs with vpype filter & linemerge
# e.g. vpype read render0001.svg filter -m 50 linemerge -t 50 write out.svg
# see reference at: https://vpype.readthedocs.io/en/stable/reference.html

