# -*- coding: utf-8 -*-
from mecode import G

#endmill_size_6000 = 6.0
#feedrate_6mm = 1000
#endmill_size_3000 = 3.0
#feedrate_3mm = 750
#endmill_size_1000 = 1.0
#feedrate_1mm = 500
#endmill_size_500 = 0.5
#feedrate_500um = 250
#endmill_size_250 = 0.25
#feedrate_250um = 150
#endmill_size_200 = 0.20
#feedrate_200um = 100

#zero at center of block

facemill = True
#w/ 3mm endmill
facemill_depth = 0.3 #in mm
facemill_length = 50.0 #in mm
facemill_width = 25.0 #in mm

#Global variables 
channel_size = 0.25
channel_length = 25.0
thickness = 9.0
bolt_hole_size = 3.0
max_mill_depth_ratio = 0.1
clearance = 10.0
boss_length = channel_length + clearance/2
boss_width = clearance/2
part_length = boss_length + clearance
part_width = boss_width + clearance
gasket_thickness = 1.55
gasket_cut_depth = 3.0
gasket_clearance = 2

#inlet need 13/64 bench press.

holes = True
drill_peck_step = 0.5
drill_peck_retract = 1.0
drill_peck_rest = 3.0

cutout = True

def mill_face (facemill_depth,facemill_width,facemill_length):
#3mm endmill
    g.feed(100)
    g.abs_move(Z=1)
    g.abs_move(x=-(facemill_length)/2,y=-(facemill_width)/2)
    g.abs_move(Z=-facemill_depth)
    g.move(y=facemill_width)
    g.move(x=facemill_length)
    g.move(y=-(facemill_width))
    g.move(x=-(facemill_length))
    for i in range(int(facemill_width/4)):
        g.move(x=facemill_length)
        g.move(y=2.0)
        g.move(x=-(facemill_length))
        g.move(y=2.0)
    g.abs_move(Z=1.0)
    
def drill_peck (x_position,y_position,z_depth,z_step,z_retract,z_rest,hole_endmill_size,feedrate):
    g.feed(feedrate)
    g.abs_move(Z=1.0)
    g.abs_move(x=x_position,y=y_position)
    g.abs_move(Z=0)
    for i in range (int(z_depth/z_step)):
        g.move(Z=-z_step*(i+1))
        g.abs_move(Z=z_retract)
        g.abs_move(Z=0)
    g.abs_move(Z=z_rest)

def mill_hole (x_position,y_position,z_depth,z_step,endmill_size,hole_size,feedrate):
    g.feed(feedrate)
    g.abs_move(Z=1.0)
    g.abs_move(x=x_position,y=y_position)
    g.move(x=-(hole_size-endmill_size)/2)
    g.abs_move(Z=0)
    for i in range (int(z_depth/z_step)):
        g.move(Z=-z_step)
        #g.arc(x=0,y=0,radius=-(hole_size-endmill_size)/2)
        line = 'G2 X0 Y0 I{} J0 F{}'.format((hole_size-endmill_size)/2, feedrate)
        g.write(line)
    g.abs_move(Z=1)
    
    
#3mm endmill to facemill
if facemill == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/flowcell/flowcell-facemill(3mm).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    
    #starts bottom left
    mill_face (facemill_depth,facemill_width,facemill_length)    
    
    
