def makepic():
	s = "P3 512 512 255 "
	x = 0
	while x < 65536: #s56*256
		s += 12 * (str(x % 256) + " ") # produces 1 1 1, 2 2 2 etc
		print (x) #debugfest
		x+=1
	return s
	
file = open("image.ppm", "w")
file.write(makepic())
file.close()