# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination

def copy(source = 0, destination = 0):
    source = source
    destination = destination
    if source == 0 and destination == 0:
        return print("copy [source] [destination]")
    if destination == 0:
        return print("No destination provided")
    fr = open(source, "r")
    data = fr.read()
    fr.close()
    fw = open(destination, "w")
    fw.write(data)
    fw.close()

copy("/Volumes/Kaleb/GreenFox/exam-basics/copy/test1.txt", "/Volumes/Kaleb/GreenFox/exam-basics/copy/test2.txt")

# 1. The exercise info provide vague information about what kind of funktion should I have to write. Its working now, but Im not sure this was the expected result.
# 2. I used absolute path for testing the funktion, because my txt editor (Atom) cant see files just by names. Anoying.