#3mm endmill for gasket space
if facemill == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/flowcell/flowcell-gasket-space(3mm).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    
    #starts bottom left
    g.feed(300)
    g.abs_move(Z=1.0)
    
    for i in range(4):
        g.abs_move(x=-(part_length+3.0)/2,y=-(part_width+3.0)/2)
        g.feed(100)
        g.abs_move(Z=-gasket_thickness*(i+1)/4)
        for i in range(int(clearance/2)):
            g.move(y=1.0)
            g.move(x=part_length+3.0)
            g.move(x=-(part_length+3.0))
    g.abs_move(Z=1.0)        
    
    for i in range(4):
        g.abs_move(x=-(part_length+3.0)/2,y=(part_width+3.0)/2)
        g.feed(100)
        g.abs_move(Z=-gasket_thickness*(i+1)/4)
        for i in range(int(clearance/2)):
            g.move(y=-1.0)
            g.move(x=part_length+3.0)
            g.move(x=-(part_length+3.0))
    g.abs_move(Z=1.0)       
    
    for i in range(4):
        g.abs_move(x=-(part_length+3.0)/2,y=(clearance/2+3.0)/2)
        g.feed(100)
        g.abs_move(Z=-gasket_thickness*(i+1)/4)
        for i in range(int(clearance/2)):
            g.move(x=1.0)
            g.move(y=-(clearance/2+3.0))
            g.move(y=(clearance/2+3.0))
    g.abs_move(Z=1.0)     
        
    for i in range(4):
        g.abs_move(x=(part_length+3.0)/2,y=(clearance/2+3.0)/2)
        g.feed(100)
        g.abs_move(Z=-gasket_thickness*(i+1)/4)
        for i in range(int(clearance/2)):
            g.move(x=-1)
            g.move(y=-(clearance/2+3.0))
            g.move(y=(clearance/2+3.0))
    g.abs_move(Z=1)     
    
        
#250mm endmill for channel
if facemill == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/flowcell/flowcell-channel(250um).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )

    #outlet
    g.feed(300)
    g.abs_move(Z=1.0)
    g.abs_move(x=-(channel_length-channel_size)/2,y=0)
    g.abs_move(Z=0)
    
    for i in range(int(1/max_mill_depth_ratio)):
        g.feed(50)
        g.move(Z=-channel_size*max_mill_depth_ratio)
        g.move(x=channel_length-channel_size)
        g.move(x=-(channel_length-channel_size))
    g.abs_move(Z=3.0)        
    
#500mm endmill for channel
if facemill == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/flowcell/flowcell-channel(500um).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )

    #outlet
    g.feed(300)
    g.abs_move(Z=1.0)
    g.abs_move(x=-(channel_length-channel_size)/2,y=0)
    g.abs_move(Z=0)
    
    for i in range(int(1/max_mill_depth_ratio)):
        g.feed(50)
        g.move(Z=-0.5*max_mill_depth_ratio)
        g.move(x=channel_length-0.5)
        g.move(x=-(channel_length-0.5))
    g.abs_move(Z=3.0)       

#3mm endmill for inlets-back
if facemill == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/flowcell/flowcell-inlets-back(3mm).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )

    mill_hole (0,0,5,drill_peck_step,3.0,5.2,100)

