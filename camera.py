import os

def take_photo( output ):
	
	os.system( 'raspistill -o %s' % output )
    
def delete_trigger( trigger ):
    
    os.system( 'rm ' + trigger )