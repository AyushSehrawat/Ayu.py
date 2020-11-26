import youtube_dl
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


print('*******************************************************\n'
      '         Checking If you have required packages        \n')
install('youtube_dl')
print('\n*****************************************************\n'
      '                    Check Complete                   \n')



ydl_opts = {} 

def dwl_vid(): 
	with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
		ydl.download([zxt]) 

channel = 1
while (channel == int(1)):
	try:
		#
		link_of_the_video = input("\nCopy & paste the URL of the YouTube video you want to download:-  ") 
		zxt = link_of_the_video.strip()
		dwl_vid()
	except:
		print('\nSomething went wrong :(')

	 
	channel = int(input("\nEnter 1 if you want to download more videos \nEnter 0 if you are done:  ")) 