#3mm endmill for boltholes
if facemill == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/flowcell/flowcell-boltholes-inlets(3mm).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )

    g.feed(300)
    g.abs_move(Z=1.0)
    
    drill_peck (-(channel_length-channel_size)/2,0,thickness/2,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100) #inlet
    drill_peck (-(boss_length/2+clearance/4),-(boss_width/2+clearance/4),thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck (-(part_length-clearance/2)/4,-(boss_width/2+clearance/4),thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck (0,-(boss_width/2+clearance/4),thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck ((part_length-clearance/2)/4,-(boss_width/2+clearance/4),thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck ((boss_length/2+clearance/4),-(boss_width/2+clearance/4),thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck ((channel_length-channel_size)/2,0,thickness/2,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100) #inlet
    
    drill_peck ((boss_length/2+clearance/4),(boss_width/2+clearance/4),thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck ((part_length-clearance/2)/4,(boss_width/2+clearance/4),thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck (0,(boss_width/2+clearance/4),thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck (-(part_length-clearance/2)/4,(boss_width/2+clearance/4),thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck (-(boss_length/2+clearance/4),(boss_width/2+clearance/4),thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
        
    g.abs_move(Z=3.0)
    
#3mm endmill for boltholes-gasket
if facemill == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/flowcell/flowcell-boltholes-gasket(3mm).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )

    g.feed(300)
    g.abs_move(Z=1.0)
    
    drill_peck (-(boss_length/2+clearance/4),-(boss_width/2+clearance/4),gasket_cut_depth,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck (-(part_length-clearance/2)/4,-(boss_width/2+clearance/4),gasket_cut_depth,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck (0,-(boss_width/2+clearance/4),gasket_cut_depth,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck ((part_length-clearance/2)/4,-(boss_width/2+clearance/4),gasket_cut_depth,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck ((boss_length/2+clearance/4),-(boss_width/2+clearance/4),gasket_cut_depth,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    
    drill_peck ((boss_length/2+clearance/4),(boss_width/2+clearance/4),gasket_cut_depth,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck ((part_length-clearance/2)/4,(boss_width/2+clearance/4),gasket_cut_depth,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck (0,(boss_width/2+clearance/4),gasket_cut_depth,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck (-(part_length-clearance/2)/4,(boss_width/2+clearance/4),gasket_cut_depth,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
    drill_peck (-(boss_length/2+clearance/4),(boss_width/2+clearance/4),gasket_cut_depth,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,100)
        
      
    g.abs_move(Z=3.0)    


#3mm endmill to cutout
if facemill == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/flowcell/flowcell-cutout(3mm).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    
    #starts bottom left
    g.feed(300)
    g.abs_move(Z=1.0)
    g.abs_move(x=-(part_length+3.0)/2,y=-(part_width+3.0)/2)
    g.abs_move(Z=0)
    
    for i in range(int(thickness/(max_mill_depth_ratio*3))):
        g.feed(100)
        g.move(Z=-3.0*max_mill_depth_ratio)
        
        g.move(x=(part_length+3.0)*0.45)
        g.move(Z=1.0)
        g.move(x=(part_length+3.0)*0.1)
        g.move(Z=-1.0)
        g.move(x=(part_length+3.0)*0.45)
        
        g.move(y=0.4*(part_width+3.0))
        g.move(Z=1.0)
        g.move(y=0.2*(part_width+3.0))
        g.move(Z=-1.0)
        g.move(y=0.4*(part_width+3.0))
        
        g.move(x=-(part_length+3.0)*0.45)
        g.move(Z=1.0)
        g.move(x=-(part_length+3.0)*0.1)
        g.move(Z=-1.0)
        g.move(x=-(part_length+3.0)*0.45)
        
        g.move(y=-0.4*(part_width+3.0))
        g.move(Z=1.0)
        g.move(y=-0.2*(part_width+3.0))
        g.move(Z=-1.0)
        g.move(y=-0.4*(part_width+3.0))
    g.abs_move(Z=1.0)
    
#3mm endmill for gasket
if facemill == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/flowcell/flowcell-gasket(3mm).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    #middle
    g.feed(300)
    g.abs_move(Z=1.0)
    g.abs_move(x=-(boss_length-3.0+gasket_clearance)/2,y=-(boss_width-3.0)/2)
    g.abs_move(Z=0)
    
    for i in range(2):
        g.feed(100)
        g.move(Z=-gasket_cut_depth/2)
        g.move(x=boss_length-3.0+gasket_clearance)
        g.move(y=boss_width-3.0)
        g.move(x=-(boss_length-3.0+gasket_clearance))
        g.move(y=-(boss_width-3.0))
    g.abs_move(Z=1)         
    
    #cutout
    g.feed(300)
    g.abs_move(Z=1.0)
    g.abs_move(x=-(part_length+3.0)/2,y=-(part_width+3.0)/2)
    g.abs_move(Z=0)
    
    for i in range(int(gasket_cut_depth)):
        g.feed(100)
        g.move(Z=-1.0)
        
        g.move(x=(part_length+3.0)*0.45)
        g.move(Z=1.0)
        g.move(x=(part_length+3.0)*0.1)
        g.move(Z=-1.0)
        g.move(x=(part_length+3.0)*0.45)
        
        g.move(y=0.4*(part_width+3.0))
        g.move(Z=1.0)
        g.move(y=0.2*(part_width+3.0))
        g.move(Z=-1.0)
        g.move(y=0.4*(part_width+3.0))
        
        g.move(x=-(part_length+3.0)*0.45)
        g.move(Z=1.0)
        g.move(x=-(part_length+3.0)*0.1)
        g.move(Z=-1.0)
        g.move(x=-(part_length+3.0)*0.45)
        
        g.move(y=-0.4*(part_width+3.0))
        g.move(Z=1.0)
        g.move(y=-0.2*(part_width+3.0))
        g.move(Z=-1.0)
        g.move(y=-0.4*(part_width+3.0))
    g.abs_move(Z=1.0)

#To end
#g.view(backend='matplotlib')
#g.view()
g.teardown()