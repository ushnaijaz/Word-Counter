from turtle import back
from PyPDF2 import PdfReader
import docx
from tkinter import *
from tkinter import filedialog

def main():
    # create a blank window
    window = Tk()
    window.geometry("500x500")
    window.title("Word Counter")    
    # window.configure(background="gray")
    
    def browser():
        filename = ""
        while filename == "":
            filename = filedialog.askopenfilename(title="Select a file", initialdir="./", filetypes=[("Word Documents", "*.docx"), ("PDF Files", "*.pdf"), ("Text Files", "*.txt")])
        explore_button.config(text=filename)
        result_window.config(state="normal")
        result_window.delete("1.0", END)
        result_window.insert(INSERT, counter(filename))
        result_window.config(state="disabled")

    explore_button = Button(window, text="Browse Files", command=browser)
    result_window = Text(window, width=55, height=25, state="disabled")   
    
    # place items in the window
    explore_button.place(x=20, y=20)
    result_window.place(x=20, y=50)
    

    window.mainloop()

def counter(filename):
    if filename.endswith(".pdf"):
        text = readPdf(filename)
    elif filename.endswith(".docx"):
        text = readDocx(filename)
    elif filename.endswith(".txt"):
        text = readTxt(filename)
    
    # split the string into a list of words
    words = text.split()
    # remove the trailing characters from the words and make them lowercase
    words = [word.lower().rstrip(",.:;?!\"").lstrip("\"") for word in words]
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    result = "\nWord count:\n"
    for word in sorted(word_count, key=word_count.get, reverse=True):
        result += word + ": " + str(word_count[word]) + "\n"
    
    return result

def readDocx(filepath):
    doc = docx.Document(filepath)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return "\n".join(fullText)

def readPdf(filepath):
    reader = PdfReader(filepath)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def readTxt(filepath):
    with open(filepath, "r") as f:
        return f.read()

main()
