from mecode import G
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/spiralcell/Spiralcell.txt",
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
COM = 1		#air-line  
pressure= 70	#air-pressure,psi  
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
      while length >= length_limit:
          length = length-trace-2*gap
          g.move(y=-length)
          g.move(x=-length)
          length = length-trace-2*gap
          g.move(y=length)
          g.move(x=length)

#Code starts
g.set_home(x=0,y=0,Z=0)
g.feed(printvel)

#----Lead in--set-----  
g.move(x=-leadinx)

set_apply_pressure(COM, pressure)

g.dwell(1)

#----Lead in--go----  
g.move(x=leadinx)

spiral(out_wall, gap, trace)

shut_off_pressure()

g.dwell(5)

g.move(Z=3)

#To end
g.view(backend='matplotlib')
#g.view()
g.teardown()