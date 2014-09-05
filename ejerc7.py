a=int(raw_input("Ingrese Numero: "))
b=a*2
con1=1
con2=0
cad=""
while b>1:
	while con1>con2:
		cad=cad+str(con1) 
		con2=con2+1
	print cad
	cad=""
	con2=0
	if con1==a:
		con1=con1-1
		a=a-1
	else:
		con1=con1+1
	b=b-1