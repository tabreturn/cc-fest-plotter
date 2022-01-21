size(400, 400)


# SECTION 1: YOUR FIRST PY5/PROCESSING SVG ====================================

# note that you could also use size(400, 400, SVG, 'layer-1.svg')

begin_record(SVG, 'layer-1.svg')
background('#FFF')
no_fill()
rect(10, 10, 100, 100)
line(10, 360, 220, 360)
rect(80, 30, 100, 100)
end_record()


# SECTION 2: LAYERED SVGs =====================================================

# plotting with different pens means you'll need to seperate your shapes/lines

begin_record(SVG, 'layer-2.svg')
stroke('#F00')
stroke_weight(8)
line(80, 80, width-80, height-80)
end_record()

# 1. view the svg markup in a code editor (note the line and rect tags)
# 2. view file in inkscape and note that there are no layers
# 3. use inkscape to add layers; view new svg markup (<g inkscape:groupmode...)
# 4. create a function to merge your py5 svg files --

from xml.etree import ElementTree

def combine_svgs(layers, new_svg):
    begin_record(SVG, new_svg); end_record()
    ElementTree.register_namespace('', 'http://www.w3.org/2000/svg')
    tree = ElementTree.parse(new_svg)
    combined = tree.getroot()
    combined.set('xmlns:inkscape', 
                 'http://www.inkscape.org/namespaces/inkscape')

    for svg in layers:
        markup = ElementTree.parse(svg).getroot()
        group = ElementTree.SubElement(combined, 'g')
        group.set('id', svg)
        group.set('inkscape:groupmode', 'bar')
        group.set('inkscape:groupmode', 'layer')
        group.set('inkscape:label', svg)
        
        for child in list(markup):
            group.append(child)

    ElementTree.indent(tree, space="\t", level=0)
    tree.write(new_svg)

combine_svgs(['layer-1.svg', 'layer-2.svg'], 'combined.svg')
print(open('combined.svg').read())

# you could add this function to a 'utils' file to import into other sketches


# SECTION 3: HOT-RELOADING ====================================================

# sometimes it's convinient to just forgo py5's preview -- use exit_sketch() to 
# close the window immediately; just hot-reload the svg in your image viewer

exit_sketch()


# SECTION 4: VPYPE ============================================================

# vpype is a veritable swiss army knife for plotter-ready vector graphics
# https://vpype.readthedocs.io/en/stable/index.html

# 1. install "vpype" via the thonny package manager (tools > manage packages)
# 2. note how the layer-1 markeup draws in this (hardly efficient) order: 
#    rect -> line -> rect

print(open('layer-1.svg').read())

# 3. visualize the draw & pen-up routes with vpype --

import vpype_cli
vpype_cli.execute('read layer-1.svg write --pen-up vpyped.svg')

# note vpype strips the element styling (if you merge svg files using vpype)

# 4. now optimize the route (to minimize the pen-up travel distance)

vpype_cli.execute('read layer-1.svg linesort write --pen-up vpyped.svg')

# check out other vpype features, like: 
# linesimplify, linemerge (which include tolerance), and multipass (with count)


# SECTION 5: VPYPE OCCULT =====================================================

# occult is a vpype plug-in to remove lines occulted by polygons from svg files

# 1. downoad occult from:
#    https://github.com/LoicGoulefert/occult/archive/refs/heads/master.zip
# 2. install it using tools > manage packages > install from local file

import os
os.system('vpype read comnined.svg occult -i write vpyped.svg')

# also check out other vpype cool plug-ins, like: 
# vpype-pixelart, hatched (half-toning with hatches)

