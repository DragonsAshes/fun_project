import sys
out = "beep"
print(sys.argv[1])

def get_frequence(note):
	if note[0] == "A":
		frequence = 440
	elif note[0] == "B":
		frequence = 494 
	elif note[0] == "C":
		frequence = 262
	elif note[0] == "D":
		frequence = 294
	elif note[0] == "E":
		frequence = 330
	elif note[0] == "F":
		frequence = 346
	else:
		frequence = 392

	if note[1] in ["b","#"]:
		if note[1] == "b":
			frequence += 16
		else:
			frequence -= 16
		octave = note[2]
	else:
		octave = note[1]
	return frequence*(2**(4-int(octave)))



music = open(sys.argv[1], "r")
for ligne in music:
	print(ligne)
	ligne = ligne.split(" ")
	f = get_frequence(ligne[0])
	print(f)
	out = out + " -f " + str(f) + " -l " + str(int(ligne[1])*250) + " -n"

val = len(out)
out = out[0:(val-3)]
print(out)
music.close()