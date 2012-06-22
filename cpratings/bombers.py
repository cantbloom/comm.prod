import os
f = open("bombers.txt")
lines = f.readlines()
f.close()
f = open("bombers.txt", mode = "w")
for l in lines:
	if "@" in l:
		l = l.split("@")[0]
	l = l.rstrip(os.linesep)
	f.write(l+"\n")
f.close()
