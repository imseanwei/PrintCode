#battery-printer
#rely on home position set with 1st code loaded (separator)
#needs to re-zero "Z" between codes/syringes, but assume same x, y

#packaging bottom
#cathode
#separator
#packaging top
#anode
#sealing

from mecode import G

#nordson Tips sizes (color, inner diameter, outer diamter, in mm)   
#Olive 1.54 1.83
#Amber 1.36 1.65
#Grey 1.19 ??
#Green 0.84 1.27
#Pink 0.61 0.91
#Purple 0.51 0.82
#Blue 0.41 0.72
#Orange 0.33 0.65
#Red 0.25 0.52
#Clear 0.20 0.42
#Lavender 0.15 0.31
#Yellow 0.10 0.24


#Define variables
printvel = 150	#printvel; mm/min
printvel_pack = 100
printvel_sep = 100

tipsize_in = 1.54	#tipsize for electrodes, separator; mm
tipsize_out = 1.83	#tipsize for electrodes, separator; mm
tipsize_pack_in = 0.20 #tipsize for packaging; mm
tipsize_pack_out = 0.42 #tipsize for packaging; mm

square_edge = 20 #outer edge length in mm
square_thickness = 3 #outer edge to inner edge width in mm

offset_pack_in = square_thickness-tipsize_pack_out+(tipsize_pack_out-tipsize_pack_in)/2 #lower left corner
offset_pack_out = -(tipsize_pack_out-tipsize_pack_in)/2 #lower left corner

layers = 1    #layers for electrodes, separator; mm
layerheight =  0.5  #stepheight; mm  
layerheight_sep = 0.05
#layers_pack_1 = int((layers*layerheight)/tipsize_pack_in)+1
layers_pack_1 = (int((layers*layerheight)/tipsize_pack_in)+1)*2
layerheight_pack_1 = (layers*layerheight)/layers_pack_1
layers_pack_2 = int((layers*layerheight+layerheight_sep)/tipsize_pack_in)+1
layerheight_pack_2 = (layers*layerheight+layerheight_sep)/layers_pack_2
layerheight_seal = 0.1

port = 1
press = 30
press_pack = 20
press_sep = 30

number_x= 1
number_y = 1
spacing_x = 5.0
spacing_y = 5.0


#Define function
def pressure_set (line, press):
    line = 'M9000 P{line} Q{press}'.format(line=line, press=press)
    g.write(line)

def pressure_on ():
    g.write('M9001')

def pressure_off ():
    g.write('M10000')

def square_3D (path_length, path_width, nozzle_size, z_step, layers): #starts lower outer left, starts at absolute Z=0
    
        step_number = int(path_width/nozzle_size) + 1
        
        step_size = path_width/step_number
        
        for i in range (layers):
            g.move(Z=z_step)
            pressure_on()
            
            for i in range (step_number-1):
                g.move(x=path_length-nozzle_size-i*2*step_size)
                g.move(y=path_length-nozzle_size-i*2*step_size)
                g.move(x=-(path_length-nozzle_size-i*2*step_size))
                g.move(y=-(path_length-nozzle_size-i*2*step_size))
                g.move(x=step_size, y=step_size) 
                
            g.move(x=path_length-nozzle_size-(step_number-1)*2*step_size)
            g.move(y=path_length-nozzle_size-(step_number-1)*2*step_size)
            g.move(x=-(path_length-nozzle_size-(step_number-1)*2*step_size))
            g.move(y=-(path_length-nozzle_size-(step_number-1)*2*step_size))
            
            pressure_off()
            g.dwell(3)
            g.move(x=-step_size*(step_number-1), y=-step_size*(step_number-1))
                                                            
  
#file- 1packaging_bottom
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/squarecell/squarecell_20mm_3mm_1packaging_bottom.txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header_batteryprinter.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer_batteryprinter.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )

#Code starts
g.set_home(x=0,y=0,Z=0) #lower left corner, nozzle edge with substrate edge, absolute zero
g.feed(printvel_pack)
g.abs_move(Z=layerheight_pack_1)
g.abs_move(x=offset_pack_in, y=offset_pack_in, )
pressure_set(port, press_pack)
pressure_on()
        
for i in range(layers_pack_1):
    g.rect(square_edge-2*square_thickness+tipsize_pack_in, square_edge-2*square_thickness+tipsize_pack_in)
    g.move(Z=layerheight_pack_1)
        
pressure_off()
g.dwell(3.0)

g.abs_move(Z=5)
                
g.abs_move(x=offset_pack_out, y=offset_pack_out)
g.abs_move(Z=layerheight_pack_1)
pressure_set(port, press_pack)
pressure_on()
        
