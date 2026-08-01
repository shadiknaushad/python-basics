f = open("/Users/shadiknaushad/Developer/python_basics/fileHandling /demo.txt", "w")
f.write("hello, world!")
f.write("\nThis is new line")
f.close()

f = open("/Users/shadiknaushad/Developer/python_basics/fileHandling /demo.txt", "a")
f.write("\nAppending a new line to the file.")
f.close()

# r+ = read and write mode(overwrite from starting of the file)
# w+ = write and read mode(overwrites the file)
# a+ = append and read mode(does not overwrite the file)

f = open("/Users/shadiknaushad/Developer/python_basics/fileHandling /demo.txt", "r+")
f.write("i am very happy to code")
f.close()

f = open("/Users/shadiknaushad/Developer/python_basics/fileHandling /demo.txt", "a+")
f.write("am i really happy to code")
f.close()          


