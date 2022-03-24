import logging as l

# below sets the default level, it will not print any errors lower than the level in lines 8 to 12
# change the filemode from append to write to overwrite the contents of the file each time
l.basicConfig(
    filename="debugging.log", 
    filemode="a", 
    level=l.DEBUG, 
    format="%(asctime)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s")

name = "joe"

l.error("this is an error")
l.critical("this is a critical error")
l.warning("don't know %s", name)
l.info("still running")
l.debug("still going")
