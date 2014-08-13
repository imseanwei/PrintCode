from mecode import G

#Global variables
outlet_amount = 2**6	 
outlet_size = 0.250 #in mm
outlet_length = 1 #in mm
#all channels are 1:1 square channels
separator_clearance = 0.075 #in mm
thickness = 12.0
bolt_hole_size = 3.0
mount_hole_size = 6.0
max_mill_depth_ratio = 0.25

#generation0------64 channels
endmill_size_0 = 0.25 #in mm
feedrate_0 = 150 #in mm/s
channel_size_0 = 1*outlet_size
center_to_center_distance_0 = 2*channel_size_0+2*separator_clearance
channel_length_0= outlet_length
channel_amount_0 = outlet_amount
total_width_of_channels_0 = (channel_amount_0-1)*center_to_center_distance_0
starting_x_position_0 = (0-total_width_of_channels_0/2)
starting_y_position_0 = 0
z_step_0 = max_mill_depth_ratio*endmill_size_0

#generation1------32 channels
endmill_size_1 = 0.5 #in mm
feedrate_1 = 250 #in mm/s
channel_size_1 = 2*outlet_size
center_to_center_distance_1 = 2*center_to_center_distance_0
channel_length_1= 0.5+channel_length_0 #in mm
channel_amount_1 = channel_amount_0/2
total_width_of_channels_1 = (channel_amount_1-1)*center_to_center_distance_1
starting_x_position_1 = (0-total_width_of_channels_1/2)
starting_y_position_1 = (channel_length_0+starting_y_position_0+(endmill_size_1-endmill_size_0)/2)
z_step_1 = max_mill_depth_ratio*endmill_size_1

#generation2------16 channels
endmill_size_2 = 0.5 #in mm
feedrate_2 = 250 #in mm/s
channel_size_2 = 3*outlet_size
center_to_center_distance_2 = 2*center_to_center_distance_1
channel_length_2= 0.5+channel_length_1 #in mm
channel_amount_2 = channel_amount_1/2
total_width_of_channels_2 = (channel_amount_2-1)*center_to_center_distance_2
starting_x_position_2 = (0-total_width_of_channels_2/2)
starting_y_position_2 = (channel_length_1+starting_y_position_1+(endmill_size_2-endmill_size_1)/2)
z_step_2 = max_mill_depth_ratio*endmill_size_2

#generation3------8 channels
endmill_size_3 = 1 #in mm
feedrate_3 = 500 #in mm/s
channel_size_3 = 4*outlet_size
center_to_center_distance_3 = 2*center_to_center_distance_2
channel_length_3= 0.5+channel_length_2 #in mm
channel_amount_3 = channel_amount_2/2
total_width_of_channels_3 = (channel_amount_3-1)*center_to_center_distance_3
starting_x_position_3 = (0-total_width_of_channels_3/2)
starting_y_position_3 = (channel_length_2+starting_y_position_2+(endmill_size_3-endmill_size_2)/2)
z_step_3 = max_mill_depth_ratio*endmill_size_3

#generation4------4 channels
endmill_size_4 = 1 #in mm
feedrate_4 = 500 #in mm/s
channel_size_4 = 5*outlet_size
center_to_center_distance_4 = 2*center_to_center_distance_3
channel_length_4= 0.5+channel_length_3 #in mm
channel_amount_4 = channel_amount_3/2
total_width_of_channels_4 = (channel_amount_4-1)*center_to_center_distance_4
starting_x_position_4 = (0-total_width_of_channels_4/2)
starting_y_position_4 = (channel_length_3+starting_y_position_3+(endmill_size_4-endmill_size_3)/2)
z_step_4 = max_mill_depth_ratio*endmill_size_4

#generation5------2 channels
endmill_size_5 = 1 #in mm
feedrate_5 = 500 #in mm/s
channel_size_5 = 6*outlet_size
center_to_center_distance_5 = 2*center_to_center_distance_4
channel_length_5= 0.5+channel_length_4 #in mm
channel_amount_5 = channel_amount_4/2
total_width_of_channels_5 = (channel_amount_5-1)*center_to_center_distance_5
starting_x_position_5 = (0-total_width_of_channels_5/2)
starting_y_position_5 = (channel_length_4+starting_y_position_4+(endmill_size_5-endmill_size_4)/2)
z_step_5 = max_mill_depth_ratio*endmill_size_5

