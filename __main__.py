from tkinter import * # cf. https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/
from tkinter.messagebox import showinfo # https://blog.furas.pl/python-tkinter-how-to-create-popup-window-or-messagebox-gb.html
import webbrowser # https://stackoverflow.com/questions/4216985/call-to-operating-system-to-open-url
from tkinter.filedialog import askopenfilename, askdirectory # https://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog # https://stackoverflow.com/questions/10993089/opening-and-reading-a-file-with-askopenfilename
 
# Tkinter root window:
root = Tk()
root.title("BEGA (Browser Extension Graphical Analyzer)")
#root.geometry('600x400') # width x height
 
# All widgets will be here:

##### ##### ##### ##### ##### ##### #####
##### "Open .crx file" #####
##### ##### ##### ##### ##### ##### #####

def open_crx_file():
	crx_file_path = askopenfilename(filetypes=[("Chromium extension","*.crx")]) # show an "Open" dialog box and return the path to the selected file
	if crx_file_path == "":
		print(f"User selected no file.")
	else:
		print(f"User selected file: '{crx_file_path}'")
		pass

btn1 = Button(root, text = "Open .crx file", fg = "black", command=open_crx_file)
btn1.grid(column=0, row=0, padx=10, pady=10)



##### ##### ##### ##### ##### ##### #####
##### "Open unpacked Chrome extension" #####
##### ##### ##### ##### ##### ##### #####

def open_unpacked_chrome_extension():
	directory = askdirectory()
	if directory == "":
		print(f"User selected no directory.")
	else:
		print(f"User selected directory: '{directory}'")
		pass

btn2 = Button(root, text = "Open unpacked Chrome extension", fg = "black", command=open_unpacked_chrome_extension)
btn2.grid(column=0, row=1, padx=10, pady=10)



##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### "Download Chrome extension based on extension ID:" #####
##### ##### ##### ##### ##### ##### ##### ##### ##### #####

extension_ID_text_field = Text(root, height=1, width=33)
extension_ID_text_field.grid(column=0, row=4, padx=10, pady=10)

def download_chrome_extension_based_on_extension_ID():
	extension_ID = extension_ID_text_field.get("1.0",'end-1c') # https://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-widget
	if len(extension_ID) != 32 or not extension_ID.isalpha():
		showinfo("Incorrect Extension ID", f"'{extension_ID}' is not a valid Chrome extension ID. It must consist of exactly 32 letters.")
	else:
		url = "https://www.crx4chrome.com/search.php?s=" + extension_ID
		webbrowser.open(url, new=0, autoraise=True) # https://stackoverflow.com/questions/4216985/call-to-operating-system-to-open-url

btn3 = Button(root, text = "Download Chrome extension based on extension ID:", fg = "black", command=download_chrome_extension_based_on_extension_ID)
btn3.grid(column=0, row=3, padx=10, pady=10)

# Execute Tkinter:
root.mainloop()
