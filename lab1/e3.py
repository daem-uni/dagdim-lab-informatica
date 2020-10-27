start1 = int(input("Inserire l'inizio uno: "))
start2 = int(input("Inserire l'inizio due: "))

end1 = int(input("Inserire la fine uno: "))
end2 = int(input("Inserire la fine due: "))

if start1 > start2:
	s = start1
else:
	s = start2

if end1 < end2:
	e = end1
else:
	e = end2

if s < e:
	print("Gli appuntamenti si sovrappongono")
else:
	print("Gli appuntamenti non si sovrappongono")
