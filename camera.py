import os

def take_photo( output ):
	
	os.system( 'raspistill -o %s' % output )