ending_y_position = (channel_length_5+starting_y_position_5)

generations = [
    (starting_x_position_0,starting_y_position_0,channel_amount_0,channel_size_0,channel_length_0,center_to_center_distance_0,z_step_0,endmill_size_0,feedrate_0),
    (starting_x_position_1,starting_y_position_1,channel_amount_1,channel_size_1,channel_length_1,center_to_center_distance_1,z_step_1,endmill_size_1,feedrate_1),
    (starting_x_position_2,starting_y_position_2,channel_amount_2,channel_size_2,channel_length_2,center_to_center_distance_2,z_step_2,endmill_size_2,feedrate_2),
    (starting_x_position_3,starting_y_position_3,channel_amount_3,channel_size_3,channel_length_3,center_to_center_distance_3,z_step_3,endmill_size_3,feedrate_3),
    (starting_x_position_4,starting_y_position_4,channel_amount_4,channel_size_4,channel_length_4,center_to_center_distance_4,z_step_4,endmill_size_4,feedrate_4),
    (starting_x_position_5,starting_y_position_5,channel_amount_5,channel_size_5,channel_length_5,center_to_center_distance_5,z_step_5,endmill_size_5,feedrate_5),
]

facemill = True
#w/ 3mm endmill
facemill_depth = 0.3 #in mm
facemill_length = 80 #in mm
facemill_width = 120 #in mm

filter_section = True
filter_endmill_size = 1.0
filter_leadout = 5
filter_leadin = 5
filter_width = 40
filter_triangle_height = 5
filter_large_size = 0.350
filter_mid_size = 0.275
filter_small_size = 0.200
filter_large_channel_amount = 32
filter_mid_channel_amount = 40
filter_small_channel_amount = 56
filter_channel_length = 1
filter_triangle_spacing = 5
filter_starting_y_position = ending_y_position+(filter_endmill_size-endmill_size_5)/2
filter_ending_y_position = filter_starting_y_position+filter_leadin+2*filter_triangle_height+filter_triangle_spacing+filter_leadout+filter_endmill_size/2

inlet_to_filter_leadin = 30

holes = True
drill_peck_step = 1.0
drill_peck_retract = 1.0
drill_peck_rest = 3.0
notch_depth = thickness
notch_width = 3.0
notch_length = total_width_of_channels_0 + 15.0


cutout = True

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



def mill_channel_vertical (channel_width,channel_length,channel_depth,z_step,endmill_size,feedrate):
    #channel_size/z_step must be integer
    if channel_width == endmill_size:
        g.feed(feedrate)
        for i in range(int(channel_depth/z_step)):
            g.move(Z=-z_step)
            g.move(y=channel_length-endmill_size/2)
            g.move(y=-(channel_length-endmill_size/2))
    else:
        g.feed(feedrate)
        for i in range(int(channel_depth/z_step)):
            g.move(Z=-z_step)
            g.move(y=channel_length-endmill_size/2)
            g.move(x=channel_depth-endmill_size)
            g.move(y=-(channel_length-endmill_size/2))
            g.move(x=-(channel_depth-endmill_size))
    g.abs_move(Z=1)
            
def mill_channel_horizontal (channel_width,channel_length,channel_depth,z_step,endmill_size,feedrate):
    #channel_size/z_step must be integer
    if channel_width == endmill_size:
        g.feed(feedrate)
        for i in range(int(channel_depth/z_step)):
            g.move(Z=-z_step)
            g.move(x=channel_length-endmill_size/2)
            g.move(x=-(channel_length-endmill_size/2))
    else:
        g.feed(feedrate)
        for i in range(int(channel_depth/z_step)):
            g.move(Z=-z_step)
            g.move(x=channel_length-endmill_size/2)
            g.move(y=channel_depth-endmill_size)
            g.move(x=-(channel_length-endmill_size/2))
            g.move(y=-(channel_depth-endmill_size))
    g.abs_move(Z=1)

