# Word-Counter

This code is a simple word counting application that allows the user to select a file (in the format of .docx, .pdf, or .txt) and displays the number of occurrences of each word in the file.

## Functionality
 
The code uses the turtle library to create a blank window. The window has a button labeled "Browse Files" which allows the user to select a file to count the words in. Once a file is selected, the code uses the PyPDF2 library to read pdf files and docx library to read docx files. If the file is a .txt file, the code uses the built-in python open function to read the file.

Once the file is read, the code splits the text into a list of words and removes any trailing characters such as punctuation. The code then counts the number of occurrences of each word in the list and displays the result in the text box in the window.

This code is a very basic word counting application and can be enhanced as per the requirement.
