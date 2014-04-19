import os
from Tkinter import *
import ttk
from ttk import *
import hashlib
#I'm not sure if `import PIL as PilImage` is still necessary?
import PIL as PilImage
from PIL import Image, ImageTk
import qrcode

#Start Tk
root = Tk()
root.title('Event Encrypted QR Ticket Generator')

#Create the frame to hold everything together
mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(row=0, column=0, sticky=(N+W+E+S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Create some StringVar()'s to display everything
first_last_name = StringVar()
event_name = StringVar()
admin_password = StringVar()
encrypted_data = StringVar()

#Create some entries for input from the user
#While we're at it align them to the grid
first_last_name_entry = ttk.Entry(mainframe, textvariable=first_last_name)
first_last_name_entry.grid(column=1, row=3, sticky=(W+E))
event_name_entry = ttk.Entry(mainframe, textvariable=event_name)
event_name_entry.grid(column=2, row=3, sticky=(W+E))
admin_password_entry = ttk.Entry(mainframe, textvariable=admin_password, show='*')
admin_password_entry.grid(column=3, row=3, sticky=(W+E))
#Create the startup qr code
qr_default = qrcode.QRCode (
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 2
)
qr_default.add_data('https://github.com/NamesJ/qr-tickets')
qr_default.make(fit=True)
qr_img_default = qr_default.make_image()
qr_img_default.save('default.png')
#Create a label for displaying the qr code
default_img = Image.open('default.png')
default_image = ImageTk.PhotoImage(default_img)
qr_label = Label(mainframe, image=default_image)
qr_label.image = default_image
qr_label.grid(column=2, row=4, sticky=(W+E))
#Here, the default event name is inserted
#for immediate display and convenience
event_name_entry.insert(0, 'DEFAULT EVENT NAME')

#Here is our function for encrypting,
#creating the qr code, and saving the qr code
def encryptData(*args):

    #Pull or "get" the data from entry
    name = first_last_name.get()
    event = event_name.get()
    admin = admin_password.get()
    #This variable should be set to whatever your password
    #after encryption equals.
    #This is a check to ensure that accidents are made when
    #typing your password
    passTest = 'ENCRYPTED STRING RESULTING FROM PASSWORD'
    #This creates our container to make a qr code
    qr = qrcode.QRCode (
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 2
    )

    #Create our encryption container
    m = hashlib.md5()
    #Create our password encryption container (mentioned above)
    entered_pass = hashlib.md5()
    #Plug-in our password to the container
    entered_pass.update(admin)
    #Digest it (create it)... yum
    entered_pass.hexdigest()
    #Add our entered information to an array for convenience
    data = [name, event, admin]

    #Create the folder for applicants if it doesn't already exist
    if (os.path.exists('applicants')) == False:
        os.makedirs('applicants')

    #Verify that the correct password was entered
    if str(entered_pass.hexdigest()) == passTest:
        if (os.path.exists('applicants/' + name)) == False:
            os.makedirs('applicants/' + name)

        #Update contact encryption
        for x in data:
            m.update(x)

        #Digest it (create it)... yum once more
        encrypted = m.hexdigest()

        #Add date to our qr code
        qr.add_data('Name: ' + name)
        qr.add_data('\r\nEvent name: ' + event)
        qr.add_data('\r\nEncrypted data: ' + encrypted)
        #Fit it properly (The fit is true sounds medieval)
        qr.make(fit=True)
        #Create a variable for our created qr code
        img = qr.make_image()
        #Save it as a png file
        img.save('applicants/' + name + '/' + name + '.png')

        #This writes the entered and encrypted information to a txt file
        my_file_name = 'applicants/' + name + '/' + name + '.txt'
        my_file = open(my_file_name, 'w')
        my_file.write('Name: ' + name)
        my_file.write('\n\nEvent name: ' + event)
        my_file.write('\n\nEncrypted data: ' + encrypted)
        my_file.close()

        #This will display the image on the label... after I fix it
        qr_img = Image.open('applicants/' + name + '/' + name + '.png')
        qr_image = ImageTk.PhotoImage(qr_img)
        qr_label.configure(image=qr_image)
        qr_label.image = qr_image
                
        encrypted_data = encrypted
        #need to del encrypted_data_entry
        encrypted_data_entry.insert(0, encrypted_data)
        
#This writes everything to the screen
encrypted_data_entry = ttk.Entry(mainframe, textvariable=encrypted_data)
encrypted_data_entry.grid(column=1, row=4, sticky=(W+E))
encrypted_data_entry.rowconfigure(0, weight=1)
ttk.Button(mainframe, text='Encrypt', command=encryptData).grid(column=3, row=4, sticky=W)

#Some labels (I keep accidentally writing lavels)
ttk.Label(mainframe, text='Name').grid(column=1, row=2, sticky=(W+E))
ttk.Label(mainframe, text='Event Name').grid(column=4, row=2, sticky=(W+E))
ttk.Label(mainframe, text='Administrave Password').grid(column=5, row=2, sticky=(W+E))

#This automatically adds some padding to everything
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
#This makes the blinky typing thing go straight to the name entry box
first_last_name_entry.focus()
#This makes enter also call the encryptData() fucntion
root.bind('<Return>', encryptData)

#Let's get loopy. This starts the GUI
root.mainloop()