def mill_n_shaped_channel (channel_size,channel_length,center_to_center_distance,z_step,endmill_size,feedrate):
    #channel_size/z_step must be integer
    #channel_size must be <= 2*endmill_size
    g.feed(feedrate)
    g.abs_move(Z=0)
    loops = int(channel_size/z_step)
    for i in range(loops):
        g.move(Z=-z_step)
        g.move(y=channel_length-endmill_size/2)
        g.move(x=(center_to_center_distance+channel_size-endmill_size))
        g.move(y=-(channel_length-endmill_size/2))
        g.move(x=-(channel_size-endmill_size))
        g.move(y=(channel_length-endmill_size/2-(channel_size-endmill_size)))
        g.move(x=-(center_to_center_distance-channel_size+endmill_size))
        g.move(y=-(channel_length-endmill_size/2-(channel_size-endmill_size)))
        g.move(x=-(channel_size-endmill_size))
    g.abs_move(Z=1)

def mill_n_shaped_channels (starting_x_position,starting_y_position,channel_amount,channel_size,channel_length,center_to_center_distance,z_step,endmill_size,feedrate):
    g.feed(feedrate)
    g.abs_move(starting_x_position,starting_y_position)  
    for i in range(int(channel_amount/2)):
        g.abs_move(Z=0)
        mill_n_shaped_channel (channel_size,channel_length,center_to_center_distance,z_step,endmill_size,feedrate)
        g.move(x=2*center_to_center_distance)


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
        g.move(Z=-z_step*i)
        g.abs_move(Z=z_retract)
    g.abs_move(Z=z_rest)

def mill_hole (x_position,y_position,z_depth,z_step,endmill_size,hole_size,feedrate):
    g.feed(feedrate)
    g.abs_move(Z=1)
    g.abs_move(x=x_position,y=y_position)
    g.move(x=-(hole_size-endmill_size)/2)
    g.abs_move(Z=0)
    for i in range (int(z_depth/z_step)):
        g.move(Z=-z_step)
        g.arc(x=0,y=0,radius=-(hole_size-endmill_size)/2)
        line = 'G2 X0 Y0 I{} J0 F{}'.format((hole_size-endmill_size)/2, feedrate)
        g.write(line)
    g.abs_move(Z=1)
    
def mill_triangle (z_depth,z_step,triangle_long_side,triangle_height,endmill_size,feedrate):
#long_side_down,equal_short_sides

    g.feed(feedrate)
    g.abs_move(Z=0)
    mill_step = endmill_size*2/3
    
    if triangle_height > 0:
        slope = ((triangle_long_side/2-endmill_size/2)/(triangle_height-endmill_size/2)) #x/y
        for i in range (int(z_depth/z_step)):
            g.move(Z=-z_step)
            g.move(x=-(triangle_long_side/2-endmill_size/2),y=-(triangle_height-endmill_size/2))
            g.move(x=(triangle_long_side-endmill_size))
            g.move(x=-(triangle_long_side/2-endmill_size/2),y=(triangle_height-endmill_size/2))
            for i in range (int((triangle_height-endmill_size/2)/mill_step)):
                g.move(x=-mill_step*slope,y=-mill_step)
                g.move(x=2*(i+1)*mill_step*slope)
                g.move(x=-2*(i+1)*mill_step*slope)
            g.move(x=mill_step*slope*int((triangle_height-endmill_size/2)/mill_step),y=(mill_step)*int((triangle_height-endmill_size/2)/mill_step))
        g.abs_move(Z=1)
    else:
        slope = ((triangle_long_side/2-endmill_size/2)/(triangle_height+endmill_size/2)) #x/y
        for i in range (int(z_depth/z_step)):
            g.move(Z=-z_step)
            g.move(x=-(triangle_long_side/2-endmill_size/2),y=-(triangle_height+endmill_size/2))
            g.move(x=(triangle_long_side-endmill_size))
            g.move(x=-(triangle_long_side/2-endmill_size/2),y=(triangle_height+endmill_size/2))
            for i in range (int(-(triangle_height+endmill_size/2)/mill_step)):
                g.move(x=-mill_step*slope,y=mill_step)
                g.move(x=2*(i+1)*mill_step*slope)
                g.move(x=-2*(i+1)*mill_step*slope)
            g.move(x=mill_step*slope*int(-(triangle_height+endmill_size/2)/mill_step),y=-(mill_step)*int(-(triangle_height+endmill_size/2)/mill_step))
        g.abs_move(Z=1)
        


