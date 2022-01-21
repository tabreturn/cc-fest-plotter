size(400, 400)

'''
01. quick intro to what a plotter is/does
02. discuss that i'm using axidraw (with inkscape, although there is a python api)
03. what is svg (https://blog.hubspot.com/website/what-is-an-svg-file)
04. svg markdown example
05. quick work on using js/dom for generative svg
06. move onto processing svg renderer
07. then onto python mode, onto py5
08. challenges of multiple colours in different layers ...
09. dom forum solution (i suggested a while back)
10. 
11. the do-it-all-at-once dilemma (cheating in inkscape?) 
12. check browser bookmarks (plotter > tools) vpype, uji, pgs, l-systems in inkscape ...
13. inspiration (#plottertwitter, inspirational artists ... check bookmarks)
'''



# YOUR FIRST SVG

# * note there are other ways, i.e. in size args

begin_record(SVG, 'layer-1.svg')
background('#FFF')
no_fill()
rect(10, 10, 100, 100)
line(10, 360, 220, 360)
rect(80, 30, 100, 100)
end_record()


# LAYERED SVGs

begin_record(SVG, 'layer-2.svg')
stroke('#F00')
stroke_weight(8)
line(80, 80, width-80, height-80)
end_record()

# 1. show svg markup (cut all superfluous code)
# 2. edit file in inkscape to show there are no layers
# 3. add inkscape layers and show code again

from xml.etree import ElementTree

def combine_svgs(layers, out):
    begin_record(SVG, out); end_record()
    ElementTree.register_namespace('', 'http://www.w3.org/2000/svg')
    tree = ElementTree.parse(out)
    combined = tree.getroot()
    combined.set('xmlns:inkscape', 'http://www.inkscape.org/namespaces/inkscape')

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
    tree.write(out)

combine_svgs(['layer-1.svg', 'layer-2.svg'], 'combined.svg')
print(open('combined.svg').read())

# * you can build up a utilities file to import into other sketches


# HOT-RELOADING

# * just use image viewer instead

exit_sketch()


# VPYPE

# 1. note the unoptimised pen route --

print(open('layer-1.svg').read())

# 2. install vpype via package manager
# 3. visualize pen route

import vpype_cli
vpype_cli.execute('read layer-1.svg write --pen-up vpyped.svg')

# optimize route

vpype_cli.execute('read layer-1.svg linesort write --pen-up vpyped.svg')
print(open('layer-1.svg').read())

# * also checkout: linesimplify & linemerge (which include tolerance), multipass (with count), pagesize

# 4. tools > manage packages (install from file downloaded from https://github.com/LoicGoulefert/occult)

import os
os.system('vpype read layer-1.svg occult -i write vpyped.svg')



# * also checkout: vpype-pixelart, hatched (half-toning with hatches)
