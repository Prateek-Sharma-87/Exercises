#### Reading from a File ####

## Reading an Entire File

with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents)

"""
The first line of this program has a lot going on. Let's start by looking at the open() function. To do any work with a file, even just printing its contents, you first need to open the file to access it. The open() function needs one argument: the name of the file you want to open. Python looks for this file in the directory where the program that's currently being executed is stored. In this example, file_reader.py is currently running, so Python looks for pi_digits.txt in the directory where file_reader.py is stored. The open() function returns an object representing the file. Here, open('pi_digits.txt') returns an object representing pi_digits.txt. Python assigns this object to file_object, which we'll work with later in the program.

The keyword with closes the file once access to it is no longer needed. Notice how we call open() in this program but not close(). You could open and close the file by calling open() and close(), but if a bug in your program prevents the close() method from being executed, the file may never close. This may seem trivial, but improperly closed files can cause data to be lost or corrupted. And if you call close() too early in your program, you'll find yourself trying to work with a closed file (a file you can't access), which leads to more errors. It's not always easy to know exactly when you should close a file, but with the structure shown here, Python will figure that out for you. All you have to do is open the file and work with it as desired, trusting that Python will close it automatically when the with block finishes execution.

Once we have a file object representing pi_digits.txt, we use the read() method in the second line of our program to read the entire contents of the file and store it as one long string in contents. When we print the value of contents, we get the entire text file back.

The only difference between this output and the original file is the extra blank line at the end of the output. The blank line appears because read() returns an empty string when it reaches the end of the file; this empty string shows up as a blank line. If you want to remove the extra blank line, you can use rstrip() in the call to print(), as shown below.
"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents.rstrip())

## File Paths

"""
When you pass a simple filename like pi_digits.txt to the open() function, Python looks in the directory where the file that's currently being executed (that is, your .py program file) is stored. Sometimes, depending on how you organize your work, the file you want to open won't be in the same directory as your program file. For example, you might store your program files in a folder called python_work; inside python_work, you might have another folder called text_files to distinguish your program files from the text files they're manipulating. Even though text_files is in python_work, just passing open() the name of a file in text_files won't work, because Python will only look in python_work and stop there; it won't go on and look in text_files. To get Python to open files from a directory other than the one where your program file is stored, you need to provide a file path, which tells Python to
look in a specific location on your system.
"""

# Relative File Path

"""
Because text_files is inside python_work, you could use a relative file path to open a file from text_files. A relative file path tells Python to look for a given location relative to the directory where the currently running program file is stored. For example, you'd write:
"""

with open('text_files/filename.txt') as file_object:
    contents = file_object.read()

print(contents.rstrip())

"""
This line tells Python to look for the desired .txt file in the folder text_files and assumes that text_files is located inside python_work (which it is).

Pleas Note: Windows systems use a backslash (\) instead of a forward slash (/) when displaying file paths, but you can still use forward slashes in your code.
"""

# Absolute File Path

"""
You can also tell Python exactly where the file is on your computer regardless of where the program that's being executed is stored. This is called an absolute file path. You use an absolute path if a relative path doesn't work. For instance, if you've put text_files in some folder other than python_work—say, a folder called other_files—then just passing open() the path 'text_files/filename.txt' won't work because Python will only look for that location inside python_work. You'll need to write out a full path to clarify where you want Python to look.

Absolute paths are usually longer than relative paths, so it's helpful to
assign them to a variable and then pass that variable to open():
"""

file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
with open(file_path) as file_object:
    contents = file_object.read()

print(contents.rstrip())

"""
Using absolute paths, you can read files from any location on your system. For now it's easiest to store files in the same directory as your program files or in a folder such as text_files within the directory that stores your program files.

Please Note: If you try to use backslashes in a file path, you'll get an error because the backslash is used to escape characters in strings. For example, in the path "C:\path\to\file.txt", the sequence \t is interpreted as a tab. If you need to use backslashes, you can escape each one in the path, like this: "C:\\path\\to\\file.txt".
"""

#### Reading Line by Line ####

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

"""
First, we assign the name of the file we're reading from to the variable filename. This is a common convention when working with files. Because the variable filename doesn't represent the actual file—it's just a string telling Python where to find the file—you can easily swap out 'pi_digits.txt' for the name of another file you want to work with. After we call open(), an object representing the file and its contents is assigned to the variable file_object. We again use the with syntax to let Python open and close the file properly. To examine the file's contents, we work through each line
in the file by looping over the file object. When we print each line, we find even more blank lines:
"""

# Output ->
# 3.1415926535
# 
#   8979323846
#
#   2643383279
# 

"""
These blank lines appear because an invisible newline character is at the end of each line in the text file. The print function adds its own newline each time we call it, so we end up with two newline characters at the end of each line: one from the file and one from print(). Using rstrip() on each line in the print() call eliminates these extra blank lines:
"""

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Output ->
# 3.1415926535
#   8979323846
#   2643383279

#### Making a List of Lines from a File ####

"""
When you use with, the file object returned by open() is only available inside the with block that contains it. If you want to retain access to a file's contents outside the with block, you can store the file's lines in a list inside the block and then work with that list. You can process parts of the file immediately and postpone some processing for later in the program. The readlines() method takes each line from the file and stores it in a list.
"""

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#### Working with a File’s Contents ####

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# Output ->
# 3.1415926535 8979323846 2643383279
# 36

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# Output ->
# 3.141592653589793238462643383279
# 32

"""
Please Note: When Python reads from a text file, it interprets all text in the file as a string. If you read in a number and want to work with that value in a numerical context, you'll have to convert it to an integer using the int() function or convert it to a float using the float() function.
"""

#### Large Files: One Million Digits ####

"""
Python has no inherent limit to how much data you can work with; you can work with as much data as your system's memory can handle.
"""

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))   

#### Is Your Birthday Contained in Pi? ####

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

#### Writing to a File ####

## Writing to an Empty File

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

"""
The above program has no terminal output, but if you open the file programming.txt, you'll see one line: "love programming."

