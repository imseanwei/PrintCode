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

channel_width_large = 0.635 #in mm
channel_width_small = 0.203 #in mm
channel_depth_large = 0.635
channel_depth_small = (channel_width_large+channel_width_small)/2
channel_length = 20 #in mm
endmill_size = 0.2 #in mm
drillbit_size = 3.0 #in mm
hole_size = 3.0 #in mm
inlet_size = 5.25 #in mm
mount_size = 6.0 #in mm
gap = 20 #inlet to mount in mm
spacing = 2 #outlet to bolt

z_loop_channel_large = int(channel_depth_large/(endmill_size*1/3))+1
z_step_channel_large = channel_depth_large/z_loop_channel_large
z_loop_channel_small = int(channel_depth_small/(endmill_size*1/3))+1
z_step_channel_small = channel_depth_small/z_loop_channel_small

facemill = True
#w/ 3mm endmill
facemill_depth = 0.3 #in mm
facemill_length = 110 #in mm
facemill_width = 120 #in mm
thickness = 9.0


holes = True
drill_peck_step = 1.0
drill_peck_retract = 1.0
drill_peck_rest = 3.0
notch_depth = thickness
notch_width = 3.0
notch_length = 5.0

cutout = True


def mill_face (facemill_depth,facemill_width,facemill_length):
#3mm endmill
    g.feed(500)
    g.abs_move(Z=1)
    g.abs_move(x=0,y=0)
    g.abs_move(Z=-facemill_depth)
    g.move(y=facemill_length-3)
    g.move(x=facemill_width-3)
    g.move(y=-(facemill_length-3))
    g.move(x=-(facemill_width-3))
    for i in range(int(facemill_length/4)):
        g.move(x=facemill_width-3)
        g.move(y=2)
        g.move(x=-(facemill_width-3))
        g.move(y=2)
    g.abs_move(Z=1)
    
def drill_peck (x_position,y_position,z_depth,z_step,z_retract,z_rest,hole_endmill_size,feedrate):
    g.feed(feedrate)
    g.abs_move(Z=1)
    g.abs_move(x=x_position,y=y_position)
    g.abs_move(Z=0)
    for i in range (int(z_depth/z_step)):
        g.move(Z=-z_step*(i+1))
        g.abs_move(Z=z_retract)
        g.abs_move(Z=0)
    g.abs_move(Z=z_rest)

def mill_hole (x_position,y_position,z_depth,z_step,endmill_size,hole_size,feedrate):
    g.feed(feedrate)
    g.abs_move(Z=1)
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
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/core-shell-printhead/core-shell-printhead-facemill(M3).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    
    #starts bottom left
    mill_face (facemill_depth,facemill_width,facemill_length)    
    
    g.abs_move(Z=3)

#200um endmill for channels
if facemill == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/core-shell-printhead/core-shell-printhead-channels(200um).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    g.feed(500)
    g.abs_move(Z=1)
    g.abs_move(x=0-(channel_width_large-endmill_size)/2,y=0-endmill_size)
    g.feed(100)
    g.move(Z=-1)
    
    #large channel
    for i in range(z_loop_channel_large):
        g.move(Z=-z_step_channel_large)
        g.move(y=channel_length)
        g.move(x=channel_width_large-endmill_size)
        g.move(y=-channel_length)
        g.move(x=channel_width_large-endmill_size)
        g.move(y=channel_length)
        for i in range(int(channel_width_large/(2*endmill_size*2/3))):
            g.move(y=channel_length)
            g.move(x=endmill_size*2/3)
            g.move(y=-channel_length)
            g.move(x=endmill_size*2/3)
        g.abs_move(x=0-(channel_width_large-endmill_size)/2,y=0-endmill_size)
    
    g.feed(500)
    g.abs_move(Z=1)
    g.abs_move(x=0-(channel_width_small-endmill_size)/2,y=channel_length-endmill_size)
    g.feed(100)
    g.move(Z=-1)
        
    #small channel when channel size < 2*endmill_size
    for i in range(z_loop_channel_small):
        g.move(Z=-z_step_channel_small)
        g.move(y=channel_length)
        g.move(x=channel_width_small-endmill_size)
        g.move(y=-channel_length)
        g.move(x=channel_width_small-endmill_size)
    
    g.abs_move(Z=3)
    
#3mm endmill for outlet leveling and bolt/mount holes
if holes == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/core-shell-printhead/core-shell-printhead-holes(M3).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
        
    
    #notch
    g.feed(500)
    g.abs_move(Z=3)
    g.abs_move(x=-notch_length/2,y=-3.0/2)
    g.abs_move(Z=0)
    for i in range (int(thickness)):
        g.move(Z=-1)
        g.move(x=notch_length)
        g.move(x=-notch_length)
    g.abs_move(Z=3)


    #peck-drilling bolt/alignment holes
    g.feed(500)
    drill_peck (0,channel_length/2,2,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#reservoir
    drill_peck (0,3*channel_length/2,2,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#reservoir
        
    drill_peck (spacing,channel_length/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt
    drill_peck (-spacing,channel_length/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#alignment
    drill_peck (-spacing,2*channel_length/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt
    drill_peck (spacing,2*channel_length/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#alignment
    drill_peck (spacing,3*channel_length/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt
    drill_peck (-spacing,3*channel_length/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#alignment
    drill_peck (-spacing,4*channel_length/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt
    drill_peck (spacing,4*channel_length/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#alignment

    drill_peck (0,2*channel_length+gap+25.4/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#alignment
        
    mill_hole (0,channel_length,thickness,drill_peck_step,drillbit_size,inlet_size,500)#inlet
    mill_hole (0,2*channel_length,thickness,drill_peck_step,drillbit_size,inlet_size,500)#inlet
    mill_hole (0,2*channel_length+gap,thickness,drill_peck_step,drillbit_size,mount_size,500)#mount-hole
    mill_hole (0,2*channel_length+gap+25.4,thickness,drill_peck_step,drillbit_size,mount_size,500)#mount-hole
    
    g.abs_move(Z=3)

#3mm endmill for cutout
if holes == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/core-shell-printhead/core-shell-printhead-cutout(M3).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
        
    g.feed(500)
    g.abs_move(Z=3)
    g.abs_move(x=-notch_length/2,y=-3.0/2)
    g.abs_move(Z=0)
    for i in range (int(thickness)):
        g.move(Z=-1)
        g.move(x=-(2.5*spacing-notch_length/2),y=channel_length/2)
        g.move(y=3*channel_length/2+gap+25.4+6)
        g.move(x=5*spacing)
        g.move(y=-(3*channel_length/2+gap+25.4+6))
        g.move(x=-(2.5*spacing-notch_length/2),y=-channel_length/2)
        g.move(x=-notch_length)
        
    g.abs_move(Z=3)    
    

#To end
#g.view(backend='matplotlib')
#g.view()
g.teardown()