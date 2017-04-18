# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination

def copy(source = 0, destination = 0):
    if source == 0 and destination == 0:
        print("copy [source] [destination]")
    if destination == 0:
        print("No destination provided")

    


copy()
