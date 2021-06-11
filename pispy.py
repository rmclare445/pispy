import time
import glob
import camera as c

outdir = "/home/ryan/photos/"

trigger = False

while True:
    
    print(glob.glob( '/home/ryan/*' ))
    
    if "click.txt" in glob.glob( '/home/ryan/*' ):
        
        lt = time.localtime()

        outname = "%02d%02d%02d_%02d%02d%04d.jpg" % (lt[3], lt[4], lt[5], lt[2], lt[1], lt[0])

        output = outdir + outname

        c.take_photo( output )
        
        c.delete_trigger( '/home/ryan/click.txt' )
        
    time.sleep(2)
