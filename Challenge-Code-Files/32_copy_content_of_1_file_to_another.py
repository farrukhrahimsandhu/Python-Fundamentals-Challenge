# Write a program to copy the contents of one file to another.

# function to copy read and copy data 
with open("Copy_from_32.txt","r") as f:
    data = f.read()
    print("This data is copyed:\n",data)

# function to copy data from other file 
with open("Copy_to_32.txt","w+") as g:
    g.write(data)
    g.seek(0)           # move cursor to start of file
    pasted = g.read()   # read back written content

    print("Here is the data that is copyed from other file:\n",pasted)

