# Immport the requires Libraries

from tkinter import *
import PyPDF2
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfile

root = Tk()

# Set the geometry of Tkinter frame
root.geometry("1100x700")


#Create a canvas
canvas = Canvas(root, width=700, height=500)
canvas.grid(columnspan=5, rowspan=5)


# frame
frame = Frame(root, borderwidth=8)
Label(frame, text="PDF Extract",fg='grey', font="Times 33 bold italic").pack(side=TOP)
frame.grid(row=0, column=0)


# Load Image
photo = Image.open('pdfff.png')
# Resized Image
resized_photo = photo.resize((400, 250), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_photo)
canvas.create_image(300,200, image=photo)


# Create a Text box
my_text = Text(root, height=25, width=40)
my_text.grid(column=3, row=1, columnspan=16)


# Instruction
label = Label(root, text="Select PDF from your device to extract all its text here ",height=2, width=50, font='Arial', bg='light blue')
label.grid(rowspan=8, row=2 , column=0)


# Clear the textbox
def clear_text_box():
   my_text.delete(1.0, END)
   

# Exit button
def exit_tk():
    root.destroy() 

# Save file function
def save_file():
    file = filedialog.asksaveasfile(initialdir="C:/gui/",
                                    defaultextension= ".txt",
                                    filetypes=[("Text file", ".txt"),("HTML file", ".html"),("PDF file",".pdf") ,("All files", ".*")])
    file_text = str(my_text.get(1.0, END))
    file.write(file_text)
    file.close()

# Open our pdf file
def open_pdf():
    browse_text.set("loading...")
    # Grab the filename pf the pdf file
    open_file = filedialog.askopenfilename(
        initialdir="C:/gui/",
        filetypes=(
            ("PDF files", "*.pdf"),
            ("All Files", "*.*")
        )
    )    
    # Check to see if there is a file
    if open_file:
        # Open the pdf file
        pdf_file = PyPDF2.PdfFileReader(open_file)
        # set the page to read
        page = pdf_file.getPage(0)
        # extract the text from the pdf file
        page_stuff = page.extractText()

        # Add text to textbox
        my_text.insert(1.0, page_stuff)

        browse_text.set("Enter")


# Enter button
browse_text = StringVar()
button = Button(root, textvariable=browse_text, command=open_pdf,bg='pink', font="Raleway", fg="black", height=2, width=15,  compound="center")
browse_text.set("Enter_here")
button.grid(row=7, rowspan=4, column=0)
# lambda:open_pdf()

# Clear Button    
button_text = StringVar()
button2 = Button(root, text="Clear_Text",bg='light blue', font="Raleway", fg="black", height=3, width=16, command=clear_text_box)
button_text.set("Clear")
button2.grid(row=10 , column=11)



# Exit button
button3 = Button(root, fg='black',bg="grey", text="Exit", command=exit_tk, width=5)
button3.grid(column=13, row=20)


# save button
button4 = Button(root, text="Save", height=3, width=15,bg='snow', font="Raleway", fg="black", command=save_file)
button4.grid(row=10, column=13)


root.mainloop()



