#minicaster
#needs to re-zero "Z" between codes/syringes, but assume same x, y

from mecode import G

#Define variables
printvel = 100	#printvel; mm/min
fly_height = 0.005 
line_length = 5
line_count = 25

port = 1
press = 30 #psi

line_offset_x = 0.2
line_offset_y = 0.1

start_x1 = 1
start_y1 = 1
start_z = fly_height

start_x2 = start_x1+line_offset_x
start_y2 = start_y1+line_offset_y

repeat_x= 3
repeat_y = 3
repeat_spacing_x = 10.0
repeat_spacing_y = 10.0

#file- 1
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/Nanjia_Interdigitated_Array_1Cathode_CC.txt",
        #header = "/Users/SeanWei/Documents/Python/PrintCode/header_batteryprinter.txt",
        #footer = "/Users/SeanWei/Documents/Python/PrintCode/footer_batteryprinter.txt",
        aerotech_include = True,
        direct_write = False,
        print_lines = False, 
        )

#Code starts
g.set_home(x=0,y=0,Z=0) #lower left corner, nozzle edge with substrate edge, absolute zero
g.feed(printvel)
g.abs_move(x=start_x1, y=start_y1, Z=start_z)
g.set_pressure(port, press)

for i in range(repeat_y):
    g.abs_move(y=repeat_spacing_y*(i))
    
    for i in range(repeat_x):
        g.abs_move(repeat_spacing_x*(i))
        
        for i in range(line_count):
            g.toggle_pressure(port)
            g.move(x=line_length)
            g.toggle_pressure(port)
            g.move(Z=1)
            g.move(x=-line_length,y=line_offset_y*2)
            g.abs_move(Z=start_z)


#file- 2
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/Nanjia_Interdigitated_Array_2Cathode.txt",
        #header = "/Users/SeanWei/Documents/Python/PrintCode/header_batteryprinter.txt",
        #footer = "/Users/SeanWei/Documents/Python/PrintCode/footer_batteryprinter.txt",
        aerotech_include = True,
        direct_write = False,
        print_lines = False, 
        )

#Code starts
g.set_home(x=0,y=0,Z=0) #lower left corner, nozzle edge with substrate edge, absolute zero
g.feed(printvel)
g.abs_move(x=start_x1, y=start_y1, Z=start_z)
g.set_pressure(port, press)

for i in range(repeat_y):
    g.abs_move(y=repeat_spacing_y*(i))
    
    for i in range(repeat_x):
        g.abs_move(repeat_spacing_x*(i))
        
        for i in range(line_count):
            g.toggle_pressure(port)
            g.move(x=line_length)
            g.toggle_pressure(port)
            g.move(Z=1)
            g.move(x=-line_length,y=line_offset_y*2)
            g.abs_move(Z=start_z)

#file - 3Anode
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/Nanjia_Interdigitated_Array_3Anode.txt",
        #header = "/Users/SeanWei/Documents/Python/PrintCode/header_batteryprinter.txt",
        #footer = "/Users/SeanWei/Documents/Python/PrintCode/footer_batteryprinter.txt",
        aerotech_include = True,
        direct_write = False,
        print_lines = False, 
        )

#Code starts
g.set_home(x=0,y=0,Z=0) #lower left corner, nozzle edge with substrate edge, absolute zero
g.feed(printvel)
g.abs_move(x=start_x2, y=start_y2, Z=start_z)
g.set_pressure(port, press)

for i in range(repeat_y):
    g.abs_move(y=repeat_spacing_y*(i))
    
    for i in range(repeat_x):
        g.abs_move(repeat_spacing_x*(i))
        
        for i in range(line_count):
            g.toggle_pressure(port)
            g.move(x=line_length)
            g.toggle_pressure(port)
            g.move(Z=1)
            g.move(x=-line_length,y=line_offset_y*2)
            g.abs_move(Z=start_z)

#To end
#g.view(backend='matplotlib')
#g.view()
g.teardown()