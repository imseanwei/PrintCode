from mecode import G
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/Spiralcell.txt",
        header = "/Users/SeanWei/Documents/Python/mecode/mecode/header-Mach3.rtf",
        footer = "/Users/SeanWei/Documents/Python/mecode/mecode/footer-Mach3.rtf",
        aerotech_include = False,
        direct_write = False,
        print_lines = True, 
        )
#Define variables
printvel = 100	#printvel; mm/min  
tipsize = 0.100	#tipsize; mm  
layerheight =  1*tipsize  #stepheight; mm  
layers = 9    #layers
COM = 5		#air-line  
pressure= 60	#air-pressure,psi  
leadinx = 3 	#leadinx; mm  
outer_wall_side_length = 6			#outer-wall-side-length; mm  
middle_wall_side_length =  outer_wall_side_length-2*tipsize  	#middle-wall-side-length; mm  
inner_wall_side_length =  middle_wall_side_length-4*tipsize  	#inner-wall-side-length; mm  
cap_side_length =  middle_wall_side_length-2*tipsize  	#cap-side-length; mm  

#functions  
def set_pressure(COM, pressure):
    print('M9000 P{} Q{}'.format(COM, pressure))

def apply_pressure():
    print('M9001')
    
def set_apply_pressure(COM, pressure):
    print('M9002 P{} Q{}'.format(COM, pressure))
    
def shut_off_pressure():
    print('M10000')

    
#Code starts
g.set_home(x=0,y=0,Z=0)
g.feed(printvel)

#----Lead in--set-----  
g.move(x=-leadinx)

set_apply_pressure(COM, pressure)

g.dwell(1)

#----Lead in--go----  
g.move(x=leadinx)

#----outer-wall-----  
g.rect(x=outer_wall_side_length-tipsize, y=outer_wall_side_length-tipsize, direction='CW', start = 'LL')

#----middle-wall-----  
g.move(x=tipsize, y=tipsize)
g.abs_move(Z=0)

dummy_z =  layerheight
for i in range(layers):
        g.rect(x=middle_wall_side_length-tipsize, y=middle_wall_side_length-tipsize, direction='CW', start = 'LL')
        g.abs_move(Z=dummy_z)
        dummy_z =  dummy_z+layerheight  
        
shut_off_pressure()
g.dwell(3)

#----inner-wall-----  
g.move(x=2*tipsize, y=2*tipsize)
g.abs_move(Z=0)

set_apply_pressure(COM, pressure)

dummy_z =  layerheight
for i in range(layers):
        g.rect(x=inner_wall_side_length-tipsize, y=inner_wall_side_length-tipsize, direction='CW', start = 'LL')
        g.abs_move(Z=dummy_z)
        dummy_z =  dummy_z+layerheight  
        
shut_off_pressure()

#--------cap-------  
g.move (x=-tipsize, y=-tipsize)
g.abs_move(Z=(layers-1)*layerheight)  

set_apply_pressure(COM, pressure)

g.rect(x=cap_side_length-tipsize, y=cap_side_length-tipsize, direction='CW', start = 'LL')

shut_off_pressure()

g.dwell(5)

g.move(Z=3)

#To end
g.view(backend='matplotlib')
#g.view()
g.teardown()