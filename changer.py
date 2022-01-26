fin = open("payloads.txt", "rt")
fout = open("payloadsnew.txt", "wt")
for line in fin:
	fout.write(line.replace('****', 'test'))
fin.close()
fout.close()