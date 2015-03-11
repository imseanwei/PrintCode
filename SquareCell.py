#battery-printer

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

tipsize_in = 1.54	#tipsize for electrodes, separator; mm
tipsize_out = 1.83	#tipsize for electrodes, separator; mm
tipsize_pack_in = 0.51 #tipsize for packaging; mm
tipsize_pack_out = 0.82 #tipsize for packaging; mm

square_edge = 20 #outer edge length in mm
square_thickness = 3 #outer edge to inner edge width in mm

offset_pack_in = square_thickness-tipsize_pack_out+(tipsize_pack_out-tipsize_pack_in)/2 #lower left corner
offset_pack_out = -(tipsize_pack_out-tipsize_pack_in)/2 #lower left corner

fill_line_number = 2
fill_line_width = (square_thickness-2*tipsize_pack_in)/fill_line_number

layerheight =  0.5  #stepheight; mm  
layerheight_pack = tipsize_pack_in*0.8
layerheight_sep = 0.05

port = 1
press = 30
press_pack = 30
press_sep = 30

layers = 1    #layers for electrodes, separator; mm
layers_pack = int((layers*layerheight*2+layerheight_sep)/layerheight_pack)+1 #layers for packaging; mm

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


#file_1 - main_print
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/squarecell/squarecell_20mm_3mm_main.txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header_batteryprinter.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer_batteryprinter.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )


#Code starts
for i in range(number_y):
    
    for i in range(number_x):
        
        g.set_home(x=0,y=0,Z=0) #lower left corner, nozzle edge and packaging in contact, absolute zero
        g.feed(printvel)
        g.abs_move(Z=layerheight)
        pressure_set(port, press)
        pressure_on()
        
        for i in range(layers):
            g.rect(square_edge-2*tipsize_pack_in-tipsize_out,square_edge-2*tipsize_pack_in-tipsize_out)
            
            for i in range(fill_line_number):    
                g.move(fill_line_width, fill_line_width)
                g.rect(square_edge-2*tipsize_pack_in-tipsize_out-2*(i+1)*fill_line_width,square_edge-2*tipsize_pack_in-tipsize_out-2*(i+1)*fill_line_width)
            
            g.abs_move(x=0,y=0)
            g.move(Z=layerheight)
        
        pressure_off()
        g.dwell(3.0)
        g.rect(square_edge-2*tipsize_pack_in-tipsize_out,square_edge-2*tipsize_pack_in-tipsize_out) #to level residue
        
        g.abs_move(Z=5)
        
        if number_x != 1:
            g.move(x=spacing_x+square_edge)
            g.abs_move(Z=0)
    
    g.abs_move(Z=5)
    
    if number_y != 1:
        g.move(y=spacing_y+square_edge)
        g.abs_move(Z=0)
        
#file_2 - pack_print
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/squarecell/squarecell_20mm_3mm_pack.txt",
        header = "/Users/SeanWei/Documents/Python/PrintCode/header_batteryprinter.txt",
        footer = "/Users/SeanWei/Documents/Python/PrintCode/footer_batteryprinter.txt",
        aerotech_include = False,
        direct_write = False,
        print_lines = False, 
        )

#Code starts
for i in range(number_y):
    
    for i in range(number_x):

        g.set_home(x=0,y=0,Z=0) #lower left corner, nozzle edge with substrate edge, absolute zero
        g.feed(printvel)
        g.abs_move(x=offset_pack_in, y=offset_pack_in, Z=layerheight_pack)
        pressure_set(port, press_pack)
        pressure_on()
        
        for i in range(layers_pack):
            g.rect(square_edge-2*square_thickness+tipsize_pack_in, square_edge-2*square_thickness+tipsize_pack_in)
            g.move(Z=layerheight_pack)
        
        pressure_off()
        g.dwell(3.0)
        g.rect(square_edge-2*square_thickness+tipsize_pack_in, square_edge-2*square_thickness+tipsize_pack_in) #to level residue
        
        g.abs_move(Z=5)
                
        g.abs_move(x=offset_pack_out, y=offset_pack_out, Z=layerheight_pack)
        pressure_set(port, press_pack)
        pressure_on()
        
        for i in range(layers_pack):
            g.rect(square_edge-tipsize_pack_in, square_edge-tipsize_pack_in)
            g.move(Z=layerheight_pack)
        
        pressure_off()
        g.dwell(3.0)
        g.rect(square_edge-tipsize_pack_in, square_edge-tipsize_pack_in) #to level residue
        
        g.abs_move(x=0, y=0, Z=5)
        
        if number_x != 1:
            g.move(x=spacing_x+square_edge)
            g.abs_move(Z=0)
    
    g.abs_move(Z=5)
    
    if number_y != 1:
        g.move(y=spacing_y+square_edge)
        g.abs_move(Z=0)


#To end
#g.view(backend='matplotlib')
#g.view()
g.teardown()