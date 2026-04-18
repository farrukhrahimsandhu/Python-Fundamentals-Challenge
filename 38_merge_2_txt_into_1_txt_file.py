# Write a program to merge two text files into one.

with open("file_1st_38.txt","r") as f:
    text_1 = f.read()

with open("file_2nd_38.txt","r") as g:
    text_2 = g.read()


with open("merged_file_38.txt","w+") as mrgd:
    mrgd.write(text_1 + "\n\n" + text_2)

print("Files have been merged into 'merged_file_38.txt'")


