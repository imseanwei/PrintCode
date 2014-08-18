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

facemill = True
#w/ 3mm endmill
facemill_depth = 0.3 #in mm
facemill_length = 80 #in mm
facemill_width = 120 #in mm

#Global variables 
outlet_size = 0.250 #in mm
outlet_length = 1
outlet_shift = 3
outlet_filter_gap = 6
connection_size = 0.4
thickness = 12.0
bolt_hole_size = 3.0
mount_hole_size = 6.0
max_mill_depth_ratio = 0.25
separator_width = 0.075


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
filter_starting_y_position = outlet_length+outlet_filter_gap
filter_ending_y_position = filter_starting_y_position+filter_leadin+2*filter_triangle_height+filter_triangle_spacing+filter_leadout+filter_endmill_size/2

inlet_to_filter_leadin = 30

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
        #g.arc(x=0,y=0,radius=-(hole_size-endmill_size)/2)
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
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/duo-printhead/Duo-Printhead-facemill(M3).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    
    #starts bottom left
    mill_face (facemill_depth,facemill_width,facemill_length)    
    
    
    

#250mm endmill for outlet
if facemill == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/duo-printhead/Duo-Printhead-outlet(250um).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )

    #outlet
    g.abs_move(x=0,y=-outlet_size)
    g.abs_move(Z=0)
    for i in range(4):
        g.move(Z=-outlet_size/4)
        g.move(y=outlet_length)
        g.move(y=-outlet_length)
    g.abs_move(Z=1)
    g.abs_move(x=0,y=outlet_length)
    g.abs_move(Z=0)
    for i in range(4):
        g.move(Z=-outlet_size/4)
        g.move(x=outlet_shift)
        g.move(y=connection_size-outlet_size)
        g.move(x=-outlet_shift)
        g.move(y=-(connection_size-outlet_size))
    g.abs_move(Z=3)        
    
    
    
    
