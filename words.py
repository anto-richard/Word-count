# Developed by Anto Richard.S
# Reference no 21001221
# To write a program for getting the word count from a file...

num_words =0
with open('text.txt','r') as file1:
    for i in file1:
        word =i.split()
        num_words += len(word)
print("Number of words={}".format(num_words))