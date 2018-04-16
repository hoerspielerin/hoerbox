hello world
---------------notes----------------------

cvlc 11.ogg --play-and-exit

killall vlc - abort

if os.path.isfile("/home/user/music/11111111.ogg"):
   print "file existing"
else:
   print "file not exiting"


------------------------------------------





------------------input-string-manipulation------------------
path = "/home/user/music/"
file_number = 111
file_ending = ".ogg"
actualString = path + str(file_number) + file_ending
print actualString
-------------------------------------------------------------

--------------check-existing-file----------------------------
if os.path.isfile(actualString):
	print "1 - Got a true expression value"
else:
   print "if is not true"
-------------------------------------------------------------   

 







