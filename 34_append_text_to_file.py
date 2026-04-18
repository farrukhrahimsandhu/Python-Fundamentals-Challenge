# Write a program to append text to a file.

with open("append_text_34.txt","a+") as f:
    data = f.write("Farrukh is appending this text to the text file named 'append_text_34'.\n")
    data = f.write("so remember it.")
    
    f.seek(0)
    written_text = f.read()
print(written_text)

# if you want to run the program more than 1 time , please remove all data from the text file first. 
# And then save the empty text file 