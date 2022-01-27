# Word-count...
## AIM:
To write a python program for getting the word count from a text.

## EQUIPEMENT'S REQUIRED: 
PC Anaconda - Python 3.7 .

## ALGORITHM: 
### Step 1:
Open visual studio code.

### Step 2: 
Create file with .py extension.

### Step 3: 
Start the program.

### Step 4:  
Write the code.

### Step 5: 
Run terminal for output of the given program.

### Step 6: 
End the program.

## PROGRAM:
```
'''Developed by Anto Richard.S
Reference no 21001221
To write a program for getting the word count from a file...'''

num_words =0
with open('text.txt','r') as file1:
    for i in file1:
        word =i.split()
        num_words += len(word)
print("Number of words={}".format(num_words))
```
## OUTPUT:
![output](out1.png)
![output](out2.png)

## RESULT:
Thus the program is written to find the word count from a text.
