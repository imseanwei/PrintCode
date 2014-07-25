from mecode import G
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/Bok's gasket.pgm",
        #header = "/Users/SeanWei/Documents/Python/mecode/mecode/header_minicaster.txt",
        #footer = "/Users/SeanWei/Documents/Python/mecode/mecode/footer_minicaster.txt",
        #aerotech_include = True,
        direct_write = False,
        print_lines = True, 
        )
#Define variables
printvel = 100	#printvel; mm/min  
tipsize = 0.100	#tipsize; mm  
layerheight =  1*tipsize  #stepheight; mm  
layers = 9    #layers
COM = 5		#air-line  
press= 60	#air-pressure,psi  
leadinx = 3 	#leadinx; mm  
outer_wall_side_length = 6			#outer-wall-side-length; mm  
middle_wall_side_length =  outer_wall_side_length-2*tipsize  	#middle-wall-side-length; mm  
inner_wall_side_length =  middle_wall_side_length-4*tipsize  	#inner-wall-side-length; mm  
cap_side_length =  middle_wall_side_length-2*tipsize  	#cap-side-length; mm  
    

#Code starts
g.set_home(x=0,y=0,z=0)
g.feed(printvel)

#----Lead in--set-----  
g.move(x=-leadinx)

g.set_pressure(COM, press)
g.toggle_pressure(COM)

g.dwell(1)

#----Lead in--go----  
g.move(x=leadinx)

#----outer-wall-----  
g.rect(x=outer_wall_side_length-tipsize, y=outer_wall_side_length-tipsize, direction='CW', start = 'LL')

#----middle-wall-----  
g.move(x=tipsize, y=tipsize)
g.abs_move(z=0)

dummy_z =  layerheight
for i in range(layers):
        g.rect(x=middle_wall_side_length-tipsize, y=middle_wall_side_length-tipsize, direction='CW', start = 'LL')
        g.abs_move(z=dummy_z)
        dummy_z =  dummy_z+layerheight  
        
g.toggle_pressure(COM)
g.dwell(3)

#----inner-wall-----  
g.move(x=2*tipsize, y=2*tipsize)
g.abs_move(z=0)

g.toggle_pressure(COM)

dummy_z =  layerheight
for i in range(layers):
        g.rect(x=inner_wall_side_length-tipsize, y=inner_wall_side_length-tipsize, direction='CW', start = 'LL')
        g.abs_move(z=dummy_z)
        dummy_z =  dummy_z+layerheight  
        
g.toggle_pressure(COM)

#--------cap-------  
g.move (x=-tipsize, y=-tipsize)
g.abs_move(z=(layers-1)*layerheight)  

g.toggle_pressure(COM)

g.rect(x=cap_side_length-tipsize, y=cap_side_length-tipsize, direction='CW', start = 'LL')

g.toggle_pressure(COM)

g.dwell(5)

g.move(z=3)

#To end
g.view(backend='matplotlib')
#g.view()
g.teardown()