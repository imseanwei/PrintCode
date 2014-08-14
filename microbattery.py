from mecode import G
g = G(
        outfile = "/Users/SeanWei/Documents/Python/PrintCode/microbattery/microbattery-single.pgm",
        #header = "/Users/SeanWei/Documents/Python/mecode/mecode/header_minicaster.txt",
        #footer = "/Users/SeanWei/Documents/Python/mecode/mecode/footer_minicaster.txt",
        #aerotech_include = True,
        direct_write = False,
        print_lines = False, 
        )
        
#Define variables
printvel = 150	#printvel; mm/min
tipsize = 0.030	#tipsize; mm  
layerheight =  1*tipsize  #stepheight; mm  
layers = 20    #layers, must be even
COM = 5		#air-line  
press= 50	#air-pressure,psi  
leadinx = 1.5 	#leadinx; mm  
teeth_length = 1.00000
separator_gap = 0.05
teeth_interdistance = 4*tipsize+2*separator_gap
teeth_amount = 5
column_x = 1
row_y = 1
spacing_x = 5
spacing_y = 3

#def function

def single_microbattery(COM, press, layerheight,layers,teeth_amount,teeth_length,tipsize,teeth_interdistance):
    #----Lead in--set-----  
    g.move(x=-leadinx)
    
    g.set_pressure(COM, press)
    g.toggle_pressure(COM)
    g.dwell(1)

    #----Lead in--go----  
    g.move(x=leadinx)
    
    dummy_z =  layerheight
    for i in range(layers/2):
    
        for i in range(teeth_amount-1):
            g.move(y=teeth_length)
            g.move(x=tipsize)
            g.move(y=-teeth_length)
            g.move(x=teeth_interdistance)
        
        g.move(y=teeth_length)
        g.move(x=tipsize)
        g.move(y=-teeth_length)
        g.abs_move(Z=dummy_z)
        dummy_z =  dummy_z+layerheight  
    
        for i in range(teeth_amount-1):
            g.move(y=teeth_length)
            g.move(x=-tipsize)
            g.move(y=-teeth_length)
            g.move(x=-teeth_interdistance)
        
        g.move(y=teeth_length)
        g.move(x=-tipsize)
        g.move(y=-teeth_length)
        g.abs_move(Z=dummy_z)
        dummy_z =  dummy_z+layerheight  
    
    g.toggle_pressure(COM)

#Code starts
g.set_home(x=0,y=0,Z=0)
g.feed(printvel)

for i in range(row_y):

    for i in range(column_x):
        single_microbattery(COM, press, layerheight,layers,teeth_amount,teeth_length,tipsize,teeth_interdistance)
        g.abs_move(Z=1)
        g.move(x=spacing_x)
        g.abs_move(Z=0)
    
    g.abs_move(Z=1)
    g.abs_move(x=0)
    g.move(y=spacing_y)
    g.abs_move(Z=0)
    
#To end
#g.view(backend='matplotlib')
g.view()
g.teardown()

