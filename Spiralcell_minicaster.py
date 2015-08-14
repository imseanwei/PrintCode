#Define variables
printvel_left = 4	#printvel
printvel_right = 4	#printvel 
printvel_fill = 4	#printvel  
tipsize = 0.200	#tipsize; mm  
layerheight =  0.8*tipsize  #stepheight; mm  
layers = 1    #layers
COM = 4		#air-line  
pressure_left= 70	#air-pressure,psi  
pressure_right= 70	#air-pressure,psi  
pressure_fill= 70	#air-pressure,psi  
leadin = 3 	#leadinx; mm  
edge = 5			#outer-wall-side-length; mm  
spacing = 0.05 	#middle-wall-side-length; mm  

def spiral_left(edge, tipsize, spacing):

      #starts from middle left
      g.set_home(x=0,y=0,Z=0)
      g.feed(printvel_left)
      g.move(x=-leadin)
      g.set_pressure(COM, pressure_left)
      g.toggle_pressure(COM)
      g.dwell(3)
      g.move(x=leadin)
      
      g.move(y=edge/2-tipsize/2) #from halfway to starting corner
      distance = edge-tipsize*2-spacing
      g.move(x=distance) #1st horizontal line
      g.move(y=-distance) #1st vertical line
      while distance >= 3*tipsize:
          
        distance = distance-tipsize*2-spacing*2
      
        g.move(x=-distance)
        g.move(y=distance)
        
        if distance >= 3*tipsize:
            distance = distance-tipsize*2-spacing*2
      
            g.move(x=distance)
            g.move(y=-distance)
      
      g.toggle_pressure(COM)
      g.dwell(5)
      g.move(Z=3)

def spiral_right(edge, tipsize, spacing):

      #starts from middle right
      g.set_home(x=0,y=0,Z=0)
      g.feed(printvel_right)
      g.move(x=leadin)
      g.set_pressure(COM, pressure_right)
      g.toggle_pressure(COM)
      g.dwell(3)
      g.move(x=-leadin)
      
      g.move(y=-(edge/2-tipsize/2)) #from halfway to starting corner
      distance = edge-tipsize*2-spacing
      g.move(x=-distance) #1st horizontal line
      g.move(y=distance) #1st vertical line
      while distance >= 3*tipsize:
          
        distance = distance-tipsize*2-spacing*2
      
        g.move(x=distance)
        g.move(y=-distance)
        
        if distance >= 3*tipsize:
            distance = distance-tipsize*2-spacing*2
      
            g.move(x=-distance)
            g.move(y=distance)

      g.toggle_pressure(COM)
      g.dwell(5)
      g.move(Z=3)
            
def spiral_fill(edge, tipsize, spacing):

    g.set_home(x=0,y=0,Z=0)
    g.feed(printvel_fill)
      
    for i in range (int(tipsize/spacing)+1):
      #starts from middle left, under spiral left's start
      g.abs_move(x=0,y=0)
      g.move(x=-(leadin+tipsize/2+spacing/2)) 
      g.set_pressure(COM, pressure_fill)
      g.toggle_pressure(COM)
      g.dwell(3)
      g.move(x=leadin+tipsize/2+spacing/2)
      
      g.move(y=edge/2-tipsize/2) #from halfway to starting corner
      distance = edge-tipsize*3-spacing*2
      g.move(x=distance) #1st horizontal line
      g.move(y=-distance) #1st vertical line
      while distance >= 3*tipsize:
          
        distance = distance-tipsize*2-spacing*2
      
        g.move(x=-distance)
        g.move(y=distance)
        
        if distance >= 3*tipsize:
            distance = distance-tipsize*2-spacing*2
      
            g.move(x=distance)
            g.move(y=-distance)
            
      g.toggle_pressure(COM)
      g.dwell(5)
      g.move(Z=3)
      
      g.abs_move(x=edge-tipsize*2-spacing)
      g.move(Z=-3)
                  
      #starts from middle right, under spiral left's start
      g.move(x=(leadin+tipsize/2+spacing/2)) 
      g.set_pressure(COM, pressure_fill)
      g.toggle_pressure(COM)
      g.dwell(3)
      g.move(x=-(leadin+tipsize/2+spacing/2))
      
      g.move(y=-(edge/2-tipsize/2)) #from halfway to starting corner
      distance = edge-tipsize*3-spacing*2
      g.move(x=-distance) #1st horizontal line
      g.move(y=distance) #1st vertical line
      while distance >= 3*tipsize:
          
        distance = distance-tipsize*2-spacing*2
      
        g.move(x=distance)
        g.move(y=-distance)
        
        if distance >= 3*tipsize:
            distance = distance-tipsize*2-spacing*2
      
            g.move(x=-distance)
            g.move(y=distance)

      g.toggle_pressure(COM)
      g.dwell(5)
      g.move(Z=spacing)
      g.move(Z=3)
            
            
from mecode import G
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/spiralcell/Spiralcell_left.txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header_minicaster.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer_minicaster.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = True, 
        )

spiral_left(edge, tipsize, spacing)

from mecode import G
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/spiralcell/Spiralcell_right.txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header_minicaster.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer_minicaster.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = True, 
        )

spiral_right(edge, tipsize, spacing)

from mecode import G
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/spiralcell/Spiralcell_fill.txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header_minicaster.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer_minicaster.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = True, 
        )

spiral_fill(edge, tipsize, spacing)

#To end
g.view(backend='matplotlib')
#g.view()
g.teardown()