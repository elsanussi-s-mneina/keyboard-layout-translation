from main import convertKeyMapsFromQwertyToDvorak, convertKeyMapsFromQwertyToColemak


inputFile = open("qwertyKeyMapsInput.txt", "r")
print("Name of the file: ", inputFile.name)

qwertyKeymaps = "".join(inputFile.readlines())
inputFile.close()


print("converted from QWERTY to Dvorak, and written to a file.")
dvorakKeyMaps = convertKeyMapsFromQwertyToDvorak(qwertyKeymaps)
dvorakOutFile = open("dvorakKeyMapsOutput.txt", "w")
dvorakOutFile.write(dvorakKeyMaps)
dvorakOutFile.close()

print("converted from QWERTY to Colemak, and written to a file.")
colemakKeyMaps = convertKeyMapsFromQwertyToColemak(qwertyKeymaps)
colemakOutFile = open("colemakKeyMapsOutput.txt", "w")
colemakOutFile.write(colemakKeyMaps)
colemakOutFile.close()