The second argument, 'w', tells Python that we want to open the file in write mode. You can open a file in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows you to read and write to the file ('r+'). If you omit the mode argument, Python opens the file in read-only mode by default.

The open() function automatically creates the file you're writing to if it doesn't already exist. However, be careful opening a file in write mode ('w') because if the file does exist, Python will erase the contents of the file before returning the file object.

Python can only write strings to a text file. If you want to store numerical data in a text file, you'll have to convert the data to string format first using the str() function.
"""

## Writing Multiple Lines

"""
Including newlines in your calls to write() makes each string appear on its own line. 
You can also use spaces, tab characters, and blank lines to format your output
"""

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

#### Appending to a File ####

"""
If you want to add content to a file instead of writing over existing content, you can 
open the file in append mode. When you open a file in append mode, Python doesn't erase 
the contents of the file before returning the file object. Any lines you write to the 
file will be added at the end of the file. If the file doesn't exist yet, Python will 
create an empty file for you.
"""

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

#### Exceptions ####

## Handling the ZeroDivisionError Exception - Using try-except Blocks

"""
When you think an error may occur, you can write a try-except block to
handle the exception that might be raised. You tell Python to try running
some code, and you tell it what to do if the code results in a particular kind
of exception.
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

"""
In the above code, if the code in a try block works, Python skips over the except block. 
If the code in the try block causes an error, Python looks for an except block whose
error matches the one that was raised and runs the code in that block. If more code followed 
the try-except block, the program would continue running because we told Python how to handle 
the error.
"""  

## Using Exceptions to Prevent Crashes

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

## The else Block

"""
We can make this program more error resistant by wrapping the line that
might produce errors in a try-except block. The error occurs on the line
that performs the division, so that's where we'll put the try-except block.
This example also includes an else block. Any code that depends on the try
block executing successfully goes in the else block.
"""
# --snip--
while True:
    # --snip--
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

"""
The try-except-else block works like this: Python attempts to run the
code in the try block. The only code that should go in a try block is code
that might cause an exception to be raised. Sometimes you'll have additional
code that should run only if the try block was successful; this code
goes in the else block. The except block tells Python what to do in case a
certain exception arises when it tries to run the code in the try block.

By anticipating likely sources of errors, you can write robust programs
that continue to run even when they encounter invalid data and missing
resources. Your code will be resistant to innocent user mistakes and malicious
attacks.
"""

## Handling the FileNotFoundError Exception

filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

"""
In this example, the code in the try block produces a FileNotFoundError,
so Python looks for an except block that matches that error. Python then
runs the code in that block, and the result is a friendly error message
instead of a traceback.

There are also two changes in the above code. One is the use of the 
variable f to represent the file object, which is a common convention. 
The second is the use of the encoding argument. This argument is needed 
when your system's default encoding doesn't match the encoding of the file 
that's being read.
"""

## Analyzing Text

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

## Working with Multiple Files

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

# Output ->
# The file alice.txt has about 29465 words.
# Sorry, the file siddhartha.txt does not exist.
# The file moby_dick.txt has about 215830 words.
# The file little_women.txt has about 189079 words.

"""
Using the try-except block in this example provides two significant
advantages. We prevent our users from seeing a traceback, and we let the
program continue analyzing the texts it's able to find. If we don't catch
the FileNotFoundError that siddhartha.txt raised, the user would see a full
traceback, and the program would stop running after trying to analyze
Siddhartha. It would never analyze Moby Dick or Little Women.
"""

## Failing Silently

"""
Sometimes you'll want the program to fail silently when an exception occurs
and continue on as if nothing happened. To make a program fail silently, you
write a try block as usual, but you explicitly tell Python to do nothing in the
except block. Python has a pass statement that tells it to do nothing in a block.

The pass statement also acts as a placeholder. It's a reminder that you're
choosing to do nothing at a specific point in your program's execution
and that you might want to do something there later. For example, in this
program we might decide to write any missing filenames to a file called
missing_files.txt. Our users wouldn't see this file, but we'd be able to read
the file and deal with any missing texts.
"""

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

#### Storing Data ####

"""
The json module allows you to dump simple Python data structures into a
file and load the data from that file the next time the program runs. You can
also use json to share data between different Python programs. Even better,
the JSON data format is not specific to Python, so you can share data you
store in the JSON format with people who work in many other programming
languages. It's a useful and portable format, and it's easy to learn.

Note: The JSON (JavaScript Object Notation) format was originally developed for JavaScript.
However, it has since become a common format used by many languages, including Python.
"""

## Using json.dump() and json.load()

"""
The json.dump() function takes two arguments: a piece of data to
store and a file object it can use to store the data.
"""

# Storing Data

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

# Loading Data

import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)

## Saving and Reading User-Generated Data

# Saving and Reading User-Generated Data

import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")

# Reading User-Generated Data

import json

filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

import json

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")

## Refactoring

"""
Often, you'll come to a point where your code will work, but you'll recognize
that you could improve the code by breaking it up into a series of functions
that have specific jobs. This process is called refactoring. Refactoring
makes your code cleaner, easier to understand, and easier to extend.
"""

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()

"""
This compartmentalization of work is an essential part of writing
clear code that will be easy to maintain and extend.
"""

