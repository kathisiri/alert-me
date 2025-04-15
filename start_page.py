# GUI first page
# Driver and emergency contact details before starting driving

# import packages
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import re

# import scripts
import drowsiness_classification

# regular expression for validating an email
REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def is_valid_email(email):
    """This function checks if the email address is valid"""
    return re.fullmatch(REGEX, email)

class InfoPage:

    def __init__(self, root):
        """This function initializes the info-page"""

        # root
        self.root = root
        self.root.title("Alert Me")
        self.root.geometry("800x420+100+50")
        self.root.resizable(False, False)  # disable resizing

        # info page frame
        info_page = Frame(root, bg="white")
        info_page.place(x=0, y=0, height=420, width=400)

        # background image
        background = ImageTk.PhotoImage(Image.open("../Data/logo.png").resize((400, 420)))  # resize background to fit half screen
        Label(self.root, image=background).place(x=400, y=0)  # place background on right side

        # Frame for logo (further reduced size)
        logo_frame = Frame(info_page, width=100, height=100, bg="white")  # Reduced size to 100x100
        logo_frame.place(x=150, y=10)  # Reduced top padding to 10

        # Load and display the logo image (reduced size)
        logo_image = ImageTk.PhotoImage(Image.open("../Data/alert.png").resize((100, 100)))  # Further reduced image size
        logo_label = Label(logo_frame, image=logo_image, background="white")
        logo_label.image = logo_image  # Prevent garbage collection
        logo_label.pack()

        # Note label (modern font)
        Label(info_page, text="Note that your contact will receive an email \n in case of a repeating drowsiness detection.", font=("Helvetica", 11, "normal"), fg="#666666", bg="white").place(x=30, y=120)

        # Driver name label and text box
        Label(info_page, text="Driver Name", font=("Helvetica", 12, "bold"), fg="#333333", bg="white").place(x=30, y=160)
        self.txt_driver_name = Entry(info_page, font=("Helvetica", 12), bg="#F1F1F1", bd=0, highlightthickness=1, highlightbackground="#CCCCCC", highlightcolor="#619BAF")
        self.txt_driver_name.place(x=35, y=190, width=330, height=28)  # Reduced height to 28px

        # Contact name label and text box
        Label(info_page, text="Contact Name", font=("Helvetica", 12, "bold"), fg="#333333", bg="white").place(x=30, y=230)
        self.txt_name_contact = Entry(info_page, font=("Helvetica", 12), bg="#F1F1F1", bd=0, highlightthickness=1, highlightbackground="#CCCCCC", highlightcolor="#619BAF")
        self.txt_name_contact.place(x=35, y=260, width=330, height=28)  # Reduced height to 28px

        # Contact email label and text box
        Label(info_page, text="Contact Email", font=("Helvetica", 12, "bold"), fg="#333333", bg="white").place(x=30, y=300)
        self.txt_email_contact = Entry(info_page, font=("Helvetica", 12), bg="#F1F1F1", bd=0, highlightthickness=1, highlightbackground="#CCCCCC", highlightcolor="#619BAF")
        self.txt_email_contact.place(x=35, y=330, width=330, height=28)  # Reduced height to 28px

        # Modern Start Driving button (Adjusted Placement)
        self.start_btn = Button(self.root, command=self.start_function, text="Start Driving", bg="#619BAF", fg="white", bd=0, font=("Helvetica", 13, "bold"), activebackground="#527A92", cursor="hand2", relief="flat")
        self.start_btn.place(x=135, y=370, width=140, height=35)  # Moved button up to 370px for better fit

        # infinite loop waiting for an event to occur and process the event as long as the window is not closed
        root.mainloop()

    def start_function(self):
        """This function checks the correctness of the input and starts the system, in case of missing or incorrect details messagebox will appear"""

        # if there is an empty field, show an error message
        if self.txt_email_contact.get() == "" or self.txt_driver_name.get() == "" or self.txt_name_contact.get() == "":
            messagebox.showerror("Error", "All fields are required.", parent=self.root)

        # if the email address is invalid, show an error message
        elif not is_valid_email(self.txt_email_contact.get()):
            messagebox.showerror("Error", "Invalid email address.", parent=self.root)

        # otherwise, show a success message, close the window and start driving
        else:
            messagebox.showinfo("Start Driving", f"{self.txt_driver_name.get()}, have a pleasant journey! \nYour emergency contact is {self.txt_name_contact.get()}. \n\nPlease wait a few seconds...", parent=self.root)
            username, contact_name, contact_email = self.txt_driver_name.get(), self.txt_name_contact.get(), self.txt_email_contact.get()  # these will be deleted when the root is destroyed
            self.root.destroy()
            drowsiness_classification.start_driving(username, contact_name, contact_email)

def main():
    InfoPage(Tk())

if __name__ == '__main__':
    main()
