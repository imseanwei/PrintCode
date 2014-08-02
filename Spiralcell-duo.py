from mecode import G
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/Spiralcell-duo.txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = True, 
        )
#Define variables
printvel = 100	#printvel; mm/min  
tipsize = 0.100	#tipsize; mm  
layerheight =  1*tipsize  #stepheight; mm  
layers = 9    #layers
COM_anode = 1		#air-line  
COM_cathode = 2
pressure_anode= 60	#air-pressure,psi  
pressure_cathode= 60	#air-pressure,psi  
leadinx = 3 	#leadinx; mm  
out_wall = 3			#outer-wall-side-length; mm  
gap = 0.05 	#middle-wall-side-length; mm  
trace = tipsize

def set_pressure(COM, pressure):
    g.write('M9000 P{} Q{}'.format(COM, pressure))
    
def apply_pressure():
    g.write('M9001')
    
def set_apply_pressure(COM, pressure):
    g.write('M9002 P{} Q{}'.format(COM, pressure))
    
def shut_off_pressure():
    g.write('M10000')

def spiral(out_wall, gap, trace):
      length = out_wall
      length_limit = 3*trace
      #starts from upper left
      g.move(x=length)
      while length > length_limit:
          length = length-trace-gap
          g.move(y=-length)
          g.move(x=-length)
          length = length-trace-gap
          g.move(y=length)
          g.move(x=length)

def spiral_reverse(out_wall, gap, trace):
      length = out_wall-tipsize
      length_limit = 3*trace
      #starts from bottom right
      g.move(x=-length)
      while length > length_limit:
          length = length-trace-gap
          g.move(y=length)
          g.move(x=length)
          length = length-trace-gap
          g.move(y=-length)
          g.move(x=-length)

#Code starts
g.set_home(x=0,y=0,Z=0)
g.feed(printvel)

#----spiral 
g.move(x=-leadinx)

set_apply_pressure(COM_anode, pressure_anode)

g.dwell(1)
 
g.move(x=leadinx)

spiral(out_wall, gap, trace)

shut_off_pressure()

g.dwell(5)

g.move(Z=3)

#-----transition
g.abs_move(x=out_wall, y=-out_wall, Z=0)
g.set_home(x=0, y=0, Z=0)

#-----spiral_reverse------
g.move(x=leadinx)

set_apply_pressure(COM_cathode, pressure_cathode)

g.dwell(1)

g.move(x=-leadinx)

spiral_reverse(out_wall, gap, trace)

shut_off_pressure()

g.dwell(5)

g.move(Z=3)

#To end
#g.view(backend='matplotlib')
#g.view()
g.teardown()