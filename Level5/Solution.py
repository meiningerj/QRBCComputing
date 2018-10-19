import subprocess

x = 2
y= 18243150071292141317265306851

while( True ):
	out = subprocess.check_output(["python","Level5.py",str(x),str(y/x)])
	x = x + 1
	print(out)
	print(x)