#3mm endmill for outlet leveling and bolt/mount holes
if holes == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/duo-printhead/Duo-Printhead-holes(M3).txt",
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
    drill_peck (0+filter_width/4,filter_starting_y_position+filter_leadout-1,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#outlet
    drill_peck (0,2+outlet_length,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#outlet
    drill_peck (-(filter_width/4),filter_starting_y_position+filter_leadout-1,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#outlet
    drill_peck (-(filter_width/2+5),(filter_starting_y_position+filter_ending_y_position)/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (0,(filter_starting_y_position+filter_ending_y_position)/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (+filter_width/2+5,(filter_starting_y_position+filter_ending_y_position)/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (+filter_width/4,filter_ending_y_position-filter_leadin+1,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filter
    drill_peck (-(filter_width/4),filter_ending_y_position-filter_leadin+1,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filter  
    drill_peck (+inlet_to_filter_leadin,filter_ending_y_position,thickness/2,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#inlet
    drill_peck (+inlet_to_filter_leadin-8,filter_ending_y_position+5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet
    drill_peck (+inlet_to_filter_leadin+8,filter_ending_y_position-5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet
    drill_peck (-(inlet_to_filter_leadin-8),filter_ending_y_position+5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet-opposite
    drill_peck (-(inlet_to_filter_leadin+8),filter_ending_y_position-5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet-opposite 
    drill_peck (0,filter_ending_y_position+5+25.4/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#alignment-top
    mill_hole (0,filter_ending_y_position+5,thickness,drill_peck_step,3.0,6.0,500)#bolt-hole
    mill_hole (0,filter_ending_y_position+5+25.4,thickness,drill_peck_step,3.0,6.0,500)#bolt-hole
    

    #with 1mm endmill to create filter 
if filter_section == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/duo-printhead/Duo-Printhead-filter(1mm).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    
    #outlet to filter connection
    g.abs_move(Z=1)
    g.abs_move(x=outlet_shift,y=outlet_length)
    g.abs_move(Z=0)
    g.move(Z=-outlet_size)
    g.move(y=outlet_filter_gap)
    g.move(x=-outlet_shift)
    g.move(x=outlet_shift)
    g.move(y=-outlet_filter_gap)
    g.move(Z=1)
      
            
    #outline filter
    g.feed(500)
    g.abs_move(x=0,y=filter_starting_y_position+filter_endmill_size/2-outlet_size/2)
    g.abs_move(Z=0)
    g.abs_move(Z=-filter_small_size)
    g.move(y=filter_leadout)
    g.abs_move(Z=0)
    
    mill_triangle (filter_small_size,filter_small_size,filter_width,-filter_triangle_height,filter_endmill_size,feedrate=500)
    
    g.abs_move(x= -filter_width/2,y=filter_starting_y_position+filter_leadout+filter_triangle_height+filter_channel_length+filter_endmill_size)
    
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
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/duo-printhead/Duo-Printhead-filter(200um).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    g.feed(100)
    g.abs_move(Z=1)
    g.abs_move(x= -filter_width/2,y=filter_starting_y_position+filter_leadout+filter_triangle_height+filter_endmill_size/2-filter_small_size/2)
    for i in range(filter_small_channel_amount/2):
        g.abs_move(Z=-filter_small_size)
        g.move(y=filter_channel_length+filter_small_size)
        g.move(y=-(filter_channel_length+filter_small_size))
        g.abs_move(Z=1)
        g.move(x=3*filter_small_size)
    g.abs_move(x= +filter_width/2,y=filter_starting_y_position+filter_leadout+filter_triangle_height+filter_endmill_size/2-filter_small_size/2)
    for i in range(filter_small_channel_amount/2):
        g.abs_move(Z=-filter_small_size)
        g.move(y=filter_channel_length+filter_small_size)
        g.move(y=-(filter_channel_length+filter_small_size))
        g.abs_move(Z=1)
        g.move(x=-3*filter_small_size)
    g.abs_move(x= -filter_width/2,y=filter_starting_y_position+filter_leadout+filter_triangle_height+filter_endmill_size/2-filter_small_size/2+2*filter_channel_length)
    for i in range(filter_mid_channel_amount/2):
        g.abs_move(Z=-filter_small_size)
        g.move(y=filter_channel_length+filter_small_size)
        g.move(x=filter_mid_size-filter_small_size)
        g.move(y=-(filter_channel_length+filter_small_size))
        g.move(x=-(filter_mid_size-filter_small_size))
        g.abs_move(Z=1)
        g.move(x=3*filter_mid_size)    
    g.abs_move(x= +filter_width/2,y=filter_starting_y_position+filter_leadout+filter_triangle_height+filter_endmill_size/2-filter_small_size/2+2*filter_channel_length)
    for i in range(filter_mid_channel_amount/2):
        g.abs_move(Z=-filter_small_size)
        g.move(y=filter_channel_length+filter_small_size)
        g.move(x=filter_mid_size-filter_small_size)
        g.move(y=-(filter_channel_length+filter_small_size))
        g.move(x=-(filter_mid_size-filter_small_size))
        g.abs_move(Z=1)
        g.move(x=-3*filter_mid_size)  
    g.abs_move(x= -filter_width/2,y=filter_starting_y_position+filter_leadout+filter_triangle_height+filter_endmill_size/2-filter_small_size/2+4*filter_channel_length)
    for i in range(filter_large_channel_amount/2):
        g.abs_move(Z=-filter_small_size)
        g.move(y=filter_channel_length+filter_small_size)
        g.move(x=filter_large_size-filter_small_size)
        g.move(y=-(filter_channel_length+filter_small_size))
        g.move(x=-(filter_large_size-filter_small_size))
        g.abs_move(Z=1)
        g.move(x=3*filter_large_size)  
    g.abs_move(x= +filter_width/2,y=filter_starting_y_position+filter_leadout+filter_triangle_height+filter_endmill_size/2-filter_small_size/2+4*filter_channel_length)
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
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/duo-printhead/Duo-Printhead-cutout(3mm).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    g.feed(500)
    g.abs_move(Z=1)
    g.abs_move(x=0,y=0)
    g.abs_move(x=-notch_length/2,y=-3/2)
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


#3mm endmill for outlet leveling and bolt/mount holes
if holes == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/duo-printhead/Duo-Printhead-holes-b(M3).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
        
    
    #notch
    g.feed(500)
    g.abs_move(Z=3)
    g.abs_move(x=-notch_length/2+separator_width+outlet_size,y=-3.0/2)
    g.abs_move(Z=0)
    for i in range (int(thickness)):
        g.move(Z=-1)
        g.move(x=notch_length)
        g.move(x=-notch_length)
    g.abs_move(Z=3)


    #peck-drilling bolt/alignment holes
    g.feed(500)
    drill_peck (separator_width+outlet_size+filter_width/4,filter_starting_y_position+filter_leadout-1,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#outlet
    drill_peck (separator_width+outlet_size,2+outlet_length,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#outlet
    drill_peck (separator_width+outlet_size-(filter_width/4),filter_starting_y_position+filter_leadout-1,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#outlet
    drill_peck (separator_width+outlet_size-(filter_width/2+5),(filter_starting_y_position+filter_ending_y_position)/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (separator_width+outlet_size,(filter_starting_y_position+filter_ending_y_position)/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (separator_width+outlet_size+filter_width/2+5,(filter_starting_y_position+filter_ending_y_position)/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filters
    drill_peck (separator_width+outlet_size+filter_width/4,filter_ending_y_position-filter_leadin+1,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filter
    drill_peck (separator_width+outlet_size-(filter_width/4),filter_ending_y_position-filter_leadin+1,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-filter  
    drill_peck (inlet_to_filter_leadin,filter_ending_y_position,thickness/2,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#inlet
    drill_peck (separator_width+outlet_size+inlet_to_filter_leadin-8,filter_ending_y_position+5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet
    drill_peck (separator_width+outlet_size+inlet_to_filter_leadin+8,filter_ending_y_position-5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet
    drill_peck (separator_width+outlet_size-(inlet_to_filter_leadin-8),filter_ending_y_position+5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet-opposite
    drill_peck (separator_width+outlet_size-(inlet_to_filter_leadin+8),filter_ending_y_position-5,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#bolt-inlet-opposite 
    drill_peck (separator_width+outlet_size,filter_ending_y_position+5+25.4/2,thickness,drill_peck_step,drill_peck_retract,drill_peck_rest,3.0,500)#alignment-top
    mill_hole (separator_width+outlet_size,filter_ending_y_position+5,thickness,drill_peck_step,3.0,6.0,500)#bolt-hole
    mill_hole (separator_width+outlet_size,filter_ending_y_position+5+25.4,thickness,drill_peck_step,3.0,6.0,500)#bolt-hole
    


#with 3mm endmill to cut-out
if cutout == True:
    g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/duo-printhead/Duo-Printhead-cutout-b(3mm).txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )
    g.feed(500)
    g.abs_move(Z=1)
    g.abs_move(x=0,y=0)
    g.abs_move(x=-notch_length/2+separator_width+outlet_size,y=-3/2)
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

#To end
#g.view(backend='matplotlib')
#g.view()
g.teardown()