for i in range(layers_pack_1):
    g.rect(square_edge-tipsize_pack_in, square_edge-tipsize_pack_in)
    g.move(Z=layerheight_pack_1)
        
pressure_off()
g.dwell(3.0)
  
g.abs_move(Z=5)

#file - 2cathode
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/squarecell/squarecell_20mm_3mm_2cathode.txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header_batteryprinter.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer_batteryprinter.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )


#Code starts
g.abs_move(x=tipsize_pack_in+tipsize_out, y=tipsize_pack_in+tipsize_out)
g.abs_move(Z=0)
g.feed(printvel)
pressure_set(port, press)       
square_3D (square_edge-2*tipsize_pack_in, square_thickness-2*tipsize_pack_in, tipsize_out, layerheight, layers)
g.abs_move(Z=5)
        

#file - 3separator
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/squarecell/squarecell_20mm_3mm_3separator.txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header_batteryprinter.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer_batteryprinter.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )

#Code starts

g.abs_move(x=tipsize_pack_in+tipsize_out, y=tipsize_pack_in+tipsize_out)
g.abs_move(Z=layers*layerheight+layerheight_sep)
g.feed(printvel_sep)
pressure_set(port, press)       
square_3D (square_edge-2*tipsize_pack_in, square_thickness-2*tipsize_pack_in, tipsize_out, layerheight_sep, 1)
g.abs_move(Z=5)       

#file- 4packaging_top
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/squarecell/squarecell_20mm_3mm_4packaging_top.txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header_batteryprinter.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer_batteryprinter.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )

#Code starts
g.set_home(x=0,y=0,Z=0) #lower left corner, nozzle edge with substrate edge, absolute zero
g.feed(printvel_pack)
g.abs_move(x=offset_pack_in, y=offset_pack_in)
g.abs_move(Z=layers*layerheight+layerheight_sep+layerheight_pack_2)
pressure_set(port, press_pack)
pressure_on()
        
for i in range(layers_pack_2):
    g.rect(square_edge-2*square_thickness+tipsize_pack_in, square_edge-2*square_thickness+tipsize_pack_in)
    g.move(Z=layerheight_pack_2)
        
pressure_off()
g.dwell(3.0)

g.abs_move(Z=5)
                
g.abs_move(x=offset_pack_out, y=offset_pack_out)
g.abs_move(Z=layers*layerheight+layerheight_sep+layerheight_pack_2)
pressure_set(port, press_pack)
pressure_on()
        
for i in range(layers_pack_2):
    g.rect(square_edge-tipsize_pack_in, square_edge-tipsize_pack_in)
    g.move(Z=layerheight_pack_2)
        
pressure_off()
g.dwell(3.0)
  
g.abs_move(Z=5)


#file - 5anode
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/squarecell/squarecell_20mm_3mm_5anode.txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header_batteryprinter.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer_batteryprinter.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )


#Code starts
g.abs_move(x=tipsize_pack_in+tipsize_out, y=tipsize_pack_in+tipsize_out)
g.abs_move(Z=2*layers*layerheight+layerheight_sep)
g.feed(printvel)
pressure_set(port, press)       
square_3D (square_edge-2*tipsize_pack_in, square_thickness-2*tipsize_pack_in, tipsize_out, layerheight, layers)
g.abs_move(Z=5)


#file- 6seal
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/squarecell/squarecell_20mm_3mm_6seal.txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header_batteryprinter.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer_batteryprinter.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )

#Code starts
g.set_home(x=0,y=0,Z=0) #lower left corner, nozzle edge with substrate edge, absolute zero
g.feed(printvel_pack)
g.abs_move(x=offset_pack_in, y=offset_pack_in)
g.abs_move(Z=2*layers*layerheight+layerheight_sep+layerheight_seal)
pressure_set(port, press_pack)
pressure_on()        

g.rect(square_edge-2*square_thickness+tipsize_pack_in, square_edge-2*square_thickness+tipsize_pack_in)
       
pressure_off()
g.dwell(3.0)

g.abs_move(Z=5)
                
g.abs_move(x=offset_pack_out, y=offset_pack_out)
g.abs_move(Z=2*layers*layerheight+layerheight_sep+layerheight_seal)
pressure_set(port, press_pack)
pressure_on()
        
g.rect(square_edge-tipsize_pack_in, square_edge-tipsize_pack_in)
        
pressure_off()
g.dwell(3.0)
   
g.abs_move(Z=5)

       
               
#To end
#g.view(backend='matplotlib')
#g.view()
g.teardown()