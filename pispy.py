import time
import glob
import camera as c

outdir = "~/photos/"
'''
trigger = False

while True:
    
    if trigger:
'''        
lt = time.localtime()

outname = "%02d%02d%02d_%s%s%s" % (lt[3], lt[4], lt[5], lt[2], lt[1], lt[0])

output = outdir + outname

c.take_photo( output )