#3mm endmill to facemill
if facemill == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/multinozzle/multinozzle-facemill(M3).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    
    #starts bottom left
    mill_face (facemill_depth,facemill_width,facemill_length)    
    
    

#3mm endmill for outlet leveling and bolt/mount holes & filter outline
if holes == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/multinozzle/multinozzle-anode-holes(M3).txt",
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
    mill_channel_horizontal (notch_width,notch_length,notch_depth,z_step=3*max_mill_depth_ratio,endmill_size=3.0,feedrate=500)
    g.abs_move(Z=3)


    #peck-drilling bolt/alignment holes
    g.feed(500)
    drill_peck (starting_x_position_0-3,starting_y_position_2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-channels
    drill_peck (-starting_x_position_0+3,starting_y_position_2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-channels
    drill_peck (0,starting_y_position_5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-channels
    drill_peck (starting_x_position_0,filter_starting_y_position+4,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#alignment-bottom left
    drill_peck (starting_x_position_0/2,filter_starting_y_position+4,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (-starting_x_position_0/2,filter_starting_y_position+4,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (-starting_x_position_0,filter_starting_y_position+4,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#alignment-bottom right
    drill_peck (-(filter_width/2+5),(filter_starting_y_position+filter_ending_y_position)/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (0,(filter_starting_y_position+filter_ending_y_position)/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (filter_width/2+5,(filter_starting_y_position+filter_ending_y_position)/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (starting_x_position_0/2,filter_ending_y_position-4,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (-starting_x_position_0/2,filter_ending_y_position-4,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (inlet_to_filter_leadin,filter_ending_y_position,thickness/2,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#inlet
    drill_peck (inlet_to_filter_leadin-8,filter_ending_y_position+5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet
    drill_peck (inlet_to_filter_leadin+8,filter_ending_y_position-5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet
    drill_peck (-(inlet_to_filter_leadin-8),filter_ending_y_position+5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet-opposite
    drill_peck (-(inlet_to_filter_leadin+8),filter_ending_y_position-5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet-opposite
    
    
    drill_peck (0,filter_ending_y_position+5+25.4/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#alignment-top
    mill_hole (0,filter_ending_y_position+5,thickness,drill_peck_step,3.0,6.0,500)#bolt-hole
    mill_hole (0,filter_ending_y_position+5+25.4,thickness,drill_peck_step,3.0,6.0,500)#bolt-hole
    

#3mm endmill for outlet leveling and bolt/mount holes & filter outline
if holes == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/multinozzle/multinozzle-cathode-holes(M3).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
        
    
    #notch
    g.feed(500)
    g.abs_move(Z=3)
    g.abs_move(x=-notch_length/2+center_to_center_distance_0/2,y=-3.0/2)
    g.abs_move(Z=0)
    mill_channel_horizontal (notch_width,notch_length,notch_depth,z_step=3*max_mill_depth_ratio,endmill_size=3.0,feedrate=500)
    g.abs_move(Z=3)


    #peck-drilling bolt/alignment holes
    g.feed(500)
    drill_peck (starting_x_position_0-3+center_to_center_distance_0/2,starting_y_position_2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-channels
    drill_peck (-starting_x_position_0+3+center_to_center_distance_0/2,starting_y_position_2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-channels
    drill_peck (0+center_to_center_distance_0/2,starting_y_position_5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-channels
    drill_peck (starting_x_position_0+center_to_center_distance_0/2,filter_starting_y_position+4,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#alignment-bottom left
    drill_peck (starting_x_position_0/2+center_to_center_distance_0/2,filter_starting_y_position+4,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (-starting_x_position_0/2+center_to_center_distance_0/2,filter_starting_y_position+4,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (-starting_x_position_0+center_to_center_distance_0/2,filter_starting_y_position+4,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#alignment-bottom right
    drill_peck (-(filter_width/2+5)+center_to_center_distance_0/2,(filter_starting_y_position+filter_ending_y_position)/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (0+center_to_center_distance_0/2,(filter_starting_y_position+filter_ending_y_position)/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (filter_width/2+5+center_to_center_distance_0/2,(filter_starting_y_position+filter_ending_y_position)/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (starting_x_position_0/2+center_to_center_distance_0/2,filter_ending_y_position-4,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (-starting_x_position_0/2+center_to_center_distance_0/2,filter_ending_y_position-4,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (inlet_to_filter_leadin+center_to_center_distance_0/2,filter_ending_y_position,thickness/2,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#inlet
    drill_peck (inlet_to_filter_leadin-8+center_to_center_distance_0/2,filter_ending_y_position+5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet
    drill_peck (inlet_to_filter_leadin+8+center_to_center_distance_0/2,filter_ending_y_position-5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet
    drill_peck (-(inlet_to_filter_leadin-8)+center_to_center_distance_0/2,filter_ending_y_position+5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet-opposite
    drill_peck (-(inlet_to_filter_leadin+8)+center_to_center_distance_0/2,filter_ending_y_position-5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet-opposite
    
    
    drill_peck (0+center_to_center_distance_0/2,filter_ending_y_position+5+25.4/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#alignment-top
    mill_hole (0+center_to_center_distance_0/2,filter_ending_y_position+5,thickness,drill_peck_step,3.0,6.0,500)#bolt-hole
    mill_hole (0+center_to_center_distance_0/2,filter_ending_y_position+5+25.4,thickness,drill_peck_step,3.0,6.0,500)#bolt-hole


#3mm endmill for outlet leveling and bolt/mount holes & filter outline
if holes == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/multinozzle/multinozzle-gasket-holes(M3).txt",
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
    mill_channel_horizontal (notch_width,notch_length,1,1,endmill_size=3.0,feedrate=500)
    g.abs_move(Z=3)


    #peck-drilling bolt/alignment holes
    g.feed(500)
    drill_peck (starting_x_position_0-3,starting_y_position_2,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-channels
    drill_peck (-starting_x_position_0+3,starting_y_position_2,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-channels
    drill_peck (0,starting_y_position_5,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-channels
    drill_peck (starting_x_position_0,filter_starting_y_position+4,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#alignment-bottom left
    drill_peck (starting_x_position_0/2,filter_starting_y_position+4,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (-starting_x_position_0/2,filter_starting_y_position+4,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (-starting_x_position_0,filter_starting_y_position+4,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#alignment-bottom right
    drill_peck (-(filter_width/2+5),(filter_starting_y_position+filter_ending_y_position)/2,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (0,(filter_starting_y_position+filter_ending_y_position)/2,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (filter_width/2+5,(filter_starting_y_position+filter_ending_y_position)/2,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (starting_x_position_0/2,filter_ending_y_position-4,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (-starting_x_position_0/2,filter_ending_y_position-4,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (inlet_to_filter_leadin-8,filter_ending_y_position+5,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet
    drill_peck (inlet_to_filter_leadin+8,filter_ending_y_position-5,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet
    drill_peck (-(inlet_to_filter_leadin-8),filter_ending_y_position+5,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet-opposite
    drill_peck (-(inlet_to_filter_leadin+8),filter_ending_y_position-5,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet-opposite
    
    
    drill_peck (0,filter_ending_y_position+5+25.4/2,1,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#alignment-top
    mill_hole (0,filter_ending_y_position+5,1,drill_peck_step,3.0,6.0,500)#bolt-hole
    mill_hole (0,filter_ending_y_position+5+25.4,1,drill_peck_step,3.0,6.0,500)#bolt-hole


#multiple endmills for multinozzle
for i, generation in enumerate(generations):
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/multinozzle/multinozzle-channels-gen{}.txt".format(i),
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    
    mill_n_shaped_channels (*generation)
    g.abs_move(Z=3)

#with 1mm endmill to create filter 
if filter_section == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/multinozzle/multinozzle-filter(1mm).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
        
    #outline filter
    g.feed(500)
    g.abs_move(x=0,y=filter_starting_y_position)
    g.abs_move(Z=0)
    g.abs_move(Z=-filter_small_size)
    g.move(y=filter_leadout)
    g.abs_move(Z=0)
    
    mill_triangle (filter_small_size,filter_small_size,filter_width,-filter_triangle_height,filter_endmill_size,feedrate=500)
    
    g.abs_move(x=-filter_width/2,y=filter_starting_y_position+filter_leadout+filter_triangle_height+filter_channel_length+filter_endmill_size)
    
    g.abs_move(Z=-filter_small_size)
    g.move(x=(filter_width-5-filter_endmill_size)/2)
    g.abs_move(Z=1)
    g.move(x=(5+filter_endmill_size))
    g.abs_move(Z=-filter_small_size)
    g.move(x=(filter_width-5-filter_endmill_size)/2)
    g.abs_move(Z=1)
    
    g.move(y=2*filter_channel_length)
    
    g.abs_move(Z=-filter_small_size)
    g.move(x=-(filter_width-5-filter_endmill_size)/2)
    g.abs_move(Z=1)
    g.move(x=-(5+filter_endmill_size))
    g.abs_move(Z=-filter_small_size)
    g.move(x=-(filter_width-5-filter_endmill_size)/2)
    g.abs_move(Z=1)
        
    g.abs_move(Z=1)
    g.abs_move(x=0,y=filter_ending_y_position-filter_leadout)
    g.abs_move(Z=0)
    
    mill_triangle (filter_small_size,filter_small_size,filter_width,filter_triangle_height,filter_endmill_size,feedrate=500)
    
    g.abs_move(x=0,y=filter_ending_y_position)
    g.abs_move(Z=-filter_small_size)
    g.move(y=filter_leadin)
    g.move(x=inlet_to_filter_leadin)
    g.abs_move(Z=3)

#with 200um endmill to create filter 
if filter_section == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/multinozzle/multinozzle-filter(200um).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    g.feed(100)
    g.abs_move(Z=1)
    g.abs_move(x=-filter_width/2,y=filter_starting_y_position+filter_leadout+filter_triangle_height+filter_endmill_size/2-filter_small_size/2)
    for i in range(filter_small_channel_amount/2):
        g.abs_move(Z=-filter_small_size)
        g.move(y=filter_channel_length+filter_small_size)
        g.move(y=-(filter_channel_length+filter_small_size))
        g.abs_move(Z=1)
        g.move(x=3*filter_small_size)
    g.abs_move(x=filter_width/2,y=filter_starting_y_position+filter_leadout+filter_triangle_height+filter_endmill_size/2-filter_small_size/2)
    for i in range(filter_small_channel_amount/2):
        g.abs_move(Z=-filter_small_size)
        g.move(y=filter_channel_length+filter_small_size)
        g.move(y=-(filter_channel_length+filter_small_size))
        g.abs_move(Z=1)
        g.move(x=-3*filter_small_size)
    g.abs_move(x=-filter_width/2,y=filter_starting_y_position+filter_leadout+filter_triangle_height+filter_endmill_size/2-filter_small_size/2+2*filter_channel_length)
    for i in range(filter_mid_channel_amount/2):
        g.abs_move(Z=-filter_small_size)
        g.move(y=filter_channel_length+filter_small_size)
        g.move(x=filter_mid_size-filter_small_size)
        g.move(y=-(filter_channel_length+filter_small_size))
        g.move(x=-(filter_mid_size-filter_small_size))
        g.abs_move(Z=1)
        g.move(x=3*filter_mid_size)    
    g.abs_move(x=filter_width/2,y=filter_starting_y_position+filter_leadout+filter_triangle_height+filter_endmill_size/2-filter_small_size/2+2*filter_channel_length)
    for i in range(filter_mid_channel_amount/2):
        g.abs_move(Z=-filter_small_size)
        g.move(y=filter_channel_length+filter_small_size)
        g.move(x=filter_mid_size-filter_small_size)
        g.move(y=-(filter_channel_length+filter_small_size))
        g.move(x=-(filter_mid_size-filter_small_size))
        g.abs_move(Z=1)
        g.move(x=-3*filter_mid_size)  
    g.abs_move(x=-filter_width/2,y=filter_starting_y_position+filter_leadout+filter_triangle_height+filter_endmill_size/2-filter_small_size/2+4*filter_channel_length)
    for i in range(filter_large_channel_amount/2):
        g.abs_move(Z=-filter_small_size)
        g.move(y=filter_channel_length+filter_small_size)
        g.move(x=filter_large_size-filter_small_size)
        g.move(y=-(filter_channel_length+filter_small_size))
        g.move(x=-(filter_large_size-filter_small_size))
        g.abs_move(Z=1)
        g.move(x=3*filter_large_size)  
    g.abs_move(x=filter_width/2,y=filter_starting_y_position+filter_leadout+filter_triangle_height+filter_endmill_size/2-filter_small_size/2+4*filter_channel_length)
    for i in range(filter_large_channel_amount/2):
        g.abs_move(Z=-filter_small_size)
        g.move(y=filter_channel_length+filter_small_size)
        g.move(x=filter_large_size-filter_small_size)
        g.move(y=-(filter_channel_length+filter_small_size))
        g.move(x=-(filter_large_size-filter_small_size))
        g.abs_move(Z=1)
        g.move(x=-3*filter_large_size)         
    g.abs_move(Z=3)
    
#with 3mm endmill to cut-out
if cutout == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/multinozzle/multinozzle-anode-cutout(3mm).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    g.feed(500)
    g.abs_move(Z=1)
    g.abs_move(x=0,y=0)
    g.move(x=-notch_length/2,y=-3/2)
    g.move(Z=-1)
    for i in range(int(thickness-1)):
        g.move(Z=-1)
        g.move(x=-(inlet_to_filter_leadin+8+5)-(-notch_length/2),y=filter_ending_y_position+5+5+3/2)
        g.move(x=-8-(-(inlet_to_filter_leadin+8+5)))
        g.move(y=filter_ending_y_position+5+25.4+8-(filter_ending_y_position+5+5+3/2))
        g.move(x=16)
        g.move(y=-(filter_ending_y_position+5+25.4+8-(filter_ending_y_position+5+5+3/2)))
        g.move(x=-8-(-(inlet_to_filter_leadin+8+5)))
        g.move(x=-(inlet_to_filter_leadin+8+5)-(-notch_length/2),y=-(filter_ending_y_position+5+5+3/2))
        g.move(x=-notch_length)
    g.move(Z=-1)
    g.move(x=0.45*(-(inlet_to_filter_leadin+8+5)-(-notch_length/2)),y=0.45*(filter_ending_y_position+5+5+3/2))
    g.move(Z=1)
    g.move(x=0.1*(-(inlet_to_filter_leadin+8+5)-(-notch_length/2)),y=0.1*(filter_ending_y_position+5+5+3/2))
    g.move(Z=-1)
    g.move(x=0.45*(-(inlet_to_filter_leadin+8+5)-(-notch_length/2)),y=0.45*(filter_ending_y_position+5+5+3/2))
    
    g.move(x=-8-(-(inlet_to_filter_leadin+8+5)))
    g.move(y=filter_ending_y_position+5+25.4+8-(filter_ending_y_position+5+5+3/2))
    g.move(x=16)
    g.move(y=-(filter_ending_y_position+5+25.4+8-(filter_ending_y_position+5+5+3/2)))
    g.move(x=-8-(-(inlet_to_filter_leadin+8+5)))
    
    g.move(x=0.45*(-(inlet_to_filter_leadin+8+5)-(-notch_length/2)),y=0.45*(-(filter_ending_y_position+5+5+3/2)))
    g.move(Z=1)
    g.move(x=0.1*(-(inlet_to_filter_leadin+8+5)-(-notch_length/2)),y=0.1*(-(filter_ending_y_position+5+5+3/2)))
    g.move(Z=-1)
    g.move(x=0.45*(-(inlet_to_filter_leadin+8+5)-(-notch_length/2)),y=0.45*(-(filter_ending_y_position+5+5+3/2)))
    g.move(Z=1)
    
    g.abs_move(Z=3)


#with 3mm endmill to cut-out
if cutout == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/multinozzle/multinozzle-cathode-cutout(3mm).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    g.feed(500)
    g.abs_move(Z=1)
    g.abs_move(x=0,y=0)
    g.move(x=-notch_length/2+center_to_center_distance_0/2,y=-3/2)
    g.move(Z=-1)
    for i in range(int(thickness-1)):
        g.move(Z=-1)
        g.move(x=-(inlet_to_filter_leadin+8+5)-(-notch_length/2),y=filter_ending_y_position+5+5+3/2)
        g.move(x=-8-(-(inlet_to_filter_leadin+8+5)))
        g.move(y=filter_ending_y_position+5+25.4+8-(filter_ending_y_position+5+5+3/2))
        g.move(x=16)
        g.move(y=-(filter_ending_y_position+5+25.4+8-(filter_ending_y_position+5+5+3/2)))
        g.move(x=-8-(-(inlet_to_filter_leadin+8+5)))
        g.move(x=-(inlet_to_filter_leadin+8+5)-(-notch_length/2),y=-(filter_ending_y_position+5+5+3/2))
        g.move(x=-notch_length)
    g.move(Z=-1)
    g.move(x=0.45*(-(inlet_to_filter_leadin+8+5)-(-notch_length/2)),y=0.45*(filter_ending_y_position+5+5+3/2))
    g.move(Z=1)
    g.move(x=0.1*(-(inlet_to_filter_leadin+8+5)-(-notch_length/2)),y=0.1*(filter_ending_y_position+5+5+3/2))
    g.move(Z=-1)
    g.move(x=0.45*(-(inlet_to_filter_leadin+8+5)-(-notch_length/2)),y=0.45*(filter_ending_y_position+5+5+3/2))
    
    g.move(x=-8-(-(inlet_to_filter_leadin+8+5)))
    g.move(y=filter_ending_y_position+5+25.4+8-(filter_ending_y_position+5+5+3/2))
    g.move(x=16)
    g.move(y=-(filter_ending_y_position+5+25.4+8-(filter_ending_y_position+5+5+3/2)))
    g.move(x=-8-(-(inlet_to_filter_leadin+8+5)))
    
    g.move(x=0.45*(-(inlet_to_filter_leadin+8+5)-(-notch_length/2)),y=0.45*(-(filter_ending_y_position+5+5+3/2)))
    g.move(Z=1)
    g.move(x=0.1*(-(inlet_to_filter_leadin+8+5)-(-notch_length/2)),y=0.1*(-(filter_ending_y_position+5+5+3/2)))
    g.move(Z=-1)
    g.move(x=0.45*(-(inlet_to_filter_leadin+8+5)-(-notch_length/2)),y=0.45*(-(filter_ending_y_position+5+5+3/2)))
    g.move(Z=1)
    
    g.abs_move(Z=3)

#with 3mm endmill to cut-out
if cutout == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/multinozzle/multinozzle-gasket-cutout(3mm).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    g.feed(500)
    g.abs_move(Z=1)
    g.abs_move(x=0,y=0)
    g.move(x=-notch_length/2,y=-3/2)
    g.move(Z=-1)

    g.move(Z=-1)
    g.move(x=-(inlet_to_filter_leadin+8+5)-(-notch_length/2),y=filter_ending_y_position+5+5+3/2)
    g.move(x=-8-(-(inlet_to_filter_leadin+8+5)))
    g.move(y=filter_ending_y_position+5+25.4+8-(filter_ending_y_position+5+5+3/2))
    g.move(x=16)
    g.move(y=-(filter_ending_y_position+5+25.4+8-(filter_ending_y_position+5+5+3/2)))
    g.move(x=-8-(-(inlet_to_filter_leadin+8+5)))
    g.move(x=-(inlet_to_filter_leadin+8+5)-(-notch_length/2),y=-(filter_ending_y_position+5+5+3/2))
    g.move(x=-notch_length)
    
    g.abs_move(Z=3)



#To end
#g.view(backend='matplotlib')
#g.view()
g.teardown()